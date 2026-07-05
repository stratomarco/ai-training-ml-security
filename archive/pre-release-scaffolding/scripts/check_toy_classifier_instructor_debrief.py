from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "instructor/toy-classifier-facilitation-guide.md",
    "instructor/toy-classifier-debrief-guide.md",
    "labs/toy-ml-attacks/toy-classifier-app/INSTRUCTOR_NOTES.md",
    "labs/toy-ml-attacks/toy-classifier-app/DEBRIEF_GUIDE.md",
    "labs/toy-ml-attacks/toy-classifier-app/worked-examples/strong-toy-classifier-lab-report.md",
    "labs/toy-ml-attacks/toy-classifier-app/worked-examples/weak-toy-classifier-lab-report.md",
    "assessments/toy-classifier-lab-rubric.md",
    "course-templates/toy-classifier-lab-report-template.md",
    "modules/03-owasp-ml-top-10/toy-classifier-debrief.md",
    "modules/10-adversarial-ml-robustness/toy-classifier-debrief.md",
    ".github/workflows/course-quality.yml",
    ".github/workflows/deploy-docs.yml",
]

REQUIRED_PHRASES = {
    "instructor/toy-classifier-facilitation-guide.md": [
        "observable",
        "Naive fixes",
        "Defense-in-depth moment",
        "Graded artifact",
        "hard decision gate",
        "residual risk",
        "evasion.py",
        "poisoning.py",
        "extraction.py",
        "output_integrity.py",
    ],
    "instructor/toy-classifier-debrief-guide.md": [
        "engineering decisions",
        "Evasion",
        "Poisoning",
        "Extraction",
        "Output integrity",
        "hard enforcement",
    ],
    "assessments/toy-classifier-lab-rubric.md": [
        "Evidence",
        "Authority",
        "Root cause",
        "Validation",
        "Residual risk",
        "Decision",
    ],
    "labs/toy-ml-attacks/toy-classifier-app/worked-examples/strong-toy-classifier-lab-report.md": [
        "I would not allow this classifier to operate as a hard enforcement gate",
        "Recommended controls",
        "Validation",
        "Residual risk",
    ],
    "labs/toy-ml-attacks/toy-classifier-app/worked-examples/weak-toy-classifier-lab-report.md": [
        "Why this is weak",
        "guardrails",
    ],
    ".github/workflows/course-quality.yml": [
        "brokenpilot-tests",
        "toy-classifier-tests",
        "pytest",
    ],
    ".github/workflows/deploy-docs.yml": [
        "workflow_dispatch",
        "mkdocs build",
    ],
}

FORBIDDEN = [
    "TODO",
    "TBD",
    "lorem ipsum",
    "placeholder",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if len(text.strip()) < 400:
            errors.append(f"file too thin: {rel}")
        for forbidden in FORBIDDEN:
            if forbidden.lower() in text.lower():
                errors.append(f"forbidden placeholder phrase {forbidden!r} in {rel}")

    for rel, phrases in REQUIRED_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"missing phrase {phrase!r} in {rel}")

    workflow = ROOT / ".github/workflows/course-quality.yml"
    if workflow.exists():
        text = workflow.read_text(encoding="utf-8")
        if "mkdocs build --strict" in text or "mkdocs build" in text:
            errors.append("course-quality workflow should not run MkDocs during content buildout")

    deploy = ROOT / ".github/workflows/deploy-docs.yml"
    if deploy.exists():
        text = deploy.read_text(encoding="utf-8")
        if "mkdocs build --strict" in text:
            errors.append("deploy workflow should not use strict MkDocs during content buildout")
        if "workflow_dispatch" not in text:
            errors.append("deploy workflow should be manual during content buildout")

    if errors:
        print("Toy-classifier instructor/debrief checks failed:")
        for err in errors:
            print(f"- {err}")
        raise SystemExit(1)

    print("Toy-classifier instructor/debrief checks passed.")


if __name__ == "__main__":
    main()
