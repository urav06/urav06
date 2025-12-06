import re
import shutil
from datetime import UTC, datetime, timedelta
from pathlib import Path

from entropy.painter import paint
from entropy.types import Transmutation

# --- Configuration ---
MARKER_START    : str   = "<!-- ENTROPY:START -->"
MARKER_END      : str   = "<!-- ENTROPY:END -->"
MUSEUM_MAX_AGE  : int   = 14
TEMPLATE_PATH   : Path  = Path(__file__).parent / "resources" / "exhibit_template.md"


def _today() -> datetime:
    return datetime.now(UTC)

class Curator:
    """ Manages README lifecycle: archive → paint → update → cleanup. """

    def __init__(self, repo_root: Path) -> None:
        """ Initialize curator with repository root path. """
        self.repo_root  : Path  = repo_root
        self.readme     : Path  = repo_root / "README.md"
        self.image      : Path  = repo_root / "image.png"
        self.museum     : Path  = repo_root / "museum"
        self.template   : str   = TEMPLATE_PATH.read_text()
        self.museum.mkdir(parents=True, exist_ok=True)

    def curate(self, transmutation: Transmutation) -> None:
        """ Archive current, paint new, update README, cleanup old. """
        self._archive_current(transmutation)
        paint(transmutation, self.image)
        self._update_readme(transmutation)
        self._cleanup_museum()

    def _archive_current(self, transmutation: Transmutation) -> None:
        """ Move current exhibit to museum before replacement. """
        if not self.image.exists():
            return None

        content = self._read_readme()
        start   = content.find(MARKER_START)
        end     = content.find(MARKER_END)

        if start == -1 or end == -1:
            raise RuntimeError("README.md is missing markers")

        current_section = content[start : end + len(MARKER_END)]
        folder_path     = self._museum_folder(current_section)

        if folder_path.exists():
            shutil.rmtree(folder_path)

        folder_path.mkdir(parents=True)
        shutil.copy2(self.image, folder_path / "image.png")
        (folder_path / "README.md").write_text(current_section, encoding="utf-8")

    def _museum_folder(self, section: str) -> Path:
        """ Generate museum folder path: YYYYMMDD_repo_sha4 from archived section. """
        match = re.search(r'\*\*Commit:\*\* \[([^\]]+)\].*\[`([a-f0-9]+)`\]', section)
        if match:
            repo_name = match.group(1).split("/")[-1]
            sha4      = match.group(2)[:4]
        else:
            repo_name = "unknown"
            sha4      = "0000"
        folder_name = f"{_today().strftime('%Y%m%d')}_{repo_name}_{sha4}"
        return self.museum / folder_name

    def _read_readme(self) -> str:
        if self.readme.exists():
            return self.readme.read_text(encoding="utf-8")
        return ""

    def _update_readme(self, transmutation: Transmutation) -> None:
        """Update README with new dynamic section."""
        if not self.readme.exists():
            msg = f"README not found at {self.readme}"
            raise FileNotFoundError(msg)

        original    = self.readme.read_text(encoding="utf-8")
        section     = self._render_section(transmutation)
        updated     = self._inject_section(original, section)

        _ = self.readme.write_text(updated, encoding="utf-8")

    def _cleanup_museum(self) -> None:
        """ Remove museum exhibits older than MUSEUM_MAX_AGE days. """
        cutoff = _today().date() - timedelta(days=MUSEUM_MAX_AGE)

        for folder in self.museum.iterdir():
            if not folder.is_dir():
                continue
            try:
                folder_date = datetime.strptime(folder.name[:8], "%Y%m%d").replace(tzinfo=UTC).date()
                if folder_date < cutoff:
                    shutil.rmtree(folder)
            except ValueError:
                continue

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
            message         = s.message,
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
