from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "instructor/README.md",
    "instructor/toy-classifier-guide.md",
    "instructor/brokenpilot-guide.md",
    "instructor/mlops-evidence-pack-guide.md",
    "instructor/40-hour-delivery-plan.md",
]

REQUIRED_README_TEXT = [
    "teaching-the-course-narrative.md",
    "40-hour-delivery-plan.md",
    "40-hour-student-experience-runbook.md",
    "grading-calibration-guide.md",
    "toy-classifier-guide.md",
    "brokenpilot-guide.md",
    "mlops-evidence-pack-guide.md",
]

ARCHIVED_ROOT_FILES = [
    "instructor/FINAL_INSTRUCTOR_READINESS_REVIEW.md",
    "instructor/final-voice-cohesion-review-guide.md",
    "instructor/current-brokenpilot-capstone-debrief-guide.md",
]

STALE_PLAN_PATTERNS = [
    "Deep coverage + DVAIA lab",
    "DVAIA/BrokenPilot lab",
    "Local laptop, DVAIA, BrokenPilot",
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def main() -> None:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing: {rel}")

    instructor_readme = read("instructor/README.md")
    for needle in REQUIRED_README_TEXT:
        if needle not in instructor_readme:
            errors.append(f"instructor/README.md missing: {needle}")

    for rel in ARCHIVED_ROOT_FILES:
        if (ROOT / rel).exists():
            errors.append(f"release-process or stale file still in instructor root: {rel}")

    plan = read("instructor/40-hour-delivery-plan.md")
    for stale in STALE_PLAN_PATTERNS:
        if stale in plan:
            errors.append(f"40-hour delivery plan still has stale lab wording: {stale}")

    if "BrokenPilot" not in plan:
        errors.append("40-hour delivery plan does not mention BrokenPilot")

    if "DVAIA optional" not in plan and "DVAIA is optional" not in plan:
        errors.append("40-hour delivery plan should explicitly mark DVAIA optional")

    if errors:
        print("instructor-track check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("instructor-track check passed.")


if __name__ == "__main__":
    main()
