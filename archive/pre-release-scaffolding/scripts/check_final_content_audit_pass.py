from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "COURSE_CONTENT_AUDIT.md": ["content-complete criteria", "Module-by-module readiness", "Remaining content tasks before cleanup"],
    "COURSE_DRY_RUN_PLAN_40H.md": ["Day 1", "Day 5", "Dry-run output"],
    "labs/FINAL_LAB_READINESS_REVIEW.md": ["BrokenPilot readiness", "Toy-classifier readiness", "MLOps evidence-pack readiness"],
    "assessments/FINAL_ASSESSMENT_READINESS_REVIEW.md": ["Assessment principle", "Assessment map", "Capstone assessment check"],
    "instructor/FINAL_INSTRUCTOR_READINESS_REVIEW.md": ["Instructor must be able to explain", "Common instructor mistakes", "End-of-week success signal"],
    "course-templates/final-course-content-audit-template.md": ["Module review", "Lab review", "Cleanup readiness decision"],
    "release-notes/v1.1-dev-final-content-audit-pass.md": ["final content-readiness", "release-hardening"],
}

SOFT_EXPECTED = [
    "labs/brokenpilot/worked-examples/current-complete-final-report.md",
    "labs/toy-ml-attacks/toy-classifier-app/DEBRIEF_GUIDE.md",
    "labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    for rel, markers in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}")
        text = path.read_text(encoding="utf-8")
        if len(text) < 800:
            fail(f"file looks too thin: {rel}")
        lower = text.lower()
        for marker in markers:
            if marker.lower() not in lower:
                fail(f"{rel} missing marker: {marker}")

    print("Final content audit checks passed.")

    missing_soft = [rel for rel in SOFT_EXPECTED if not (ROOT / rel).exists()]
    if missing_soft:
        print("\nSoft reminders before cleanup:")
        for rel in missing_soft:
            print(f"- not found yet: {rel}")
        print("These are reminders, not failures. Apply the related content packages if they are still pending.")


if __name__ == "__main__":
    main()
