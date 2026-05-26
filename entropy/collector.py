import random
from datetime import UTC, datetime, timedelta

from httpx import Client
from pydantic import TypeAdapter

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
FRESHNESS_HRS   : int       = 25
DIFF_BUDGET     : int       = 50_000    # total diff chars fed to the model — bounded for any commit size
DIFF_PER_FILE   : int       = 10_000    # per-file cap so one huge file can't crowd out the rest
IGNORED_REPOS   : set[str]  = {"urav06/urav06"}
IGNORED_USERS   : set[str]  = set()  # Insert snowflakes here

# --- API Endpoints ---
GITHUB_API              : str = "https://api.github.com"
SEARCH_COMMITS_ENDPOINT : str = "/search/commits"
EVENTS_ENDPOINT         : str = "/users/{user}/received_events/public"
STARRED_ENDPOINT        : str = "/users/{user}/starred"
COMMITS_ENDPOINT        : str = "/repos/{repo}/commits"
FETCH_COMMIT_ENDPOINT   : str = "/repos/{repo}/commits/{sha}"

# --- Response validators (built once) ---
SEARCH_RESULTS : TypeAdapter[SearchResponse]      = TypeAdapter(SearchResponse)
EVENTS         : TypeAdapter[list[Event]]         = TypeAdapter(list[Event])
STARRED_REPOS  : TypeAdapter[list[StarredRepo]]   = TypeAdapter(list[StarredRepo])
REPO_COMMITS   : TypeAdapter[list[CommitSummary]] = TypeAdapter(list[CommitSummary])
COMMIT_DETAIL  : TypeAdapter[CommitResponse]      = TypeAdapter(CommitResponse)


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
        """ Search API to find self.user's latest commit directly. """

        query = " ".join([
            f"author:{self.user}",
            *(f"-repo:{r}" for r in IGNORED_REPOS),
            f"committer-date:>{self._cutoff.isoformat()}",
        ])

        if not (resp := self._get(SEARCH_COMMITS_ENDPOINT, SEARCH_RESULTS, q=query, per_page=1)):
            return None
        if not resp.items:
            return None

        hit = resp.items[0]
        return self.fetch_commit(RepoSlug(hit.full_name), CommitHash(hit.sha))

    def _scout_network(self) -> EntropySource | None:
        """ PushEvents from network → fetch commit. """

        if not (events := self._get(EVENTS_ENDPOINT.format(user=self.user), EVENTS, per_page=100)):
            return None

        for event in events:
            if event.type != "PushEvent":
                continue

            user: GitHubLogin   = GitHubLogin(event.actor)
            repo: RepoSlug      = RepoSlug(event.repo)
            sha : CommitHash    = CommitHash(event.head)

            if event.created_at < self._cutoff:
                break

            if user in IGNORED_USERS or repo in IGNORED_REPOS:
                continue

            if source := self.fetch_commit(repo, sha):
                return source

        return None

    def _scout_starred(self) -> EntropySource | None:
        """ Latest commit from a recently-pushed starred repo. """
        if not (repos := self._get(STARRED_ENDPOINT.format(user=self.user), STARRED_REPOS, per_page=50)):
            return None

        fresh_repos = [
            RepoSlug(r.full_name) for r in repos
            if r.pushed_at and r.pushed_at > self._cutoff
            and r.full_name not in IGNORED_REPOS
            and r.owner_login not in IGNORED_USERS
        ]
        random.shuffle(fresh_repos)

        for repo in fresh_repos:
            if not (commits := self._get(COMMITS_ENDPOINT.format(repo=repo), REPO_COMMITS, per_page=1)):
                continue

            source = self.fetch_commit(repo, CommitHash(commits[0].sha))
            if source and source.author_handle not in IGNORED_USERS:
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

        if not (data := self._get(FETCH_COMMIT_ENDPOINT.format(repo=repo, sha=sha), COMMIT_DETAIL)):
            return None

        return EntropySource(
            timestamp       = data.author_date,
            author_name     = data.author_name,
            author_handle   = GitHubLogin(data.author_login or "Unknown"),
            repo_slug       = repo,
            commit_hash     = sha,
            message         = data.message,
            diff            = self._pack_diff(data.files),
            permalink       = data.html_url,
        )

    def _pack_diff(self, files: list[FilePatch]) -> str:
        """ Join file patches under a per-file and total char budget, cutting on line boundaries. """
        blocks: list[str] = []
        for f in files:
            if not f.patch:
                continue
            patch = f.patch if len(f.patch) <= DIFF_PER_FILE else f.patch[:DIFF_PER_FILE].rsplit("\n", 1)[0] + "\n…"
            blocks.append(f"File: {f.filename}\n{patch}")

        diff = "\n\n".join(blocks)
        if len(diff) > DIFF_BUDGET:
            diff = diff[:DIFF_BUDGET].rsplit("\n", 1)[0] + "\n…[diff truncated]"
        return diff or "No text changes."

    def _get[T](self, endpoint: str, shape: TypeAdapter[T], **params: str | int) -> T | None:
        """ GET, then validate the body into shape; None on the expected 403/404 (private, deleted, etc.). """
        resp = self.client.get(endpoint, params=params)
        if resp.status_code in (403, 404):
            return None
        _ = resp.raise_for_status()
        return shape.validate_python(resp.json())
