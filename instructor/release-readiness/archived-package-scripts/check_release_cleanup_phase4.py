from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ARCHIVE = ROOT / "instructor" / "release-readiness" / "archived-package-scaffolding"

REQUIRED = [
    "STYLE_AND_VOICE_FINAL_PASS.md",
    "GENERATED_SCAFFOLDING_CLEANUP_REPORT.md",
    "instructor/release-readiness/student-facing-cleanup-checklist.md",
    "scripts/check_student_facing_scaffolding.py",
    "VALIDATION_BASELINE.md",
]

DURABLE = [
    "scripts/sync_mkdocs_content.py",
    "scripts/check_repo_structure.py",
    "scripts/check_content_readiness.py",
    "scripts/check_lab_targets.py",
]

ALLOWED_ACTIVE_PREFIXES = (
    "check_",
    "sync_",
    "apply_release_cleanup_phase4.py",
)

FORBIDDEN_ACTIVE_PREFIXES = (
    "repair_",
    "fix_",
    "add_",
)


def exists(rel: str) -> bool:
    return (ROOT / rel).exists()


def main() -> None:
    missing: list[str] = []
    problems: list[str] = []

    for rel in REQUIRED + DURABLE:
        if not exists(rel):
            missing.append(rel)

    if (ROOT / "README_PACKAGE.md").exists():
        problems.append("root README_PACKAGE.md should be archived, not student-facing")

    if SCRIPTS.exists():
        for path in SCRIPTS.glob("*.py"):
            name = path.name
            if name.startswith(FORBIDDEN_ACTIVE_PREFIXES):
                problems.append(f"temporary helper still active: scripts/{name}")
            if name.startswith("apply_") and name != "apply_release_cleanup_phase4.py":
                problems.append(f"old apply script still active: scripts/{name}")

    if not ARCHIVE.exists():
        problems.append("archive directory missing")

    if missing or problems:
        print("Release cleanup phase 4 check failed:")
        for item in missing:
            print(f"- missing: {item}")
        for item in problems:
            print(f"- {item}")
        raise SystemExit(1)

    print("Release cleanup phase 4 checks passed.")


if __name__ == "__main__":
    main()
