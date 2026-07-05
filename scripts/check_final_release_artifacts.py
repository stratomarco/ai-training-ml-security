from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
RELEASE_PROCESS = "instructor/release-readiness/release-process-docs"

REQUIRED_FILES = [
    "VERSION",
    "COURSE_RELEASE_MANIFEST.md",
    "PUBLISHED_COURSE_VIEW.md",
    "RELEASE_TAGGING_GUIDE.md",
    "USAGE_AND_LICENSING_GUIDE.md",
    f"{RELEASE_PROCESS}/RELEASE_CANDIDATE_CHECKLIST.md",
    f"{RELEASE_PROCESS}/FINAL_RELEASE_REVIEW.md",
    f"{RELEASE_PROCESS}/QUALITY_GATE_BASELINE.md",
    f"{RELEASE_PROCESS}/VALIDATION_BASELINE.md",
    "instructor/README.md",
    "instructor/toy-classifier-guide.md",
    "instructor/brokenpilot-guide.md",
    "instructor/mlops-evidence-pack-guide.md",
    "scripts/run_final_release_gate.py",
    "scripts/check_instructor_track.py",
    "scripts/check_final_release_artifacts.py",
    "scripts/check_root_process_docs.py",
]

REQUIRED_ACTIVE_SCRIPTS = [
    "check_repo_structure.py",
    "check_content_readiness.py",
    "check_lab_targets.py",
    "check_workflow_validation_baseline.py",
    "check_release_candidate_phase8.py",
    "check_instructor_track.py",
    "check_final_release_artifacts.py",
    "check_root_process_docs.py",
    "run_final_release_gate.py",
    "sync_mkdocs_content.py",
    "generate_mkdocs_nav.py",
]

FORBIDDEN_SCRIPT_PREFIXES = (
    "apply_",
    "repair_",
    "add_",
    "fix_",
)

FORBIDDEN_SCRIPT_NAMES = {
    "check_rc_instructor_track_fixes.py",
    "check_pre_rc_review_package.py",
    "run_pre_rc_review.py",
    "apply_pre_rc_review.py",
    "prepare_final_release_artifacts.py",
}

REQUIRED_README_LINKS = [
    "COURSE_RELEASE_MANIFEST.md",
    "USAGE_AND_LICENSING_GUIDE.md",
    "RELEASE_TAGGING_GUIDE.md",
]

REQUIRED_INSTRUCTOR_LINKS = [
    "toy-classifier-guide.md",
    "brokenpilot-guide.md",
    "mlops-evidence-pack-guide.md",
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")

    if not SCRIPTS.exists():
        errors.append("missing scripts directory")
    else:
        for name in REQUIRED_ACTIVE_SCRIPTS:
            if not (SCRIPTS / name).exists():
                errors.append(f"missing active validation script: scripts/{name}")

        for path in sorted(SCRIPTS.glob("*.py")):
            name = path.name
            forbidden = (
                name.startswith(FORBIDDEN_SCRIPT_PREFIXES)
                or name.startswith("check_release_cleanup_phase")
                or name in FORBIDDEN_SCRIPT_NAMES
            )
            if forbidden:
                errors.append(f"package-era helper still active: scripts/{name}")

    if (ROOT / "README_PACKAGE.md").exists():
        errors.append("root README_PACKAGE.md should be archived before release tagging")

    readme = read("README.md")
    for link in REQUIRED_README_LINKS:
        if link not in readme:
            warnings.append(f"README.md does not mention {link}")
    if "QUALITY_GATE_BASELINE.md](QUALITY_GATE_BASELINE.md)" in readme:
        errors.append("README.md still links to root QUALITY_GATE_BASELINE.md")
    if "COURSE_VOICE_AND_COHESION_REVIEW.md" in readme:
        errors.append("README.md still links to archived COURSE_VOICE_AND_COHESION_REVIEW.md")

    instructor_readme = read("instructor/README.md")
    for link in REQUIRED_INSTRUCTOR_LINKS:
        if link not in instructor_readme:
            errors.append(f"instructor/README.md missing {link}")

    usage = read("USAGE_AND_LICENSING_GUIDE.md").lower()
    if usage:
        if "commercial" not in usage:
            errors.append("USAGE_AND_LICENSING_GUIDE.md does not mention commercial use")
        if "attribution" not in usage:
            errors.append("USAGE_AND_LICENSING_GUIDE.md does not mention attribution")

    version = read("VERSION").strip()
    if version and not version.startswith("v1.1"):
        warnings.append(f"VERSION is not v1.1-prefixed: {version}")

    if (ROOT / "scripts" / "check_root_process_docs.py").exists():
        import subprocess
        import sys
        result = subprocess.run([sys.executable, "scripts/check_root_process_docs.py"], cwd=ROOT)
        if result.returncode != 0:
            errors.append("scripts/check_root_process_docs.py failed")

    if errors:
        print("final release artifact check failed:")
        for error in errors:
            print(f"- {error}")
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"- {warning}")
        raise SystemExit(1)

    print("final release artifact check passed.")
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")


if __name__ == "__main__":
    main()
