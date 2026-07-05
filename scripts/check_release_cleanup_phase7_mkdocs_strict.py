from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = ROOT / "mkdocs.yml"
DOCS = ROOT / ".mkdocs-src"


def fail(msg: str) -> None:
    raise SystemExit(f"Release cleanup phase 7 check failed: {msg}")


def require(path: str) -> None:
    if not (ROOT / path).exists():
        fail(f"missing {path}")


def main() -> None:
    require("scripts/sync_mkdocs_content.py")
    require("scripts/generate_mkdocs_nav.py")
    require(".github/workflows/course-quality.yml")
    require(".github/workflows/deploy-docs.yml")

    subprocess.run([sys.executable, "scripts/sync_mkdocs_content.py"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "scripts/generate_mkdocs_nav.py"], cwd=ROOT, check=True)

    if not DOCS.exists():
        fail(".mkdocs-src was not generated")

    text = MKDOCS.read_text(encoding="utf-8")
    for required in [
        "docs_dir: .mkdocs-src",
        "not_in_nav: |",
        "nav:",
        "modules/",
        "labs/",
        "course-templates/",
        "assessments/",
        "instructor/",
    ]:
        if required not in text:
            fail(f"mkdocs.yml missing expected text: {required}")

    if "release-notes/" in text and not (DOCS / "release-notes").exists():
        fail("mkdocs.yml references release-notes but .mkdocs-src/release-notes does not exist")

    course_quality = (ROOT / ".github/workflows/course-quality.yml").read_text(encoding="utf-8")
    for required in [
        "mkdocs build --strict",
        "labs/brokenpilot/prototype-app",
        "labs/toy-ml-attacks/toy-classifier-app",
        "pytest",
    ]:
        if required not in course_quality:
            fail(f"course-quality workflow missing expected text: {required}")

    deploy = (ROOT / ".github/workflows/deploy-docs.yml").read_text(encoding="utf-8")
    for required in ["workflow_dispatch", "mkdocs build --strict"]:
        if required not in deploy:
            fail(f"deploy workflow missing expected text: {required}")

    # If mkdocs is available, run the actual strict build. This is the acceptance gate.
    try:
        subprocess.run(["mkdocs", "build", "--strict"], cwd=ROOT, check=True)
    except FileNotFoundError:
        fail("mkdocs command not found in this environment")
    except subprocess.CalledProcessError as exc:
        fail(f"mkdocs build --strict failed with exit code {exc.returncode}")

    print("Release cleanup phase 7 MkDocs strict/navigation checks passed.")


if __name__ == "__main__":
    main()
