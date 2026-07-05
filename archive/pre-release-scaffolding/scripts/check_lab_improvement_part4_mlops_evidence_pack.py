from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "labs/mlops-supply-chain-labs/evidence-pack-review/README.md",
    "labs/mlops-supply-chain-labs/evidence-pack-review/requirements.txt",
    "labs/mlops-supply-chain-labs/evidence-pack-review/train.ipynb",
    "labs/mlops-supply-chain-labs/evidence-pack-review/registry/model_registry.json",
    "labs/mlops-supply-chain-labs/evidence-pack-review/metadata/training-run.json",
    "labs/mlops-supply-chain-labs/evidence-pack-review/storage/bucket-policy.json",
    "labs/mlops-supply-chain-labs/evidence-pack-review/ci/promotion-workflow.yml",
    "labs/mlops-supply-chain-labs/evidence-pack-review/artifacts/model.pkl.README.md",
    "labs/mlops-supply-chain-labs/evidence-pack-review/artifacts/model-sha256.txt",
    "labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md",
    "modules/08-secure-mlops-supply-chain/mlops-evidence-pack-review.md",
    "course-templates/mlops-evidence-pack-review-template.md",
    "assessments/mlops-evidence-pack-review-rubric.md",
    "labs/mlops-supply-chain-labs/worked-examples/strong-mlops-supply-chain-review.md",
    "labs/mlops-supply-chain-labs/worked-examples/weak-mlops-supply-chain-review.md",
    "instructor/mlops-evidence-pack-facilitation-guide.md",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    assert_true(not missing, f"Missing required files: {missing}")

    notebook = json.loads(read("labs/mlops-supply-chain-labs/evidence-pack-review/train.ipynb"))
    notebook_text = json.dumps(notebook)
    assert_true("!pip install scikit-learn pandas boto3" in notebook_text, "Notebook must include runtime dependency install smell")
    assert_true("FAKE_TRAINING_API_KEY_DO_NOT_USE" in notebook_text, "Notebook must include fake inline secret smell")
    assert_true("model.pkl" in notebook_text, "Notebook must reference pickle artifact")

    reqs = read("labs/mlops-supply-chain-labs/evidence-pack-review/requirements.txt")
    assert_true("scikit-learn" in reqs and "==" not in reqs, "requirements.txt must demonstrate unpinned dependency risk")

    registry = json.loads(read("labs/mlops-supply-chain-labs/evidence-pack-review/registry/model_registry.json"))
    assert_true(registry["promotion_policy"]["approval_required"] is False, "Registry must demonstrate missing approval gate")
    assert_true(
        registry["artifact_sha256_recorded"] != registry["artifact_sha256_observed"],
        "Registry must demonstrate artifact hash mismatch",
    )
    assert_true("models/latest/model.pkl" in registry["artifact_uri"], "Registry must demonstrate mutable artifact path")

    training_run = json.loads(read("labs/mlops-supply-chain-labs/evidence-pack-review/metadata/training-run.json"))
    assert_true(training_run["dataset_sha256"] is None, "Training run must demonstrate missing dataset hash")
    assert_true(training_run["dependency_lockfile"] is None, "Training run must demonstrate missing lockfile evidence")

    bucket = json.loads(read("labs/mlops-supply-chain-labs/evidence-pack-review/storage/bucket-policy.json"))
    assert_true(len(bucket["write_principals"]) >= 2, "Bucket policy must demonstrate shared write access")
    assert_true(bucket["object_lock_enabled"] is False, "Bucket policy must demonstrate no object lock")

    workflow = read("labs/mlops-supply-chain-labs/evidence-pack-review/ci/promotion-workflow.yml")
    assert_true("No artifact signature check" in workflow, "Workflow must demonstrate missing signature check")
    assert_true("No approval check" in workflow, "Workflow must demonstrate missing approval check")

    lab = read("labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md")
    for term in ["Deliverable", "Success criteria", "recommendation", "residual risk", "validation"]:
        assert_true(term.lower() in lab.lower(), f"Lab guide must include {term}")

    strong = read("labs/mlops-supply-chain-labs/worked-examples/strong-mlops-supply-chain-review.md")
    weak = read("labs/mlops-supply-chain-labs/worked-examples/weak-mlops-supply-chain-review.md")
    assert_true("Block promotion" in strong, "Strong example must make a clear block decision")
    assert_true("Weak Example" in weak and "Why this is weak" in weak, "Weak example must explain why it is weak")

    template = read("course-templates/mlops-evidence-pack-review-template.md")
    for section in ["Recommendation", "Evidence table", "Required controls", "Residual risk"]:
        assert_true(section in template, f"Template missing section: {section}")

    print("MLOps evidence-pack checks passed.")


if __name__ == "__main__":
    main()
