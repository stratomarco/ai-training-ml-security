from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

COURSE_QUALITY = ROOT / ".github" / "workflows" / "course-quality.yml"
DEPLOY_DOCS = ROOT / ".github" / "workflows" / "deploy-docs.yml"
VALIDATION_BASELINE = ROOT / "instructor" / "release-readiness" / "release-process-docs" / "VALIDATION_BASELINE.md"

SCRIPT_REF = re.compile(r"(?:python|python3|\$\{?\{?\s*env\.pythonLocation\s*\}?\}?/bin/python)?\s*(scripts/[A-Za-z0-9_./-]+\.py)")


def require_file(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def require_contains(text: str, needle: str, label: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"{label} missing required text: {needle}")


def check_script_refs(text: str, label: str, errors: list[str]) -> None:
    for match in re.finditer(r"scripts/[A-Za-z0-9_./-]+\.py", text):
        rel = match.group(0)
        if not (ROOT / rel).exists():
            errors.append(f"{label} references missing script: {rel}")


def main() -> None:
    errors: list[str] = []

    course_quality = require_file(COURSE_QUALITY, errors)
    deploy_docs = require_file(DEPLOY_DOCS, errors)
    validation_baseline = require_file(VALIDATION_BASELINE, errors)

    if course_quality:
        for required in [
            "python scripts/check_repo_structure.py",
            "python scripts/check_content_readiness.py",
            "python scripts/check_lab_targets.py",
            "python scripts/check_workflow_validation_baseline.py",
            "python scripts/check_root_process_docs.py",
            "python scripts/sync_mkdocs_content.py",
            "python scripts/generate_mkdocs_nav.py",
            "mkdocs build --strict",
            "labs/brokenpilot/prototype-app",
            "labs/toy-ml-attacks/toy-classifier-app",
            "pytest",
        ]:
            require_contains(course_quality, required, "course-quality.yml", errors)
        if "check_release_cleanup_phase7_mkdocs_strict.py" in course_quality:
            errors.append("course-quality.yml still references archived phase-7 checker")
        check_script_refs(course_quality, "course-quality.yml", errors)

    if deploy_docs:
        for required in [
            "workflow_dispatch",
            "python scripts/sync_mkdocs_content.py",
            "python scripts/generate_mkdocs_nav.py",
            "mkdocs build --strict",
            "mkdocs gh-deploy --force",
        ]:
            require_contains(deploy_docs, required, "deploy-docs.yml", errors)
        if "gh-deploy --force --strict" in deploy_docs:
            errors.append("deploy-docs.yml passes invalid --strict flag to gh-deploy")
        if "check_release_cleanup_phase7_mkdocs_strict.py" in deploy_docs:
            errors.append("deploy-docs.yml still references archived phase-7 checker")
        check_script_refs(deploy_docs, "deploy-docs.yml", errors)

    if validation_baseline:
        require_contains(validation_baseline, "MkDocs", "VALIDATION_BASELINE.md", errors)

    if errors:
        print("workflow readiness check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("workflow readiness check passed.")


if __name__ == "__main__":
    main()
