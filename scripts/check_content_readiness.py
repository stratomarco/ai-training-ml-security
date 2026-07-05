from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    "01-security-engineering-for-ai",
    "02-ml-system-architecture",
    "03-owasp-ml-top-10",
    "04-biml-architectural-risk-analysis",
    "05-llm-application-security",
    "06-rag-security",
    "07-agent-tool-security",
    "08-secure-mlops-supply-chain",
    "09-privacy-attacks",
    "10-adversarial-ml-robustness",
    "11-ai-red-team-methodology",
    "12-capstone-brokenpilot",
]

NORMAL_MODULE_FILES = [
    "README.md",
    "student-reading-guide.md",
    "deep-dive.md",
    "attack-anatomy.md",
    "controls-and-remediations.md",
    "common-mistakes.md",
    "worked-example.md",
]

CAPSTONE_FILES = [
    "README.md",
    "student-reading-guide.md",
    "lab-path.md",
    "capstone-checkpoints.md",
    "final-report-current-path.md",
]

CORE_FILES = [
    "README.md",
    "syllabus.md",
    "course-map.md",
    "labs/RUNNABLE_AND_REASONING_LAB_INDEX.md",
    "labs/LAB_QUALITY_STANDARD.md",
    "labs/STUDENT_LAB_JOURNAL_GUIDE.md",
    "labs/READING_TO_LAB_TRANSFER_CHECKLIST.md",
    "assessments/40-hour-daily-checkpoints.md",
    "assessments/40-hour-checkpoint-rubric.md",
    "assessments/lab-deliverable-quality-checklist.md",
    "instructor/40-hour-student-experience-runbook.md",
    "instructor/lab-troubleshooting-and-reset-guide.md",
    "PUBLISHED_COURSE_VIEW.md",
]

LAB_TARGETS = [
    "labs/brokenpilot/prototype-app/app/main.py",
    "labs/brokenpilot/prototype-app/tests/test_basic.py",
    "labs/brokenpilot/prototype-app/LAB_GUIDE.md",
    "labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md",
    "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md",
    "labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md",
    "labs/toy-ml-attacks/toy-classifier-app/train.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/poisoning.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/extraction.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/output_integrity.py",
    "labs/toy-ml-attacks/toy-classifier-app/tests/test_toy_classifier.py",
    "labs/mlops-supply-chain-labs/evidence-pack-review/README.md",
    "labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md",
]

MODEL_ANSWERS_AND_ANCHORS = [
    "labs/brokenpilot/worked-examples/current-complete-final-report.md",
    "labs/brokenpilot/worked-examples/current-final-report-evidence-map.md",
    "labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md",
    "labs/mlops-supply-chain-labs/worked-examples/mlops-evidence-pack-evidence-map.md",
    "labs/toy-ml-attacks/toy-classifier-app/worked-examples/strong-toy-classifier-lab-report.md",
    "labs/toy-ml-attacks/toy-classifier-app/worked-examples/weak-toy-classifier-lab-report.md",
]

OPTIONAL_BUILDOUT_DOCS = [
    "COURSE_COMPLETION_SCORECARD.md",
    "COURSE_CONTENT_AUDIT.md",
    "COURSE_FLOW_REVIEW.md",
    "labs/LAB_COVERAGE_AND_MATURITY_MATRIX.md",
    "assessments/END_TO_END_ASSESSMENT_MAP.md",
    "instructor/teaching-the-course-as-one-journey.md",
]


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def main() -> None:
    missing: list[str] = []
    warnings: list[str] = []

    for rel in CORE_FILES:
        if not exists(rel):
            missing.append(rel)

    for module in MODULES:
        base = Path("modules") / module

        if module == "12-capstone-brokenpilot":
            required = CAPSTONE_FILES
        else:
            required = NORMAL_MODULE_FILES

        for filename in required:
            rel = str(base / filename).replace("\\", "/")
            if not exists(rel):
                missing.append(rel)

    for rel in LAB_TARGETS:
        if not exists(rel):
            missing.append(rel)

    for rel in MODEL_ANSWERS_AND_ANCHORS:
        if not exists(rel):
            warnings.append(f"optional but recommended anchor missing: {rel}")

    for rel in OPTIONAL_BUILDOUT_DOCS:
        if not exists(rel):
            warnings.append(f"buildout/audit doc not present in student path: {rel}")

    if missing:
        print("Content readiness check failed:")
        for item in missing:
            print(f"- missing: {item}")
        raise SystemExit(1)

    print("Content readiness check passed.")

    if warnings:
        print("\nNon-blocking notes:")
        for item in warnings:
            print(f"- {item}")


if __name__ == "__main__":
    main()
