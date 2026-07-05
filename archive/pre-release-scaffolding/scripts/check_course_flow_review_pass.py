from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()

REQUIRED_FILES = [
    "COURSE_FLOW_REVIEW.md",
    "labs/LAB_COVERAGE_AND_MATURITY_MATRIX.md",
    "modules/MODULE_SEQUENCE_AND_DEPENDENCY_MAP.md",
    "labs/brokenpilot/CAPSTONE_INTEGRATION_MAP.md",
    "assessments/END_TO_END_ASSESSMENT_MAP.md",
    "instructor/teaching-the-course-as-one-journey.md",
    "COURSE_COMPLETION_SCORECARD.md",
]

MODULE_IDS = [f"{i:02d}" for i in range(1, 13)]

REQUIRED_TERMS = [
    "Completion decision",
    "BrokenPilot",
    "toy classifier",
    "MLOps",
    "capstone",
    "residual risk",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        fail(f"missing {path}")
    return target.read_text(encoding="utf-8")


def main() -> None:
    for path in REQUIRED_FILES:
        text = read(path)
        if len(text.split()) < 250:
            fail(f"{path} looks too thin")

    flow = read("COURSE_FLOW_REVIEW.md")
    for term in REQUIRED_TERMS:
        if term not in flow:
            fail(f"COURSE_FLOW_REVIEW.md missing term: {term}")
    for module_id in MODULE_IDS:
        if f"{module_id}" not in flow:
            fail(f"COURSE_FLOW_REVIEW.md missing module id {module_id}")

    matrix = read("labs/LAB_COVERAGE_AND_MATURITY_MATRIX.md")
    for phrase in ["Observable failure", "Observable fix", "Reasoning", "Runnable"]:
        if phrase not in matrix:
            fail(f"lab matrix missing {phrase}")

    sequence = read("modules/MODULE_SEQUENCE_AND_DEPENDENCY_MAP.md")
    for phrase in ["Foundations", "Application behavior", "Lifecycle and data risk", "Testing and synthesis"]:
        if phrase not in sequence:
            fail(f"sequence map missing phase {phrase}")

    capstone = read("labs/brokenpilot/CAPSTONE_INTEGRATION_MAP.md")
    for phrase in ["Direct prompt injection", "Insecure output handling", "Memory poisoning", "Minimum evidence set"]:
        if phrase not in capstone:
            fail(f"capstone map missing {phrase}")

    scorecard = read("COURSE_COMPLETION_SCORECARD.md")
    for phrase in ["Definition of content complete", "Remaining content tasks before cleanup", "Cleanup tasks after content complete"]:
        if phrase not in scorecard:
            fail(f"scorecard missing {phrase}")

    cleanup = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    if cleanup.exists():
        cleanup_text = cleanup.read_text(encoding="utf-8")
        if "Course flow review" not in cleanup_text:
            fail("CLEANUP_BEFORE_RELEASE.md was not updated with course flow review cleanup note")

    print("Course flow review pass checks passed.")


if __name__ == "__main__":
    main()
