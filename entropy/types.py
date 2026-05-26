"""Domain types for the Entropy."""

from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from pydantic import AliasPath, BaseModel, Field

# ==========================================
# Domain Primitives
# ==========================================
GitHubLogin = NewType("GitHubLogin", str)   # e.g. "urav06"
RepoSlug    = NewType("RepoSlug", str)      # e.g. "urav06/dialectic"
CommitHash  = NewType("CommitHash", str)    # e.g. "7b3f1a2..."
HexColor    = NewType("HexColor", str)      # e.g. "#FF00FF"
ChaosScore  = NewType("ChaosScore", int)    # 0 to 100


# ==========================================
# Domain Entities
# ==========================================
@dataclass(frozen=True)
class EntropySource:
    """The raw material extracted from GitHub."""

    timestamp       : datetime
    author_name     : str
    author_handle   : GitHubLogin
    repo_slug       : RepoSlug
    commit_hash     : CommitHash
    message         : str
    diff            : str
    permalink       : str

    @property
    def repo_url(self) -> str:
        return f"https://github.com/{self.repo_slug}"

    @property
    def author_url(self) -> str:
        return f"https://github.com/{self.author_handle}"


@dataclass(frozen=True)
class Transmutation:
    """The Alchemist's analysis of the entropy."""

    source      : EntropySource
    critique    : str
    chaos_score : ChaosScore
    mood_color  : HexColor


# ==========================================
# GitHub API Response Models
# ==========================================
# Validated at the boundary by the Collector. Field-aliases flatten the API's
# nesting down to the values we actually read; a missing or null path falls back
# to the field default, so non-PushEvents, null authors and binary files (no
# patch) all validate cleanly.

# --- Search API: GET /search/commits ---
class SearchHit(BaseModel):
    sha         : str
    full_name   : str = Field(validation_alias=AliasPath("repository", "full_name"))


class SearchResponse(BaseModel):
    items: list[SearchHit]


# --- Events API: GET /users/{user}/received_events ---
class Event(BaseModel):
    type        : str  # "PushEvent", "WatchEvent", etc.
    created_at  : datetime
    repo        : str = Field(validation_alias=AliasPath("repo", "name"))
    actor       : str = Field(validation_alias=AliasPath("actor", "login"))
    head        : str = Field("", validation_alias=AliasPath("payload", "head"))


# --- Starred API: GET /users/{user}/starred ---
class StarredRepo(BaseModel):
    full_name   : str
    pushed_at   : datetime | None = None
    owner_login : str = Field(validation_alias=AliasPath("owner", "login"))


# --- Commits API: GET /repos/{repo}/commits[/{sha}] ---
class FilePatch(BaseModel):
    filename: str
    patch   : str = ""


class CommitSummary(BaseModel):
    sha: str


class CommitResponse(BaseModel):
    html_url    : str
    message     : str             = Field(validation_alias=AliasPath("commit", "message"))
    author_name : str             = Field(validation_alias=AliasPath("commit", "author", "name"))
    author_date : datetime        = Field(validation_alias=AliasPath("commit", "author", "date"))
    author_login: str | None      = Field(None, validation_alias=AliasPath("author", "login"))
    files       : list[FilePatch] = []
