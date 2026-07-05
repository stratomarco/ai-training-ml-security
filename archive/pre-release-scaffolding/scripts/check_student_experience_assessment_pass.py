from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "labs/STUDENT_LAB_JOURNAL_GUIDE.md",
    "course-templates/student-lab-journal-template.md",
    "course-templates/daily-checkpoint-submission-template.md",
    "assessments/40-hour-daily-checkpoints.md",
    "assessments/40-hour-checkpoint-rubric.md",
    "assessments/lab-deliverable-quality-checklist.md",
    "assessments/anchor-based-grading-guide.md",
    "instructor/40-hour-student-experience-runbook.md",
    "instructor/lab-troubleshooting-and-reset-guide.md",
    "labs/brokenpilot/CAPSTONE_CHECKPOINTS.md",
    "modules/12-capstone-brokenpilot/capstone-checkpoints.md",
    "docs/start-here/40-hour-student-workbook.md",
]

KEYWORDS = {
    "labs/STUDENT_LAB_JOURNAL_GUIDE.md": ["observable failure", "residual risk", "reasoning labs"],
    "course-templates/student-lab-journal-template.md": ["Root cause", "Validation", "Residual risk"],
    "assessments/40-hour-daily-checkpoints.md": ["Day 1", "Day 5", "Capstone report"],
    "assessments/40-hour-checkpoint-rubric.md": ["Evidence", "Root cause", "Residual risk"],
    "instructor/40-hour-student-experience-runbook.md": ["prompt-hacking tournament", "enforcement point", "checkpoint"],
    "instructor/lab-troubleshooting-and-reset-guide.md": ["BrokenPilot", "Toy classifier", "MLOps evidence pack"],
    "labs/brokenpilot/CAPSTONE_CHECKPOINTS.md": ["Checkpoint 1", "Checkpoint 4", "leadership recommendation"],
    "modules/12-capstone-brokenpilot/capstone-checkpoints.md": ["Scope and system model", "Reproducible evidence", "Remediation backlog"],
}


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit("Missing required files:\n" + "\n".join(missing))

    failures: list[str] = []
    for relpath, terms in KEYWORDS.items():
        text = (ROOT / relpath).read_text(encoding="utf-8").lower()
        for term in terms:
            if term.lower() not in text:
                failures.append(f"{relpath} missing {term!r}")

    if failures:
        raise SystemExit("Student experience checks failed:\n" + "\n".join(failures))

    print("Student experience and assessment checks passed.")


if __name__ == "__main__":
    main()
