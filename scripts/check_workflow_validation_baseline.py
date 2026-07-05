from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COURSE_QUALITY = ROOT / ".github" / "workflows" / "course-quality.yml"
DEPLOY_DOCS = ROOT / ".github" / "workflows" / "deploy-docs.yml"
VALIDATION_BASELINE = ROOT / "VALIDATION_BASELINE.md"


def require_file(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def require_contains(text: str, needle: str, label: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"{label} missing required text: {needle}")


def main() -> None:
    errors: list[str] = []

    course_quality = require_file(COURSE_QUALITY, errors)
    deploy_docs = require_file(DEPLOY_DOCS, errors)
    validation_baseline = require_file(VALIDATION_BASELINE, errors)

    if course_quality:
        require_contains(
            course_quality,
            "python scripts/check_repo_structure.py",
            "course-quality.yml",
            errors,
        )
        require_contains(
            course_quality,
            "python scripts/check_content_readiness.py",
            "course-quality.yml",
            errors,
        )
        require_contains(
            course_quality,
            "python scripts/check_lab_targets.py",
            "course-quality.yml",
            errors,
        )
        require_contains(
            course_quality,
            "mkdocs build --strict",
            "course-quality.yml",
            errors,
        )
        require_contains(
            course_quality,
            "labs/brokenpilot/prototype-app",
            "course-quality.yml",
            errors,
        )
        require_contains(
            course_quality,
            "labs/toy-ml-attacks/toy-classifier-app",
            "course-quality.yml",
            errors,
        )
        require_contains(
            course_quality,
            "pytest",
            "course-quality.yml",
            errors,
        )

    if deploy_docs:
        require_contains(
            deploy_docs,
            "workflow_dispatch",
            "deploy-docs.yml",
            errors,
        )
        require_contains(
            deploy_docs,
            "--strict",
            "deploy-docs.yml",
            errors,
        )

    if validation_baseline:
        require_contains(
            validation_baseline,
            "MkDocs",
            "VALIDATION_BASELINE.md",
            errors,
        )

    if errors:
        print("workflow readiness check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("workflow readiness check passed.")


if __name__ == "__main__":
    main()
