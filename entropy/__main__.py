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

    if len(sys.argv) == 3:  # noqa: PLR2004
        source = collector.fetch_commit(RepoSlug(sys.argv[1]), CommitHash(sys.argv[2]))
        if not source:
            sys.exit(f"Commit not found: {sys.argv[1]}@{sys.argv[2]}")
    else:
        source = collector.collect()

    curator.curate(alchemist.transmute(source))


if __name__ == "__main__":
    main()
