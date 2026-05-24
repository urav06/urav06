"""Domain types for the Entropy."""

from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from pydantic import BaseModel

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
# Validated at the boundary by the Collector. Optional fields are defaulted so
# eager validation tolerates the API's variety (e.g. non-PushEvents carry no
# payload.head, binary files carry no patch).

# --- Search API ---
class SearchRepository(BaseModel):
    full_name: str


class SearchHit(BaseModel):
    """One result from GET /search/commits"""

    sha         : str
    repository  : SearchRepository


class SearchResponse(BaseModel):
    """GET /search/commits response"""

    items: list[SearchHit]


# --- Events API ---
class EventRepo(BaseModel):
    name: str


class PushPayload(BaseModel):
    head: str = ""


class EventActor(BaseModel):
    login: str


class Event(BaseModel):
    """One event from GET /users/{user}/received_events"""

    type        : str  # "PushEvent", "WatchEvent", etc.
    repo        : EventRepo
    actor       : EventActor
    payload     : PushPayload
    created_at  : datetime


# --- Starred API ---
class RepoOwner(BaseModel):
    login: str


class StarredRepo(BaseModel):
    """One repo from GET /users/{user}/starred"""

    full_name   : str
    pushed_at   : datetime | None = None
    owner       : RepoOwner


# --- Commits API ---
class CommitAuthor(BaseModel):
    name: str
    date: datetime


class CommitData(BaseModel):
    author  : CommitAuthor
    message : str


class GitHubUser(BaseModel):
    login: str


class FilePatch(BaseModel):
    filename: str
    patch   : str = ""


class CommitSummary(BaseModel):
    sha: str


class CommitResponse(BaseModel):
    """GET /repos/{owner}/{repo}/commits/{sha} response"""

    commit  : CommitData
    author  : GitHubUser | None = None
    html_url: str
    files   : list[FilePatch] = []
