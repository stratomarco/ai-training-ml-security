from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], cwd: Path | None = None) -> None:
    where = cwd or ROOT
    print(f"\n==> {' '.join(command)}")
    result = subprocess.run(command, cwd=where)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> None:
    py = sys.executable

    checks = [
        [py, "scripts/check_repo_structure.py"],
        [py, "scripts/check_content_readiness.py"],
        [py, "scripts/check_lab_targets.py"],
        [py, "scripts/check_workflow_validation_baseline.py"],
        [py, "scripts/check_release_candidate_phase8.py"],
        [py, "scripts/check_instructor_track.py"],
        [py, "scripts/check_final_release_artifacts.py"],
    ]

    scaffolding_check = ROOT / "scripts" / "check_student_facing_scaffolding.py"
    if scaffolding_check.exists():
        checks.append([py, "scripts/check_student_facing_scaffolding.py"])

    for command in checks:
        run(command)

    run(["mkdocs", "build", "--strict"])

    run([py, "-m", "pytest"], cwd=ROOT / "labs" / "brokenpilot" / "prototype-app")
    run([py, "-m", "pytest"], cwd=ROOT / "labs" / "toy-ml-attacks" / "toy-classifier-app")

    print("\nFinal release gate passed.")


if __name__ == "__main__":
    main()
