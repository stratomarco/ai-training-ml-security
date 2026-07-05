from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md",
    "labs/mlops-supply-chain-labs/worked-examples/mlops-evidence-pack-evidence-map.md",
    "labs/mlops-supply-chain-labs/worked-examples/mlops-evidence-pack-executive-readout.md",
    "labs/mlops-supply-chain-labs/worked-examples/mlops-evidence-pack-remediation-plan.md",
    "instructor/mlops-evidence-pack-model-answer-debrief.md",
    "assessments/mlops-evidence-pack-model-answer-rubric.md",
    "modules/08-secure-mlops-supply-chain/mlops-evidence-pack-model-answer.md",
]

MODEL_ANSWER_REQUIRED = [
    "Executive summary",
    "Finding 1",
    "artifact digest",
    "dependency",
    "dataset",
    "approval",
    "storage",
    "notebook",
    "Validation",
    "Residual risk",
    "Leadership recommendation",
]

EVIDENCE_REQUIRED = [
    "requirements.txt",
    "train.ipynb",
    "registry/model_registry.json",
    "metadata/training-run.json",
    "storage/bucket-policy.json",
    "ci/promotion-workflow.yml",
    "artifacts/model.pkl.README.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: str) -> str:
    full = ROOT / path
    if not full.exists():
        fail(f"missing required file: {path}")
    return full.read_text(encoding="utf-8")


def main() -> None:
    for path in REQUIRED_FILES:
        read(path)

    model = read("labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md")
    if len(model.split()) < 1200:
        fail("model answer is too short to be a complete reference answer")
    for token in MODEL_ANSWER_REQUIRED:
        if token not in model:
            fail(f"model answer missing token: {token}")

    evidence = read("labs/mlops-supply-chain-labs/worked-examples/mlops-evidence-pack-evidence-map.md")
    for token in EVIDENCE_REQUIRED:
        if token not in evidence:
            fail(f"evidence map missing source: {token}")

    debrief = read("instructor/mlops-evidence-pack-model-answer-debrief.md")
    for token in ["Naive fixes", "Defense-in-depth", "Grading anchors", "Closing message"]:
        if token not in debrief:
            fail(f"debrief missing section: {token}")

    rubric = read("assessments/mlops-evidence-pack-model-answer-rubric.md")
    for token in ["Evidence use", "Root cause", "Remediation quality", "Validation", "Leadership recommendation"]:
        if token not in rubric:
            fail(f"rubric missing section: {token}")

    module_page = read("modules/08-secure-mlops-supply-chain/mlops-evidence-pack-model-answer.md")
    for token in ["Student-facing path", "Model answer resources", "Core lesson"]:
        if token not in module_page:
            fail(f"module page missing section: {token}")

    print("MLOps evidence-pack model answer checks passed.")


if __name__ == "__main__":
    main()
