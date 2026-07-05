from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def append_once(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker not in text:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
        write(path, text)


def write_course_quality_workflow() -> None:
    workflow = '''
name: Course Quality Checks

on:
  push:
    branches:
      - v1.1-dev-testable-labs
  pull_request:
  workflow_dispatch:

jobs:
  repo-and-content-checks:
    name: Repo and content checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install course tooling
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Repository structure
        run: python scripts/check_repo_structure.py

      - name: Content readiness
        run: python scripts/check_content_readiness.py

      - name: Lab target presence
        run: python scripts/check_lab_targets.py

  brokenpilot-tests:
    name: BrokenPilot tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install BrokenPilot dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r labs/brokenpilot/prototype-app/requirements.txt

      - name: Run BrokenPilot tests
        working-directory: labs/brokenpilot/prototype-app
        run: pytest

  toy-classifier-tests:
    name: Toy classifier tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install toy classifier dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r labs/toy-ml-attacks/toy-classifier-app/requirements-dev.txt

      - name: Run toy classifier tests
        working-directory: labs/toy-ml-attacks/toy-classifier-app
        run: pytest

  mkdocs-smoke-test:
    name: MkDocs smoke test, non-strict
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install MkDocs dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          pip install mkdocs-material

      - name: Generate MkDocs source
        run: python scripts/sync_mkdocs_content.py

      - name: Build MkDocs site without strict nav enforcement
        run: mkdocs build
'''
    write(ROOT / ".github/workflows/course-quality.yml", workflow)


def write_deploy_workflow() -> None:
    workflow = '''
name: Deploy MkDocs site

on:
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    name: Build site
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install MkDocs dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          pip install mkdocs-material

      - name: Generate MkDocs source
        run: python scripts/sync_mkdocs_content.py

      - name: Build MkDocs site
        run: mkdocs build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    name: Deploy site
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
'''
    write(ROOT / ".github/workflows/deploy-docs.yml", workflow)


def write_validation_baseline() -> None:
    text = '''
# Validation Baseline for v1.1-dev

This branch is still in course buildout and cleanup. The validation baseline protects the parts of the course that are stable enough to gate every push.

## Active gates

Run these before committing substantial changes:

```powershell
python scripts/check_repo_structure.py
python scripts/check_content_readiness.py
python scripts/check_lab_targets.py
```

BrokenPilot:

```powershell
cd labs\\brokenpilot\\prototype-app
pytest
```

Toy classifier:

```powershell
cd labs\\toy-ml-attacks\\toy-classifier-app
pytest
```

## MkDocs status

MkDocs is currently a smoke test only:

```powershell
python scripts\\sync_mkdocs_content.py
mkdocs build
```

Do not use `mkdocs build --strict` as a required gate until the final navigation cleanup is complete.

## Postponed gates

These return in the final release-hardening phase:

- strict MkDocs navigation
- orphan-page failure
- final CI release checklist
- final public-site deploy automation
- cleanup verification for archived package-era scripts

## Why this baseline exists

Earlier workflows used release-grade MkDocs checks while content and lab routing were still moving. That created false failures and made useful development harder. This baseline protects runnable labs and core course readiness without blocking on website polish.
'''
    write(ROOT / "VALIDATION_BASELINE.md", text)


def write_workflow_check() -> None:
    text = '''
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"missing required workflow file: {rel}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        raise SystemExit(f"workflow readiness check failed: {where} missing {needle!r}")


def forbid(text: str, needle: str, where: str) -> None:
    if needle in text:
        raise SystemExit(f"workflow readiness check failed: {where} still contains {needle!r}")


def main() -> None:
    cq = read(".github/workflows/course-quality.yml")
    deploy = read(".github/workflows/deploy-docs.yml")

    require(cq, "check_repo_structure.py", "course-quality.yml")
    require(cq, "check_content_readiness.py", "course-quality.yml")
    require(cq, "check_lab_targets.py", "course-quality.yml")
    require(cq, "labs/brokenpilot/prototype-app", "course-quality.yml")
    require(cq, "labs/toy-ml-attacks/toy-classifier-app", "course-quality.yml")
    require(cq, "pytest", "course-quality.yml")
    require(cq, "mkdocs build", "course-quality.yml")
    forbid(cq, "mkdocs build --strict", "course-quality.yml")

    require(deploy, "workflow_dispatch", "deploy-docs.yml")
    require(deploy, "mkdocs build", "deploy-docs.yml")
    forbid(deploy, "mkdocs build --strict", "deploy-docs.yml")

    baseline = ROOT / "VALIDATION_BASELINE.md"
    if not baseline.exists():
        raise SystemExit("workflow readiness check failed: VALIDATION_BASELINE.md missing")

    print("Workflow and validation cleanup checks passed.")


if __name__ == "__main__":
    main()
'''
    write(ROOT / "scripts/check_workflow_validation_baseline.py", text)


def update_cleanup_notes() -> None:
    block = '''
## Release cleanup phase 3 status

Workflow and validation cleanup has started.

Current development gates:

- repository structure check
- content readiness check
- lab target presence check
- BrokenPilot pytest
- toy-classifier pytest
- non-strict MkDocs smoke build

Postponed until final release hardening:

- MkDocs strict navigation
- orphan-page failure
- public deploy automation on every push
- deletion of archived buildout material
- final generated-phrasing cleanup
'''
    append_once(ROOT / "CLEANUP_BEFORE_RELEASE.md", "## Release cleanup phase 3 status", block)


def update_release_notes() -> None:
    text = '''
# v1.1-dev Release Cleanup Phase 3

This cleanup phase resets workflows and validation to the correct development baseline.

## Changed

- Course quality workflow now protects repo structure, content readiness, lab target presence, BrokenPilot tests, toy-classifier tests, and a non-strict MkDocs smoke build.
- Deploy workflow is manual-only during cleanup.
- Strict MkDocs navigation remains postponed until final release hardening.
- Added `VALIDATION_BASELINE.md`.
- Added `scripts/check_workflow_validation_baseline.py`.

## Not changed

- No course content was rewritten.
- No lab behavior was changed.
- No MkDocs strict navigation cleanup was attempted.
'''
    write(ROOT / "release-notes/v1.1-dev-release-cleanup-phase3.md", text)


def main() -> None:
    write_course_quality_workflow()
    write_deploy_workflow()
    write_validation_baseline()
    write_workflow_check()
    update_cleanup_notes()
    update_release_notes()
    print("\nApplied release cleanup phase 3.")


if __name__ == "__main__":
    main()
