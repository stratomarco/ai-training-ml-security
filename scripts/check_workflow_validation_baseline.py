
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"missing required workflow file: {rel}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        raise SystemExit(f"workflow readiness check failed: {where} missing {needle!r}")


def forbid(text: str, needle: str, where: str) -> None:
    if needle in text:
        raise SystemExit(f"workflow readiness check failed: {where} still contains {needle!r}")


def main() -> None:
    cq = read(".github/workflows/course-quality.yml")
    deploy = read(".github/workflows/deploy-docs.yml")

    require(cq, "check_repo_structure.py", "course-quality.yml")
    require(cq, "check_content_readiness.py", "course-quality.yml")
    require(cq, "check_lab_targets.py", "course-quality.yml")
    require(cq, "labs/brokenpilot/prototype-app", "course-quality.yml")
    require(cq, "labs/toy-ml-attacks/toy-classifier-app", "course-quality.yml")
    require(cq, "pytest", "course-quality.yml")
    require(cq, "mkdocs build", "course-quality.yml")
    forbid(cq, "mkdocs build --strict", "course-quality.yml")

    require(deploy, "workflow_dispatch", "deploy-docs.yml")
    require(deploy, "mkdocs build", "deploy-docs.yml")
    forbid(deploy, "mkdocs build --strict", "deploy-docs.yml")

    baseline = ROOT / "VALIDATION_BASELINE.md"
    if not baseline.exists():
        raise SystemExit("workflow readiness check failed: VALIDATION_BASELINE.md missing")

    print("Workflow and validation cleanup checks passed.")


if __name__ == "__main__":
    main()
