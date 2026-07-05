from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ARCHIVE = ROOT / "archive" / "pre-release-scaffolding"

def main() -> None:
    errors: list[str] = []
    for rel in [
        "RELEASE_CLEANUP_PHASE1_REPORT.md",
        "CLEANUP_BEFORE_RELEASE.md",
        "scripts/check_content_readiness.py",
        "scripts/check_lab_targets.py",
        "release-notes/v1.1-dev-release-cleanup-phase1.md",
    ]:
        if not (ROOT / rel).exists():
            errors.append(f"missing: {rel}")
    if not ARCHIVE.exists():
        errors.append("missing archive/pre-release-scaffolding")
    if SCRIPTS.exists():
        for path in SCRIPTS.glob("*.py"):
            name = path.name
            if name.startswith("apply_") and name != "apply_release_cleanup_phase1.py":
                errors.append(f"temporary apply script still active: scripts/{name}")
            if name.startswith("repair_"):
                errors.append(f"temporary repair script still active: scripts/{name}")
            if name.startswith("add_"):
                errors.append(f"temporary nav/helper script still active: scripts/{name}")
            if name.startswith("fix_"):
                errors.append(f"temporary fix script still active: scripts/{name}")
    report = ROOT / "RELEASE_CLEANUP_PHASE1_REPORT.md"
    if report.exists():
        text = report.read_text(encoding="utf-8", errors="replace")
        for phrase in ["What this pass intentionally did not do", "MkDocs strict navigation", "Archived scripts"]:
            if phrase not in text:
                errors.append(f"cleanup report missing phrase: {phrase}")
    if errors:
        print("Release cleanup phase 1 check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Release cleanup phase 1 check passed.")
if __name__ == "__main__":
    main()
