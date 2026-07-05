from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".mkdocs-src"
STATIC_DOCS = ROOT / "docs"

CANONICAL_DIRS = [
    "modules",
    "labs",
    "course-templates",
    "instructor",
    "assessments",
    "releases",
    "release-notes",
]

CANONICAL_FILES = [
    "syllabus.md",
    "references.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "VERSION.md",
    "LICENSE.md",
    "LICENSE-CONTENT.md",
    "LICENSE-CODE.md",
    "COMMERCIAL-LICENSE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CONTENT_STRATEGY.md",
    "CONTENT_QUALITY_EDITING_GUIDE.md",
    "SOURCE_OF_TRUTH.md",
    "SECURITY.md",
    "course-map.md",
    "glossary.md",
    "PUBLISHED_COURSE_VIEW.md",
    "COURSE_RELEASE_MANIFEST.md",
    "COURSE_STORYLINE.md",
    "USAGE_AND_LICENSING_GUIDE.md",
    "RELEASE_TAGGING_GUIDE.md",
]


def copy_dir(src: Path, dst: Path) -> None:
    if not src.exists():
        return

    if dst.exists():
        shutil.rmtree(dst)

    shutil.copytree(
        src,
        dst,
        ignore=shutil.ignore_patterns(
            ".git",
            ".venv",
            "__pycache__",
            ".pytest_cache",
            "site",
            ".mkdocs-src",
            "node_modules",
            "*.pyc",
            "model.pkl",
        ),
    )


def copy_file(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)

    OUT.mkdir(parents=True, exist_ok=True)

    if STATIC_DOCS.exists():
        for item in STATIC_DOCS.iterdir():
            if item.name in {
                "README.md",
                "modules",
                "labs",
                "templates",
                "course-templates",
                "instructor",
                "assessments",
                "releases",
                "release-notes",
            }:
                continue

            target = OUT / item.name
            if item.is_dir():
                copy_dir(item, target)
            else:
                copy_file(item, target)

    for dirname in CANONICAL_DIRS:
        copy_dir(ROOT / dirname, OUT / dirname)

    for filename in CANONICAL_FILES:
        copy_file(ROOT / filename, OUT / filename)

    index = OUT / "index.md"
    if not index.exists():
        index.write_text(
            "# AI Training: ML Security\n\n"
            "Welcome to the AI Training ML Security course.\n",
            encoding="utf-8",
            newline="\n",
        )

    print(f"MkDocs source generated at: {OUT}")


if __name__ == "__main__":
    main()
