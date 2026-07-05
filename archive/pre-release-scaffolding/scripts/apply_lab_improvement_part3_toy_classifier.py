from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "labs" / "toy-ml-attacks" / "toy-classifier-app"

REQUIRED_APP_FILES = [
    APP / "README.md",
    APP / "requirements.txt",
    APP / "requirements-dev.txt",
    APP / "train.py",
    APP / "data" / "messages.json",
    APP / "toy_classifier" / "model.py",
    APP / "attacks" / "evasion.py",
    APP / "attacks" / "poisoning.py",
    APP / "attacks" / "extraction.py",
    APP / "attacks" / "output_integrity.py",
    APP / "tests" / "test_toy_classifier.py",
]


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def append_once(path: Path, marker: str, section: str) -> None:
    text = read(path)
    if marker in text:
        print(f"already updated: {path.relative_to(ROOT)}")
        return
    if text and not text.endswith("\n"):
        text += "\n"
    text += "\n" + section.strip() + "\n"
    write(path, text)
    print(f"updated: {path.relative_to(ROOT)}")


def replace_aspirational_text(path: Path) -> None:
    text = read(path)
    if not text:
        return
    replacements = {
        "Suggested toy-code extension": "Runnable toy-classifier extension",
        "Students receive a small fake dataset and a set of example messages.": "Students use the shipped synthetic dataset at `labs/toy-ml-attacks/toy-classifier-app/data/messages.json`.",
        "small fake dataset": "shipped synthetic dataset",
    }
    updated = text
    for old, new in replacements.items():
        updated = updated.replace(old, new)
    if updated != text:
        write(path, updated)
        print(f"normalized wording: {path.relative_to(ROOT)}")


def main() -> None:
    missing = [p for p in REQUIRED_APP_FILES if not p.exists()]
    if missing:
        print("Missing toy-classifier files. Unzip/copy the package into the repo first.")
        for path in missing:
            print(f"missing: {path.relative_to(ROOT)}")
        raise SystemExit(1)

    toy_readme = ROOT / "labs" / "toy-ml-attacks" / "README.md"
    append_once(
        toy_readme,
        "<!-- toy-classifier-app-link -->",
        """
<!-- toy-classifier-app-link -->

## Runnable toy-classifier app

The observable path for Modules 03 and 10 is now the shipped toy-classifier app:

```text
labs/toy-ml-attacks/toy-classifier-app/
```

Use it for evasion, poisoning, extraction, and output-integrity exercises. The dataset is synthetic, deterministic, local, and covered by pytest.
""",
    )

    classical_lab = ROOT / "labs" / "toy-ml-attacks" / "classical-ml-attack-lab.md"
    replace_aspirational_text(classical_lab)
    append_once(
        classical_lab,
        "<!-- toy-classifier-runnable-path -->",
        """
<!-- toy-classifier-runnable-path -->

## Runnable path: toy-classifier app

Use the shipped app instead of inventing a dataset:

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
python -m pip install -r requirements-dev.txt
python train.py
python attacks/evasion.py
python attacks/poisoning.py
python attacks/extraction.py
python attacks/output_integrity.py
pytest
```

macOS/Linux uses the same commands with `/` path separators.

Student deliverable: for each script, record the before/after output, identify the changed security property, propose one implementable control, and state residual risk.
""",
    )

    evasion_lab = ROOT / "labs" / "adversarial-ml-labs" / "evasion-robustness-lab.md"
    replace_aspirational_text(evasion_lab)
    append_once(
        evasion_lab,
        "<!-- toy-classifier-evasion-path -->",
        """
<!-- toy-classifier-evasion-path -->

## Runnable evasion path

Use the shipped synthetic dataset and evasion script:

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
python -m pip install -r requirements-dev.txt
python attacks/evasion.py
pytest
```

The core engineering question is whether the classifier should be allowed to act as a hard authorization or safety gate. A robust answer should discuss confidence, fallback, review queues, monitoring, and residual risk.
""",
    )

    module03 = ROOT / "modules" / "03-owasp-ml-top-10" / "README.md"
    append_once(
        module03,
        "<!-- module03-toy-classifier -->",
        """
<!-- module03-toy-classifier -->

## Runnable lab anchor

The classical ML attack categories in this module are supported by `labs/toy-ml-attacks/toy-classifier-app/`. Use it to demonstrate input manipulation, data poisoning, model extraction by queries, and output-integrity failure with deterministic tests.
""",
    )

    module10 = ROOT / "modules" / "10-adversarial-ml-robustness" / "README.md"
    append_once(
        module10,
        "<!-- module10-toy-classifier -->",
        """
<!-- module10-toy-classifier -->

## Runnable lab anchor

Use `labs/toy-ml-attacks/toy-classifier-app/` for the observable evasion and poisoning portions of this module. Keep the backdoor and drift exercises as reasoning/tabletop activities unless a separate deterministic target is added later.
""",
    )

    changelog = ROOT / "CHANGELOG.md"
    append_once(
        changelog,
        "<!-- v1.1-dev-lab-improvement-part3-toy-classifier -->",
        """
<!-- v1.1-dev-lab-improvement-part3-toy-classifier -->

## v1.1-dev: Toy-classifier observable ML attack lab

- Added a deterministic toy-classifier app for Modules 03 and 10.
- Added runnable evasion, poisoning, extraction, and output-integrity scripts.
- Added pytest coverage for all four attack demonstrations.
- Updated the toy ML and adversarial evasion labs to point to shipped data and scripts.
""",
    )

    print("\nApplied lab improvement Part 3 toy-classifier package.")


if __name__ == "__main__":
    main()
