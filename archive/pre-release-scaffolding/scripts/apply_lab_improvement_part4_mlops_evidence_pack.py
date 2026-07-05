from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]


def write_text(relative_path: str, content: str) -> None:
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).lstrip(), encoding="utf-8", newline="\n")
    print(f"wrote: {relative_path}")


def write_json(relative_path: str, payload: object) -> None:
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {relative_path}")


def append_once(relative_path: str, marker: str, content: str) -> None:
    path = ROOT / relative_path
    if not path.exists():
        print(f"skip missing file: {relative_path}")
        return
    text = path.read_text(encoding="utf-8")
    if marker in text:
        print(f"already updated: {relative_path}")
        return
    path.write_text(text.rstrip() + "\n\n" + dedent(content).lstrip(), encoding="utf-8", newline="\n")
    print(f"updated: {relative_path}")


TRAIN_NOTEBOOK = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Broken ML Training Notebook\n",
                "\n",
                "This notebook is intentionally unsafe and synthetic. Students should review it as evidence, not execute it.\n",
                "All secrets, buckets, and model artifacts are fake training-only values.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Smell 1: dependency installation at training time with no lockfile or provenance.\n",
                "!pip install scikit-learn pandas boto3\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Smell 2: fake inline secret and shared storage path.\n",
                "TRAINING_API_KEY = 'FAKE_TRAINING_API_KEY_DO_NOT_USE'\n",
                "TRAINING_DATA_URI = 's3://shared-ml-training-bucket/raw/customer-events.csv'\n",
                "MODEL_OUTPUT_URI = 's3://shared-ml-training-bucket/models/latest/model.pkl'\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Smell 3: no dataset hash, no schema check, no split manifest, no approval gate.\n",
                "import pickle\n",
                "from sklearn.linear_model import LogisticRegression\n",
                "model = LogisticRegression()\n",
                "# Training data intentionally omitted from this evidence pack.\n",
                "# The review question is whether this pipeline leaves enough evidence to trust the artifact.\n",
                "with open('model.pkl', 'wb') as f:\n",
                "    pickle.dump(model, f)\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Review prompt\n",
                "\n",
                "Do not execute this notebook as part of the lab. Identify the supply-chain and promotion-control failures that would make this model unsafe to promote.\n",
            ],
        },
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "version": "3.x"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}


MODEL_REGISTRY = {
    "registry": "training-only-fake-registry",
    "model_name": "customer-risk-classifier",
    "candidate_version": "2026.07.03-unsafe-demo",
    "artifact_uri": "s3://shared-ml-training-bucket/models/latest/model.pkl",
    "artifact_sha256_recorded": "1111111111111111111111111111111111111111111111111111111111111111",
    "artifact_sha256_observed": "2222222222222222222222222222222222222222222222222222222222222222",
    "promotion_policy": {
        "approval_required": False,
        "minimum_reviewers": 0,
        "allowed_promoters": ["ml-platform-ci", "shared-training-role"],
        "requires_dataset_manifest": False,
        "requires_dependency_lockfile": False,
        "requires_signed_artifact": False,
        "requires_model_card": False,
        "rollback_plan_required": False,
    },
    "last_promotion_event": {
        "actor": "shared-training-role",
        "source_branch": "experiment/notebook-cleanup",
        "environment": "production-candidate",
        "decision": "auto-promoted",
        "reason": "accuracy_above_threshold",
    },
}


TRAINING_RUN = {
    "run_id": "train-2026-07-03-unsafe-demo",
    "model_name": "customer-risk-classifier",
    "dataset_uri": "s3://shared-ml-training-bucket/raw/customer-events.csv",
    "dataset_sha256": None,
    "schema_version": None,
    "feature_manifest": None,
    "dependency_lockfile": None,
    "base_image_digest": "python:3.11-latest",
    "trainer_identity": "shared-training-role",
    "metrics": {
        "accuracy": 0.941,
        "auc": 0.902,
        "calibration_checked": False,
        "slice_evaluation_checked": False,
    },
    "notes": "Synthetic evidence pack. Review metadata gaps; do not run as a real pipeline.",
}


BUCKET_POLICY = {
    "bucket": "shared-ml-training-bucket",
    "purpose": "synthetic training-only evidence pack",
    "write_principals": ["shared-training-role", "notebook-users", "ml-platform-ci"],
    "read_principals": ["analytics-readonly", "notebook-users", "ml-platform-ci"],
    "versioning_enabled": False,
    "object_lock_enabled": False,
    "public_access_block": True,
    "risk_notes": [
        "Multiple identities can overwrite model artifacts.",
        "No object lock or immutable artifact path is enforced.",
        "The model registry points at models/latest/model.pkl instead of a content-addressed artifact.",
    ],
}


def main() -> None:
    write_text(
        "labs/mlops-supply-chain-labs/evidence-pack-review/README.md",
        """
        # MLOps Evidence Pack Review

        This directory is a static, synthetic evidence pack for Module 08. It is not a runnable ML pipeline. Students review the evidence as if they were assessing whether a model candidate should be promoted.

        ## Learning objective

        The goal is to identify whether the training and promotion evidence is strong enough to trust the model artifact. Students should focus on provenance, dependency control, artifact integrity, identity, approval gates, rollback, and monitoring readiness.

        ## Files

        | File | What to review |
        |---|---|
        | `train.ipynb` | Notebook training smells: inline install, fake inline secret, shared bucket, pickle export, missing manifests |
        | `requirements.txt` | Unpinned dependencies and missing lockfile |
        | `metadata/training-run.json` | Missing dataset hash, schema version, feature manifest, and dependency lockfile |
        | `registry/model_registry.json` | Weak promotion policy and artifact hash mismatch |
        | `storage/bucket-policy.json` | Shared write permissions and mutable model path |
        | `ci/promotion-workflow.yml` | Accuracy-only promotion and no signed artifact check |
        | `artifacts/model.pkl.README.md` | Placeholder explaining why the real binary artifact is not shipped |

        ## Student task

        Write a short MLOps supply-chain review that answers:

        1. Can this candidate be promoted as-is?
        2. Which evidence is missing or untrustworthy?
        3. Which controls must be implemented before promotion?
        4. How would the team validate the fix?
        5. What residual risk remains after remediation?

        ## Safety note

        This evidence pack is intentionally fake and local. Do not connect it to real buckets, registries, notebooks, or credentials.
        """,
    )

    write_text(
        "labs/mlops-supply-chain-labs/evidence-pack-review/requirements.txt",
        """
        scikit-learn
        pandas
        boto3
        joblib
        """,
    )

    write_json("labs/mlops-supply-chain-labs/evidence-pack-review/train.ipynb", TRAIN_NOTEBOOK)
    write_json("labs/mlops-supply-chain-labs/evidence-pack-review/registry/model_registry.json", MODEL_REGISTRY)
    write_json("labs/mlops-supply-chain-labs/evidence-pack-review/metadata/training-run.json", TRAINING_RUN)
    write_json("labs/mlops-supply-chain-labs/evidence-pack-review/storage/bucket-policy.json", BUCKET_POLICY)

    write_text(
        "labs/mlops-supply-chain-labs/evidence-pack-review/ci/promotion-workflow.yml",
        """
        name: unsafe-model-promotion-demo

        on:
          workflow_dispatch:

        jobs:
          promote:
            runs-on: ubuntu-latest
            permissions:
              contents: read
            steps:
              - name: Check candidate metric
                run: |
                  echo "accuracy=0.941"
                  echo "Promoting because accuracy is above threshold"

              - name: Promote model
                run: |
                  echo "Copying model.pkl to production-candidate registry"
                  echo "No artifact signature check"
                  echo "No dataset manifest check"
                  echo "No approval check"
        """,
    )

    write_text(
        "labs/mlops-supply-chain-labs/evidence-pack-review/artifacts/model.pkl.README.md",
        """
        # model.pkl placeholder

        The lab intentionally does not ship a binary pickle model. Students should treat the referenced `model.pkl` as an artifact described by the surrounding metadata.

        Review question: would you trust an opaque pickle artifact promoted from a mutable `latest` path without a verified content hash, signed artifact, dependency manifest, dataset manifest, and approval record?
        """,
    )

    write_text(
        "labs/mlops-supply-chain-labs/evidence-pack-review/artifacts/model-sha256.txt",
        """
        recorded: 1111111111111111111111111111111111111111111111111111111111111111
        observed: 2222222222222222222222222222222222222222222222222222222222222222
        status: mismatch
        """,
    )

    write_text(
        "labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md",
        """
        # MLOps Evidence Pack Review Lab

        ## Purpose

        This is the concrete Module 08 review lab. It is intentionally a reasoning lab, not a runnable pipeline. Students inspect a static evidence pack and decide whether a model candidate should be promoted.

        ## Why this is not a runnable pipeline

        The security decision in this module is not whether a toy pipeline can execute. The decision is whether the evidence around an ML artifact is strong enough to trust the artifact in production. A static evidence pack is closer to how engineers review real ML supply-chain risk: notebooks, dependency files, registry metadata, storage permissions, promotion logs, and review records.

        ## Evidence pack

        Review:

        ```text
        labs/mlops-supply-chain-labs/evidence-pack-review/
        ```

        ## Scenario

        An ML team wants to promote `customer-risk-classifier` to a production-candidate registry. The model has acceptable aggregate accuracy, but the evidence pack contains weak or missing supply-chain controls.

        ## Student steps

        1. Inspect `train.ipynb` and identify notebook-level risks.
        2. Inspect `requirements.txt` and dependency evidence.
        3. Inspect `metadata/training-run.json` and decide whether the training run is reproducible.
        4. Inspect `registry/model_registry.json` and decide whether the promotion gate is acceptable.
        5. Inspect `storage/bucket-policy.json` and identify who can overwrite training data or model artifacts.
        6. Inspect `ci/promotion-workflow.yml` and identify whether the workflow proves artifact integrity.
        7. Produce a review using the MLOps evidence-pack review template.

        ## Required findings

        A strong submission should identify at least these issues:

        - dependencies are unpinned and no lockfile is provided;
        - the notebook installs dependencies at runtime;
        - a fake inline secret appears in the notebook;
        - the model artifact is a mutable pickle path rather than a content-addressed signed artifact;
        - recorded and observed artifact hashes do not match;
        - dataset hash, schema version, feature manifest, and split manifest are missing;
        - the promotion policy allows auto-promotion with no approval;
        - storage write permissions allow shared identities to overwrite artifacts;
        - aggregate accuracy is treated as a release gate without robustness, privacy, slice, or rollback evidence.

        ## Deliverable

        Submit one review memo with:

        - recommendation: promote, limited pilot, or block;
        - evidence table;
        - root causes;
        - required controls;
        - validation plan;
        - residual risk.

        ## Success criteria

        The student should not merely say that the pipeline is insecure. The review must explain what evidence is missing, why that evidence matters, what control should replace it, and how the team would know the control works.
        """,
    )

    write_text(
        "modules/08-secure-mlops-supply-chain/mlops-evidence-pack-review.md",
        """
        # Module 08 Lab: MLOps Evidence Pack Review

        This Module 08 lab uses a static evidence pack instead of a fake runnable pipeline.

        ## Core decision

        Should the model candidate be promoted to a production-candidate registry?

        ## Review target

        ```text
        labs/mlops-supply-chain-labs/evidence-pack-review/
        ```

        ## Why this fits Module 08

        MLOps supply-chain security is mostly an evidence and control problem. The reviewer needs to know whether dependencies, data, training code, model artifacts, registry entries, promotion gates, and rollback plans are trustworthy.

        ## What students must produce

        Students produce a review memo and a remediation backlog. The best submissions show:

        - artifact provenance and integrity gaps;
        - weak identity and storage boundaries;
        - missing reproducibility evidence;
        - weak promotion policy;
        - specific controls such as lockfiles, dataset manifests, signed artifacts, immutable artifact paths, approval gates, and rollback plans;
        - a validation plan for each control.
        """,
    )

    write_text(
        "course-templates/mlops-evidence-pack-review-template.md",
        """
        # MLOps Evidence Pack Review Template

        ## Recommendation

        Choose one:

        - Promote
        - Limited pilot only
        - Block promotion

        Explain the decision in two or three sentences.

        ## Evidence table

        | Evidence item | Observation | Security property affected | Risk |
        |---|---|---|---|
        | Training notebook |  |  |  |
        | Dependencies |  |  |  |
        | Dataset metadata |  |  |  |
        | Artifact metadata |  |  |  |
        | Registry policy |  |  |  |
        | Storage policy |  |  |  |
        | Promotion workflow |  |  |  |

        ## Root causes

        Describe the underlying control failures, not only the symptoms.

        ## Required controls

        | Control | Owner | Validation method | Priority |
        |---|---|---|---|
        |  |  |  |  |

        ## Residual risk

        What risk remains after the recommended controls are implemented?

        ## Final decision

        State the promotion decision again and name the minimum evidence required to revisit it.
        """,
    )

    write_text(
        "assessments/mlops-evidence-pack-review-rubric.md",
        """
        # MLOps Evidence Pack Review Rubric

        ## Excellent

        - Makes a clear promote, limited-pilot, or block decision.
        - Ties every major observation to a security property: integrity, provenance, reproducibility, least privilege, approval, rollback, or monitoring readiness.
        - Distinguishes symptoms from root causes.
        - Recommends implementable controls and validation methods.
        - Explains residual risk after remediation.

        ## Adequate

        - Identifies most major issues.
        - Recommends plausible controls but may be light on validation.
        - Gives a decision but does not fully justify the business or engineering tradeoff.

        ## Weak

        - Lists smells without connecting them to risk.
        - Treats accuracy as sufficient evidence for promotion.
        - Says to add security review or guardrails without naming concrete controls.
        - Provides no validation plan or residual-risk statement.
        """,
    )

    write_text(
        "labs/mlops-supply-chain-labs/worked-examples/strong-mlops-supply-chain-review.md",
        """
        # Strong Example: MLOps Evidence Pack Review

        ## Recommendation

        Block promotion. The model may have acceptable aggregate accuracy, but the evidence pack does not establish artifact integrity, training reproducibility, dependency provenance, storage integrity, or approval control.

        ## Key findings

        | Finding | Evidence | Required control | Validation |
        |---|---|---|---|
        | Mutable artifact path | Registry points to `models/latest/model.pkl` | Content-addressed artifact path and signed artifact | Registry rejects unsigned or hash-mismatched artifacts |
        | Hash mismatch | Recorded and observed SHA-256 values differ | Verify artifact hash before promotion | Promotion job fails on mismatch |
        | Unpinned dependencies | `requirements.txt` has no pinned versions | Lockfile with reviewed package sources | Rebuild uses identical dependency graph |
        | Missing dataset evidence | Training run has no dataset hash or schema version | Dataset manifest and schema contract | Promotion requires matching dataset manifest |
        | Weak promotion gate | Approval not required and zero reviewers | Human approval for production candidate | CI blocks promotion without approval record |
        | Shared write permissions | Multiple identities can write to the bucket | Least-privilege storage policy and object lock | Unauthorized overwrite attempt fails |

        ## Residual risk

        Even after these controls, the model can still fail under drift, data-quality changes, or adversarial input. Promotion should require monitoring, rollback, and periodic review of training data and model behavior.
        """,
    )

    write_text(
        "labs/mlops-supply-chain-labs/worked-examples/weak-mlops-supply-chain-review.md",
        """
        # Weak Example: MLOps Evidence Pack Review

        The model should probably be okay because the accuracy is high. The notebook has some messy parts and the team should clean it up. They should add security checks and maybe review the bucket permissions. I would let it go to staging and see what happens.

        ## Why this is weak

        - No clear security property is named.
        - Accuracy is treated as enough evidence.
        - The artifact hash mismatch is not addressed.
        - The recommendation does not name concrete controls.
        - There is no validation method.
        - There is no residual-risk statement.
        """,
    )

    write_text(
        "instructor/mlops-evidence-pack-facilitation-guide.md",
        """
        # Instructor Guide: MLOps Evidence Pack Review

        ## Teaching goal

        Students should learn that ML supply-chain security is an evidence problem. A model should not move toward production just because a notebook runs or aggregate accuracy is high.

        ## Facilitation plan

        1. Start with the promotion question: would you promote this model?
        2. Give students 20 minutes to inspect the evidence pack.
        3. Ask them to identify the first blocker, not every possible issue.
        4. Force each finding into the pattern: evidence, root cause, control, validation, residual risk.
        5. Compare one strong and one weak example.

        ## Common student mistakes

        - Saying "pin dependencies" but not requiring a lockfile validation step.
        - Saying "review the model" without naming artifact signing, hash checks, or registry gates.
        - Treating a fake inline secret as the only issue.
        - Ignoring the mutable `latest` artifact path.
        - Ignoring rollback and monitoring readiness.

        ## Anchor answer

        The strongest decision is to block promotion until the team can prove dependency provenance, dataset provenance, artifact integrity, registry approval, storage least privilege, and rollback readiness.
        """,
    )

    append_once(
        "labs/mlops-supply-chain-labs/README.md",
        "MLOps Evidence Pack Review Lab",
        """
        ## MLOps Evidence Pack Review Lab

        Use `mlops-evidence-pack-review-lab.md` for the concrete Module 08 supply-chain review exercise. The evidence pack is intentionally static: students review notebook, dependency, artifact, registry, storage, and promotion evidence instead of running a fake pipeline.
        """,
    )

    append_once(
        "modules/08-secure-mlops-supply-chain/README.md",
        "MLOps Evidence Pack Review",
        """
        ## MLOps Evidence Pack Review

        This module now includes `mlops-evidence-pack-review.md`, a concrete review lab backed by the static evidence pack in `labs/mlops-supply-chain-labs/evidence-pack-review/`.
        """,
    )

    append_once(
        "labs/mlops-supply-chain-labs/broken-ml-pipeline-lab.md",
        "Evidence-pack option",
        """
        ## Evidence-pack option

        This tabletop can be run with the static evidence pack in `evidence-pack-review/`. That pack gives students concrete artifacts to inspect: notebook, dependency file, registry metadata, storage policy, promotion workflow, and artifact hash evidence. The intended learning outcome is a review decision and remediation backlog, not successful execution of a toy pipeline.
        """,
    )

    write_text(
        "release-notes/v1.1-dev-lab-improvement-part4-mlops-evidence-pack.md",
        """
        # v1.1-dev Lab Improvement Part 4: MLOps Evidence Pack

        Adds a concrete static evidence pack for Module 08 MLOps supply-chain review. The lab remains a reasoning lab by design, but students now inspect real local files instead of only discussing a paper scenario.

        Added:

        - `labs/mlops-supply-chain-labs/evidence-pack-review/`
        - `labs/mlops-supply-chain-labs/mlops-evidence-pack-review-lab.md`
        - `modules/08-secure-mlops-supply-chain/mlops-evidence-pack-review.md`
        - `course-templates/mlops-evidence-pack-review-template.md`
        - `assessments/mlops-evidence-pack-review-rubric.md`
        - strong and weak worked examples
        - instructor facilitation guide
        """,
    )

    print("\nApplied lab improvement Part 4 MLOps evidence-pack package.")


if __name__ == "__main__":
    main()
