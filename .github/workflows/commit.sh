#!/bin/bash
# Commit and push changes to the repository
# Usage: commit.sh "commit message"

set -e

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git add README.md image.png museum/
git diff --staged --quiet || git commit -m "$1"
git push
