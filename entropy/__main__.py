"""
Entropy pipeline runner.

Usage:
    uv run python -m entropy              # Auto mode
    uv run python -m entropy REPO SHA     # Manual mode
"""

import sys
from os import environ
from pathlib import Path

import matplotlib as mpl

from entropy.alchemist import Alchemist
from entropy.collector import EntropyCollector
from entropy.curator import Curator
from entropy.types import CommitHash, GitHubLogin, RepoSlug

mpl.use("Agg")


def main() -> None:
    """Run the entropy pipeline."""
    token       = environ["GITHUB_TOKEN"]
    user        = GitHubLogin(environ.get("GITHUB_USER", "urav06"))
    collector   = EntropyCollector(token, user)
    alchemist   = Alchemist(environ["GOOGLE_API_KEY"])
    curator     = Curator(Path.cwd())

    match sys.argv[1:]:
        case [repo, sha]:
            source = collector.fetch_commit(RepoSlug(repo), CommitHash(sha))
            if not source:
                sys.exit(f"Commit not found: {repo}@{sha}")
        case []:
            source = collector.collect()
        case _:
            sys.exit("Usage: python -m entropy [REPO SHA]")

    curator.curate(alchemist.transmute(source))


if __name__ == "__main__":
    main()
