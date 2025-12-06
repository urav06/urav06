"""Domain types for the Entropy."""

from dataclasses import dataclass
from datetime import datetime
from typing import NewType, NotRequired, TypedDict

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
# GitHub API Response Types
# ==========================================

# --- Search API ---
class SearchRepository(TypedDict):
    full_name: str


class SearchHit(TypedDict):
    """One result from GET /search/commits"""
    sha         : str
    repository  : SearchRepository


class SearchResponse(TypedDict):
    """GET /search/commits response"""
    items: list[SearchHit]


# --- Events API ---
class EventRepo(TypedDict):
    name: str


class PushPayload(TypedDict):
    head: str


class EventActor(TypedDict):
    login: str


class Event(TypedDict):
    """One event from GET /users/{user}/received_events"""
    type        : str  # "PushEvent", "WatchEvent", etc.
    repo        : EventRepo
    actor       : EventActor
    payload     : PushPayload
    created_at  : str


# --- Starred API ---
class RepoOwner(TypedDict):
    login: str


class StarredRepo(TypedDict):
    """One repo from GET /users/{user}/starred"""

    full_name   : str
    pushed_at   : str | None
    owner       : RepoOwner


# --- Commits API ---
class CommitAuthor(TypedDict):
    name: str
    date: str


class CommitData(TypedDict):
    author  : CommitAuthor
    message : str


class GitHubUser(TypedDict):
    login: str


class FilePatch(TypedDict):
    filename: str
    patch   : NotRequired[str]


class CommitSummary(TypedDict):
    sha: str


class CommitResponse(TypedDict):
    """GET /repos/{owner}/{repo}/commits/{sha} response"""

    commit  : CommitData
    author  : GitHubUser | None
    html_url: str
    files   : NotRequired[list[FilePatch]]
