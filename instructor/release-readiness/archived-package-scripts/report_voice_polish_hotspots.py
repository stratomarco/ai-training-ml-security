
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

STUDENT_PATHS = [
    "README.md",
    "syllabus.md",
    "PUBLISHED_COURSE_VIEW.md",
    "labs",
    "modules",
    "course-templates",
    "assessments",
]

SKIP_PARTS = {
    ".git",
    ".venv",
    ".mkdocs-src",
    "site",
    "archive",
    "release-notes",
    "releases",
    "release-readiness",
    "__pycache__",
}

PHRASES = [
    "this package",
    "checked twice",
    "apply script",
    "the apply script",
    "generated",
    "placeholder",
    "todo",
    "fix later",
    "mkdocs fight",
    "no mkdocs fight",
    "student should",
    "students should",
    "best practices",
    "add guardrails",
    "improve security",
]

OPENING_PATTERNS = [
    re.compile(r"^this module\b", re.I),
    re.compile(r"^this lab\b", re.I),
    re.compile(r"^this exercise\b", re.I),
    re.compile(r"^students will\b", re.I),
]


def is_student_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if any(part in SKIP_PARTS for part in path.parts):
        return False
    if path.suffix.lower() != ".md":
        return False
    return any(rel == item or rel.startswith(item.rstrip("/") + "/") for item in STUDENT_PATHS)


def line_numbered_matches(path: Path) -> list[tuple[int, str, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    out: list[tuple[int, str, str]] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        low = line.lower()
        for phrase in PHRASES:
            if phrase in low:
                out.append((idx, phrase, line.strip()))
    return out


def opening_stats(path: Path) -> Counter[str]:
    counts: Counter[str] = Counter()
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        for pattern in OPENING_PATTERNS:
            if pattern.search(stripped):
                counts[pattern.pattern] += 1
    return counts


def main() -> None:
    files = [path for path in ROOT.rglob("*.md") if is_student_file(path)]
    print(f"Student-facing Markdown files scanned: {len(files)}")

    phrase_hits: list[tuple[str, int, str, str]] = []
    opening_counts: defaultdict[str, Counter[str]] = defaultdict(Counter)

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        for line_no, phrase, line in line_numbered_matches(path):
            phrase_hits.append((rel, line_no, phrase, line))
        counts = opening_stats(path)
        if counts:
            opening_counts[rel].update(counts)

    print("\nPhrase hotspots, review manually:")
    if not phrase_hits:
        print("- none")
    else:
        for rel, line_no, phrase, line in phrase_hits[:200]:
            print(f"- {rel}:{line_no}: [{phrase}] {line}")
        if len(phrase_hits) > 200:
            print(f"- ... {len(phrase_hits) - 200} more")

    print("\nRepeated opening patterns, review manually:")
    any_openings = False
    for rel, counts in sorted(opening_counts.items()):
        total = sum(counts.values())
        if total >= 3:
            any_openings = True
            print(f"- {rel}: {dict(counts)}")
    if not any_openings:
        print("- none above threshold")

    print("\nResult: report complete. These are review prompts, not automatic failures.")


if __name__ == "__main__":
    main()
