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
    "QUALITY_IMPROVEMENT_PLAN.md",
    "SOURCE_OF_TRUTH.md",
]


def copy_dir(src: Path, dst: Path) -> None:
    if not src.exists():
        print(f"skip missing dir: {src.relative_to(ROOT)}")
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
        ),
    )
    print(f"copied dir: {src.relative_to(ROOT)}")


def copy_file(src: Path, dst: Path) -> None:
    if not src.exists():
        print(f"skip missing file: {src.relative_to(ROOT)}")
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"copied file: {src.relative_to(ROOT)}")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)

    OUT.mkdir(parents=True, exist_ok=True)

    if STATIC_DOCS.exists():
        for item in STATIC_DOCS.iterdir():
            if item.name in {
                "modules",
                "labs",
                "templates",
                "course-templates",
                "instructor",
                "assessments",
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
    readme = OUT / "README.md"
    if not index.exists() and readme.exists():
        shutil.copy2(readme, index)

    print(f"\nMkDocs source generated at: {OUT}")


if __name__ == "__main__":
    main()
