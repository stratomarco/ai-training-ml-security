from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[1]


COURSE_QUALITY = """\
name: Course Quality Checks

on:
  push:
    branches:
      - v1.1-dev-testable-labs
  pull_request:
  workflow_dispatch:

jobs:
  quality:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install course tooling
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Repository and content checks
        run: |
          python scripts/check_repo_structure.py
          python scripts/check_content_readiness.py
          python scripts/check_lab_targets.py
          python scripts/check_workflow_validation_baseline.py

      - name: Build MkDocs source and navigation
        run: |
          python scripts/sync_mkdocs_content.py
          python scripts/generate_mkdocs_nav.py
          python scripts/check_release_cleanup_phase7_mkdocs_strict.py

      - name: MkDocs strict build
        run: mkdocs build --strict

      - name: BrokenPilot tests
        working-directory: labs/brokenpilot/prototype-app
        run: |
          pip install -r requirements.txt
          pytest

      - name: Toy classifier tests
        working-directory: labs/toy-ml-attacks/toy-classifier-app
        run: |
          pip install -r requirements-dev.txt
          pytest
"""

DEPLOY_DOCS = """\
name: Deploy MkDocs site

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install MkDocs
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Generate MkDocs source and navigation
        run: |
          python scripts/sync_mkdocs_content.py
          python scripts/generate_mkdocs_nav.py
          python scripts/check_release_cleanup_phase7_mkdocs_strict.py

      - name: Build MkDocs site
        run: mkdocs build --strict

      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip().rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def run(cmd: list[str]) -> None:
    print("+ " + " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def append_once(path: Path, marker: str, text: str) -> None:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker not in current:
        write(path, current.rstrip() + "\n\n" + text.strip() + "\n")


def main() -> None:
    write(ROOT / ".github/workflows/course-quality.yml", COURSE_QUALITY)
    write(ROOT / ".github/workflows/deploy-docs.yml", DEPLOY_DOCS)

    # sync_mkdocs_content.py and generate_mkdocs_nav.py are shipped in this package.
    # Regenerate site source, then generate nav from the actual generated files.
    run([sys.executable, "scripts/sync_mkdocs_content.py"])
    run([sys.executable, "scripts/generate_mkdocs_nav.py"])

    append_once(
        ROOT / "CLEANUP_BEFORE_RELEASE.md",
        "Release cleanup phase 7",
        """
## Release cleanup phase 7

MkDocs strict navigation was regenerated from the actual published source tree.

Expected release behavior:

- `scripts/sync_mkdocs_content.py` creates `.mkdocs-src`.
- `scripts/generate_mkdocs_nav.py` regenerates `mkdocs.yml` navigation from files that exist.
- `mkdocs build --strict` is the release gate.
- CI runs the two runnable lab targets before publishing.
""",
    )

    write(
        ROOT / "release-notes/v1.1-dev-release-cleanup-phase7.md",
        """
# v1.1-dev release cleanup phase 7

This phase prepares MkDocs strict navigation for the release candidate.

Changes:

- Regenerate MkDocs source from canonical folders.
- Generate navigation from files that exist in `.mkdocs-src`.
- Declare intentional non-nav pages using `not_in_nav`.
- Re-enable `mkdocs build --strict` in course-quality and manual deploy workflows.
- Keep BrokenPilot and toy-classifier tests as CI gates.

This phase does not change course content or lab behavior.
""",
    )

    print("Applied release cleanup phase 7 MkDocs strict/navigation cleanup.")


if __name__ == "__main__":
    main()
