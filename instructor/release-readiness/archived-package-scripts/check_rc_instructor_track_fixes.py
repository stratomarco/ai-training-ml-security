from __future__ import annotations

import re
from pathlib import Path

ROOT = Path.cwd()


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    required = [
        "instructor/README.md",
        "instructor/toy-classifier-guide.md",
        "instructor/brokenpilot-guide.md",
        "instructor/mlops-evidence-pack-guide.md",
        "instructor/40-hour-delivery-plan.md",
    ]
    for rel in required:
        if not exists(rel):
            errors.append(f"missing required instructor-track file: {rel}")

    readme = read("instructor/README.md")
    for needle in [
        "Start here",
        "Per-module teaching notes",
        "Per-lab facilitation entry points",
        "toy-classifier-guide.md",
        "brokenpilot-guide.md",
        "mlops-evidence-pack-guide.md",
        "release-readiness",
    ]:
        if needle not in readme:
            errors.append(f"instructor/README.md missing: {needle}")

    for rel in [
        "instructor/FINAL_INSTRUCTOR_READINESS_REVIEW.md",
        "instructor/final-voice-cohesion-review-guide.md",
        "instructor/current-brokenpilot-capstone-debrief-guide.md",
        "instructor/toy-classifier-facilitation-guide.md",
        "instructor/toy-classifier-debrief-guide.md",
        "instructor/brokenpilot-standalone-facilitation-guide.md",
        "instructor/mlops-evidence-pack-facilitation-guide.md",
        "instructor/mlops-evidence-pack-model-answer-debrief.md",
    ]:
        if exists(rel):
            errors.append(f"superseded/root release or fragmented instructor file still present: {rel}")

    if not exists("instructor/release-readiness/archived-pre-release-docs"):
        errors.append("missing release-readiness archive directory")

    plan = read("instructor/40-hour-delivery-plan.md")
    stale_plan_terms = [
        "Local laptop, DVAIA, BrokenPilot",
        "Local laptop, DVAIA, and BrokenPilot",
        "Deep coverage + DVAIA lab",
        "DVAIA/BrokenPilot lab",
        "DVAIA / BrokenPilot lab",
    ]
    for term in stale_plan_terms:
        if term in plan:
            errors.append(f"40-hour plan still contains stale DVAIA-primary wording: {term}")

    if "BrokenPilot" not in plan:
        errors.append("40-hour plan does not mention BrokenPilot")
    if "DVAIA optional" not in plan and "DVAIA is optional" not in plan:
        warnings.append("40-hour plan does not explicitly say DVAIA optional")

    guide_expectations = {
        "instructor/toy-classifier-guide.md": ["Debrief prompts", "pytest", "Common instructor corrections"],
        "instructor/brokenpilot-guide.md": ["Debrief prompts", "prototype-app", "Module mapping"],
        "instructor/mlops-evidence-pack-guide.md": ["Debrief prompts", "evidence pack", "Expected student output"],
    }
    for rel, needles in guide_expectations.items():
        text = read(rel)
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel} missing: {needle}")

    # Catch obvious stale current-prefixed teaching references outside archive/release notes.
    for path in (ROOT / "instructor").glob("*.md"):
        if path.name.startswith("current-"):
            errors.append(f"current-prefixed instructor root file remains: {path.relative_to(ROOT)}")

    # Check that old app-local instructor notes, if present, are only pointers.
    app_notes = read("labs/toy-ml-attacks/toy-classifier-app/INSTRUCTOR_NOTES.md")
    if app_notes and "single instructor entry point" not in app_notes:
        warnings.append("toy-classifier app INSTRUCTOR_NOTES.md exists but may still contain duplicated guidance")

    if errors:
        print("RC instructor-track fix check failed:")
        for error in errors:
            print(f"- {error}")
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"- {warning}")
        raise SystemExit(1)

    print("RC instructor-track fix check passed.")
    if warnings:
        print("\nNon-blocking notes:")
        for warning in warnings:
            print(f"- {warning}")


if __name__ == "__main__":
    main()
