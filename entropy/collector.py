import random
from datetime import UTC, datetime, timedelta
from typing import cast

from httpx import Client

from entropy.types import (
    CommitHash,
    CommitResponse,
    CommitSummary,
    EntropySource,
    Event,
    FilePatch,
    GitHubLogin,
    RepoSlug,
    SearchResponse,
    StarredRepo,
)

# --- Configuration ---
FRESHNESS_HRS: int      = 25
IGNORED_REPOS: set[str] = {"urav06/urav06"}
IGNORED_USERS: set[str] = set()  # Insert snowflakes here

# --- API Endpoints ---
GITHUB_API              : str = "https://api.github.com"
SEARCH_COMMITS_ENDPOINT : str = "/search/commits"
EVENTS_ENDPOINT         : str = "/users/{user}/received_events/public"
STARRED_ENDPOINT       : str = "/users/{user}/starred"
COMMITS_ENDPOINT        : str = "/repos/{repo}/commits"
FETCH_COMMIT_ENDPOINT   : str = "/repos/{repo}/commits/{sha}"


class EntropyCollector:
    def __init__(self, token: str, user: GitHubLogin) -> None:
        self.user   : GitHubLogin   = user
        self.client : Client        = Client(
            base_url= GITHUB_API,
            headers = {
                "Authorization"         : f"Bearer {token}",
                "Accept"                : "application/vnd.github+json",
                "X-GitHub-Api-Version"  : "2022-11-28",
            },
            timeout = 15.0,
        )
        self._cutoff: datetime = datetime.now(UTC) - timedelta(hours=FRESHNESS_HRS)

    def collect(self) -> EntropySource:

        return (
            self._scout_self()
            or self._scout_network()
            or self._scout_starred()
            or self._summon_legend()
        )

    # --- Scouts ---
    def _scout_self(self) -> EntropySource | None:
        """ Search API to Find self.user's latest commit directly. """

        query = " ".join([
            f"author:{self.user}",
            *(f"-repo:{r}" for r in IGNORED_REPOS),
            f"committer-date:>{self._cutoff.isoformat()}",
        ])

        if not (resp := self._get(SEARCH_COMMITS_ENDPOINT, params={"q": query, "per_page": 1})):
            return None

        if not (items := cast("SearchResponse", resp)["items"]):
            return None

        return self.fetch_commit(
            RepoSlug(items[0]["repository"]["full_name"]), CommitHash(items[0]["sha"])
        )

    def _scout_network(self) -> EntropySource | None:
        """ PushEvents from network → fetch commit. """

        if not (resp := self._get(EVENTS_ENDPOINT.format(user=self.user), params={"per_page": 100})):
            return None

        for event in cast(list[Event], resp):
            if event["type"] != "PushEvent":
                continue

            user: GitHubLogin   = GitHubLogin(event["actor"]["login"])
            repo: RepoSlug      = RepoSlug(event["repo"]["name"])
            sha : CommitHash    = CommitHash(event["payload"]["head"])

            if self._parse_ts(event["created_at"]) < self._cutoff:
                break

            if user in IGNORED_USERS or repo in IGNORED_REPOS:
                continue

            if source := self.fetch_commit(repo, sha):
                return source

        return None

    def _scout_starred(self) -> EntropySource | None:
        """ Latest commit from a recently-pushed starred repo. """
        if not (resp := self._get(STARRED_ENDPOINT.format(user=self.user), params={"per_page": 50})):
            return None

        repos       = cast(list[StarredRepo], resp)
        fresh_repos = [
            RepoSlug(r["full_name"]) for r in repos
            if self._parse_ts(r.get("pushed_at") or "2000-06-01") > self._cutoff
            and r["full_name"] not in IGNORED_REPOS
            and r["owner"]["login"] not in IGNORED_USERS
        ]
        random.shuffle(fresh_repos)

        for repo in fresh_repos:
            if not (resp := self._get(COMMITS_ENDPOINT.format(repo=repo), params={"per_page": 1})):
                continue

            if (
                len(commits := cast(list[CommitSummary], resp)) > 0
                and (source := self.fetch_commit(repo, CommitHash(commits[0]["sha"])))
                and (source.author_handle not in IGNORED_USERS)
            ):
                return source

        return None

    def _summon_legend(self) -> EntropySource:
        """ Fallback: The legendary Linux genesis commit. """
        result = self.fetch_commit(
            RepoSlug("torvalds/linux"),
            CommitHash("1da177e4c3f41524e886b7f1b8a0c1fc7321cac2"),
        )
        if not result:
            raise RuntimeError("There is a glitch in the matrix.")
        return result

    # --- Helpers ---
    def fetch_commit(self, repo: RepoSlug, sha: CommitHash) -> EntropySource | None:
        """ Fetch a specific commit by repo and SHA. """

        if not (resp := self._get(FETCH_COMMIT_ENDPOINT.format(repo=repo, sha=sha))):
            return None

        data    = cast(CommitResponse, resp)
        author  = data["author"]
        commit  = data["commit"]

        return EntropySource(
            timestamp       = datetime.fromisoformat(commit["author"]["date"]),
            author_name     = commit["author"]["name"],
            author_handle   = GitHubLogin(author["login"] if author else "Unknown"),
            repo_slug       = repo,
            commit_hash     = sha,
            message         = commit["message"],
            diff            = self._pack_diff(data.get("files", [])),
            permalink       = data["html_url"],
        )

    def _pack_diff(self, files: list[FilePatch], max_len: int = 3000) -> str:
        """ Pack file patches into a buffer, prioritizing larger diffs. """
        patches = [(f["filename"], f.get("patch", "")) for f in files if f.get("patch")]
        patches.sort(key=lambda x: len(x[1]), reverse=True)

        buffer: list[str] = []
        length = 0
        for name, patch in patches:
            entry = f"File: {name}\n{patch}\n\n"
            if length + len(entry) > max_len:
                remaining = max_len - length
                if remaining > 50:
                    buffer.append(f"File: {name}\n{patch[:remaining]}...[Truncated]")
                break
            buffer.append(entry)
            length += len(entry)

        return "".join(buffer) or "No text changes."

    def _get(self, endpoint: str, params: dict[str, str | int] | None = None) -> object | None:
        """ Safe GET """
        resp = self.client.get(endpoint, params=params)
        if resp.status_code in (403, 404):
            return None  # Expected: private repo, deleted, etc.
        _ = resp.raise_for_status()
        return resp.json()

    @staticmethod
    def _parse_ts(ts: str) -> datetime:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
