from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ".github/workflows/course-quality.yml",
    ".github/workflows/deploy-docs.yml",
    "VALIDATION_BASELINE.md",
    "scripts/check_workflow_validation_baseline.py",
    "release-notes/v1.1-dev-release-cleanup-phase3.md",
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"Release cleanup phase 3 check failed: missing {rel}")
    return path.read_text(encoding="utf-8")


def require(rel: str, needle: str) -> None:
    text = read(rel)
    if needle not in text:
        raise SystemExit(f"Release cleanup phase 3 check failed: {rel} missing {needle!r}")


def forbid(rel: str, needle: str) -> None:
    text = read(rel)
    if needle in text:
        raise SystemExit(f"Release cleanup phase 3 check failed: {rel} still contains {needle!r}")


def main() -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            raise SystemExit(f"Release cleanup phase 3 check failed: missing {rel}")

    require(".github/workflows/course-quality.yml", "check_content_readiness.py")
    require(".github/workflows/course-quality.yml", "check_lab_targets.py")
    require(".github/workflows/course-quality.yml", "labs/brokenpilot/prototype-app")
    require(".github/workflows/course-quality.yml", "labs/toy-ml-attacks/toy-classifier-app")
    require(".github/workflows/course-quality.yml", "pytest")
    forbid(".github/workflows/course-quality.yml", "mkdocs build --strict")

    require(".github/workflows/deploy-docs.yml", "workflow_dispatch")
    require(".github/workflows/deploy-docs.yml", "mkdocs build")
    forbid(".github/workflows/deploy-docs.yml", "mkdocs build --strict")

    require("VALIDATION_BASELINE.md", "Active gates")
    require("VALIDATION_BASELINE.md", "Postponed gates")
    require("CLEANUP_BEFORE_RELEASE.md", "Release cleanup phase 3 status")

    print("Release cleanup phase 3 checks passed.")


if __name__ == "__main__":
    main()
