
from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "labs/brokenpilot/prototype-app/app/main.py",
    "labs/brokenpilot/prototype-app/app/mock_llm.py",
    "labs/brokenpilot/prototype-app/app/controls.py",
    "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md",
    "labs/brokenpilot/prototype-app/DIRECT_PROMPT_INJECTION_LAB.md",
    "labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md",
    "labs/toy-ml-attacks/toy-classifier-app/train.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/poisoning.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/extraction.py",
    "labs/toy-ml-attacks/toy-classifier-app/attacks/output_integrity.py",
    "labs/mlops-supply-chain-labs/evidence-pack-review/README.md",
    "labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md",
]
TEXT_EXPECTATIONS = {
    "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py": ["run_evasion", "malicious", "phish", "safe"],
    "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md": ["POST /render", "ENABLE_OUTPUT_ENCODING=false", "ENABLE_OUTPUT_ENCODING=true"],
    "labs/RUNNABLE_AND_REASONING_LAB_INDEX.md": ["BrokenPilot", "toy-classifier", "MLOps"],
}
def main() -> None:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing: {rel}")
    for rel, needles in TEXT_EXPECTATIONS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing text target: {rel}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel} missing expected text: {needle}")
    if errors:
        print("Lab target check failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Lab target check passed.")
if __name__ == "__main__":
    main()
