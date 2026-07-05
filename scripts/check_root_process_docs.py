from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RELEASE_PROCESS_DIR = ROOT / "instructor" / "release-readiness" / "release-process-docs"

FORBIDDEN_EXACT = {
    "CLEANUP_BEFORE_RELEASE.md",
    "FINAL_HUMAN_POLISH_REPORT.md",
    "FINAL_RELEASE_REVIEW.md",
    "GENERATED_SCAFFOLDING_CLEANUP_REPORT.md",
    "QUALITY_GATE_BASELINE.md",
    "VALIDATION_BASELINE.md",
    "VOICE_POLISH_PASS_REPORT.md",
    "STYLE_AND_VOICE_FINAL_PASS.md",
    "RELEASE_CANDIDATE_CHECKLIST.md",
    "RELEASE_CHECKLIST.md",
    "QUALITY_IMPROVEMENT_PLAN.md",
    "project-backlog.md",
}

ALLOWED_ROOT_MARKDOWN = {
    "README.md",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "COMMERCIAL-LICENSE.md",
    "CONTENT_QUALITY_EDITING_GUIDE.md",
    "CONTENT_STRATEGY.md",
    "CONTRIBUTING.md",
    "COURSE_RELEASE_MANIFEST.md",
    "COURSE_STORYLINE.md",
    "LICENSE.md",
    "LICENSE-CODE.md",
    "LICENSE-CONTENT.md",
    "PUBLISHED_COURSE_VIEW.md",
    "README_PACKAGE.md",  # caught separately by final artifact check; allowed here for package application only
    "REFERENCES.md",
    "RELEASE_TAGGING_GUIDE.md",
    "ROADMAP.md",
    "SECURITY.md",
    "SOURCE_OF_TRUTH.md",
    "USAGE_AND_LICENSING_GUIDE.md",
    "VERSION.md",
    "course-map.md",
    "glossary.md",
    "references.md",
    "syllabus.md",
}

FORBIDDEN_PATTERNS = [
    re.compile(r".*REPORT\.md$"),
    re.compile(r".*CHECKLIST\.md$"),
    re.compile(r".*BASELINE\.md$"),
    re.compile(r"^FINAL_.*\.md$"),
    re.compile(r"^VOICE_POLISH_.*\.md$"),
    re.compile(r"^GENERATED_SCAFFOLDING_.*\.md$"),
    re.compile(r"^CLEANUP_.*\.md$"),
]


def looks_like_process_doc(name: str) -> bool:
    if name in FORBIDDEN_EXACT:
        return True
    if name in ALLOWED_ROOT_MARKDOWN:
        return False
    return any(pattern.match(name) for pattern in FORBIDDEN_PATTERNS)


def main() -> None:
    errors: list[str] = []

    for path in sorted(ROOT.glob("*.md")):
        name = path.name
        if looks_like_process_doc(name):
            errors.append(
                f"root process/checklist/report doc should live under "
                f"instructor/release-readiness/release-process-docs/: {name}"
            )

    if not RELEASE_PROCESS_DIR.exists():
        errors.append("missing release process document home: instructor/release-readiness/release-process-docs/")

    if errors:
        print("root process-doc guard failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("root process-doc guard passed.")


if __name__ == "__main__":
    main()
