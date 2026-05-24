import re
from datetime import UTC, datetime
from pathlib import Path

from entropy.painter import paint
from entropy.types import Transmutation

# --- Configuration ---
MARKER_START    : str   = "<!-- ENTROPY:START -->"
MARKER_END      : str   = "<!-- ENTROPY:END -->"
MSG_MAX_CHARS   : int   = 250
MSG_MAX_LINES   : int   = 6
TEMPLATE_PATH   : Path  = Path(__file__).parent / "resources" / "exhibit_template.md"


def _today() -> datetime:
    return datetime.now(UTC)


def _format_message(message: str) -> str:
    """ Truncate and fence a commit message so its markdown can't hijack the page. """
    lines = [line.rstrip() for line in message.strip().splitlines()]
    while lines and not lines[-1]:
        lines.pop()

    truncated = len(lines) > MSG_MAX_LINES
    lines     = lines[:MSG_MAX_LINES]

    text = "\n".join(lines)
    if len(text) > MSG_MAX_CHARS:
        text      = text[:MSG_MAX_CHARS].rstrip()
        truncated = True

    if truncated:
        text += "\n…"

    longest_tilde_run = max((len(m.group()) for m in re.finditer(r"~+", text)), default=0)
    fence             = "~" * max(3, longest_tilde_run + 1)
    return f"{fence}\n{text}\n{fence}"


class Curator:
    """ Manages the README's dynamic section: paint → update. """

    def __init__(self, repo_root: Path) -> None:
        """ Initialize curator with repository root path. """
        self.repo_root  : Path  = repo_root
        self.readme     : Path  = repo_root / "README.md"
        self.image      : Path  = repo_root / "image.png"
        self.template   : str   = TEMPLATE_PATH.read_text()

    def curate(self, transmutation: Transmutation) -> None:
        """ Paint the new attractor and splice it into the README. """
        paint(transmutation, self.image)
        self._update_readme(transmutation)

    def _update_readme(self, transmutation: Transmutation) -> None:
        """Update README with new dynamic section."""
        if not self.readme.exists():
            msg = f"README not found at {self.readme}"
            raise FileNotFoundError(msg)

        original    = self.readme.read_text(encoding="utf-8")
        section     = self._render_section(transmutation)
        updated     = self._inject_section(original, section)

        _ = self.readme.write_text(updated, encoding="utf-8")

    def _render_section(self, transmutation: Transmutation) -> str:
        """ Generate the dynamic markdown section. """
        t = transmutation
        s = t.source

        repo_url   = f"https://github.com/{s.repo_slug}"
        author_url = f"https://github.com/{s.author_handle}"
        commit_url = f"{repo_url}/commit/{s.commit_hash}"

        commit_line = (
            f"[{s.repo_slug}]({repo_url}) by "
            f"[@{s.author_handle}]({author_url}) · [`{s.commit_hash[:7]}`]({commit_url})"
        )

        return self.template.format(
            MARKER_START    = MARKER_START,
            MARKER_END      = MARKER_END,
            today           = _today().strftime("%Y-%m-%d"),
            timestamp       = int(_today().timestamp()),
            image_name      = self.image.name,
            commit_line     = commit_line,
            message         = _format_message(s.message),
            critique        = t.critique,
            chaos_score     = t.chaos_score,
            mood_color      = t.mood_color,
        )

    def _inject_section(self, text: str, section: str) -> str:
        """Replace content between markers."""
        start   = text.find(MARKER_START)
        end     = text.find(MARKER_END)

        if start == -1 or end == -1:
            return text + "\n" + section

        return text[:start] + section + text[end + len(MARKER_END) :]
