from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "labs" / "toy-ml-attacks" / "toy-classifier-app"

REQUIRED = [
    APP / "README.md",
    APP / "requirements.txt",
    APP / "requirements-dev.txt",
    APP / "train.py",
    APP / "data" / "messages.json",
    APP / "toy_classifier" / "__init__.py",
    APP / "toy_classifier" / "model.py",
    APP / "attacks" / "__init__.py",
    APP / "attacks" / "evasion.py",
    APP / "attacks" / "poisoning.py",
    APP / "attacks" / "extraction.py",
    APP / "attacks" / "output_integrity.py",
    APP / "tests" / "test_toy_classifier.py",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    missing = [path for path in REQUIRED if not path.exists()]
    if missing:
        for path in missing:
            print(f"missing: {path.relative_to(ROOT)}")
        fail("toy-classifier required files are missing")

    data = json.loads((APP / "data" / "messages.json").read_text(encoding="utf-8"))
    labels = {row.get("label") for row in data}
    if labels != {"safe", "phish"}:
        fail(f"dataset labels must be safe/phish, got {sorted(labels)}")
    if len(data) < 40:
        fail("dataset should contain at least 40 synthetic examples")

    for script in ["evasion.py", "poisoning.py", "extraction.py", "output_integrity.py"]:
        result = subprocess.run(
            [sys.executable, str(APP / "attacks" / script)],
            cwd=APP,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            fail(f"attack script failed: {script}")
        if "Observation:" not in result.stdout:
            fail(f"attack script does not print an observation: {script}")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=APP,
        text=True,
        capture_output=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        fail("toy-classifier pytest failed")

    print("Toy-classifier lab checks passed.")


if __name__ == "__main__":
    main()
