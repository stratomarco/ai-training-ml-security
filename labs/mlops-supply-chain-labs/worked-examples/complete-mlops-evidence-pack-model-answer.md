# Complete Model Answer: MLOps Evidence-Pack Review

This model answer is a reference submission for the Module 08 evidence-pack review lab. It is not the only valid answer. A strong student submission may use different wording, but it should connect every recommendation to evidence in the provided pack and should explain how the fix will be validated.

## Executive summary

Recommendation: **do not promote the model to production yet. Approve a limited remediation sprint, then reassess promotion after provenance, artifact-integrity, approval, and rollback controls are demonstrated.**

The evidence pack shows a model promotion process that relies on accuracy and convenience rather than supply-chain assurance. The issues are not isolated style problems. They form an attack path: an unreviewed notebook can install unpinned packages, train from weakly identified data, export a mutable pickle artifact, write it to a shared location, and promote it through a workflow that does not require artifact signing, manifest verification, human approval, rollback evidence, or separation of duties.

The primary security concern is not that the model may be inaccurate. The concern is that the organization cannot prove what code, data, dependency set, parameters, and artifact were promoted. If a bad model is deployed, the team would struggle to determine whether the cause was an honest training change, a dependency compromise, a poisoned dataset, a tampered artifact, or an unauthorized promotion.

## Scope and assumptions

Reviewed artifacts:

- `requirements.txt`
- `train.ipynb`
- `registry/model_registry.json`
- `metadata/training-run.json`
- `storage/bucket-policy.json`
- `ci/promotion-workflow.yml`
- `artifacts/model.pkl.README.md`
- `artifacts/model-sha256.txt`

Assumptions:

- All data and secrets in the pack are fake and local to the training repository.
- The goal is to assess an MLOps promotion process, not to exploit a real service.
- The intended production use is important enough that model provenance, artifact integrity, rollback, and approval evidence matter.
- This is a reasoning lab. The deliverable is a review artifact, not a runnable exploit.

## Finding 1: Model promotion lacks a verifiable artifact identity

Severity: High

### Evidence

The registry metadata points to a mutable artifact location such as `models/latest/model.pkl`. The artifact identity is not tied to an immutable digest, signed manifest, or build attestation. The evidence pack also includes a recorded hash that does not match the expected promotion evidence.

### Why this matters

A model artifact is executable decision logic for the system. If the promotion process cannot prove exactly which artifact was reviewed and deployed, then approval is only symbolic. A later investigation cannot reliably answer which model was live, where it came from, or whether it was modified after training.

### Security property at risk

- Integrity of the promoted artifact
- Traceability from training run to deployed model
- Non-repudiation of approval and promotion decisions

### Weak remediation

"Rename the model file with a version number."

This helps humans read the file name, but it does not prove artifact integrity. A file named `model-v3.pkl` can still be overwritten or replaced.

### Strong remediation

Require every promotable model to have:

- immutable artifact URI
- SHA-256 digest stored in the registry
- signed model manifest
- training-run identifier
- dataset version and hash
- code commit hash
- dependency lockfile reference
- approval record linked to the exact digest

Promotion must fail if the observed artifact digest does not match the registry digest or signed manifest.

### Validation

Before promotion, run an automated check that retrieves the candidate artifact, computes its digest, compares it with the registry digest, verifies the signature, and records the result in the promotion log. Attempt to promote an artifact with a changed digest and confirm the workflow blocks it.

### Residual risk

Digest and signature checks do not prove that the model is safe or fair. They prove that the reviewed artifact is the artifact being promoted. Model behavior testing, monitoring, and rollback are still required.

## Finding 2: Dependency provenance is weak and reproducibility is not demonstrated

Severity: High

### Evidence

`requirements.txt` contains unpinned dependencies. The training notebook also installs packages at runtime. The training metadata does not include a dependency lockfile hash or environment image digest.

### Why this matters

The same training code may produce different behavior depending on the dependency versions resolved at runtime. A compromised or changed dependency could influence the model or training process without leaving clear evidence in the model registry.

### Security property at risk

- Build reproducibility
- Dependency integrity
- Incident investigation quality

### Weak remediation

"Review the notebook before running it."

Manual review is useful but incomplete. It does not preserve a reproducible environment, and it cannot reliably catch future dependency changes.

### Strong remediation

Use a controlled training environment:

- lock dependencies with exact versions and hashes
- build training images from reviewed base images
- record the image digest in training metadata
- block runtime package installation in production training jobs
- scan dependencies and base images before training
- store dependency SBOM or ML-BOM with the model package

### Validation

Rebuild the model twice from the same code, data, and locked environment. Confirm that the training run metadata includes the same lockfile hash and environment image digest. Attempt to run the notebook with inline package installation enabled and confirm the controlled pipeline rejects it.

### Residual risk

Pinned dependencies can still contain vulnerabilities. Pinning improves traceability; it does not replace vulnerability monitoring, patch management, and exception handling.

## Finding 3: Training data provenance and schema evidence are insufficient

Severity: Medium to High

### Evidence

The training metadata does not provide a complete dataset hash, dataset version, schema version, or provenance statement. The reviewer cannot determine whether the model was trained on the intended data or whether the data changed between evaluation and promotion.

### Why this matters

Training data is part of the model supply chain. If the data source, version, and transformation path are not recorded, then the team cannot distinguish between normal drift, accidental data corruption, and deliberate poisoning.

### Security property at risk

- Training-data integrity
- Reproducibility
- Poisoning investigation capability

### Weak remediation

"Ask the data team to confirm that the dataset is correct."

A verbal confirmation does not create durable evidence and does not support automated promotion checks.

### Strong remediation

Require a dataset provenance record for each training run:

- dataset identifier
- immutable dataset version
- dataset hash or manifest hash
- schema version
- transformation code commit
- data quality checks
- owner approval for sensitive data use
- retention and privacy classification

Promotion should fail if the dataset evidence is missing or does not match the reviewed training run.

### Validation

Create a training run with missing dataset hash and confirm the promotion gate rejects it. Create a valid run with a complete dataset manifest and confirm the registry links the dataset evidence to the candidate model.

### Residual risk

A dataset manifest does not prove that labels are semantically correct. Label quality, bias review, privacy controls, and monitoring remain separate assurance activities.

## Finding 4: Promotion workflow lacks approval gates and separation of duties

Severity: High

### Evidence

The promotion workflow relies on automated conditions and accuracy-style logic, but it does not require a signed review, security approval, model-owner approval, rollback evidence, or separation between training and promotion authority.

### Why this matters

A model can pass a technical threshold and still be unsafe to deploy. Promotion is a risk decision, not only a metric comparison. Without approval gates, a compromised workflow, mistaken configuration, or over-permissive engineer account could promote an unsafe model without meaningful review.

### Security property at risk

- Change-control integrity
- Accountability
- Least privilege

### Weak remediation

"Notify the team in Slack when a model is promoted."

Notification after promotion does not prevent unsafe promotion. It may help detection, but it is not an approval gate.

### Strong remediation

Introduce promotion policy as code:

- separate train, register, approve, promote, and rollback permissions
- require model-owner approval
- require security review for high-impact models
- require rollback plan evidence
- require signed artifact and manifest verification
- require evaluation report and threshold justification
- log all approval decisions and artifact digests

### Validation

Attempt promotion without approval and confirm it fails. Attempt promotion with approval but with a mismatched artifact digest and confirm it fails. Confirm all approval records are linked to the same immutable model digest.

### Residual risk

Approval gates can become rubber stamps. Review quality still depends on clear criteria, accountable reviewers, and periodic audit.

## Finding 5: Shared mutable storage weakens artifact integrity

Severity: Medium to High

### Evidence

The bucket policy allows shared write access and does not show object lock, retention controls, or a clear separation between staging and production artifacts.

### Why this matters

If many actors or jobs can overwrite model artifacts, then registry approval may not reflect what is actually deployed. Shared mutable storage creates a gap between review and runtime.

### Security property at risk

- Artifact integrity
- Least privilege
- Environment separation

### Weak remediation

"Ask engineers not to overwrite model files."

A convention is not a control. The system must prevent or detect unauthorized overwrite.

### Strong remediation

Use storage controls that enforce artifact immutability and separation:

- write-once artifact paths
- object lock or retention policy for promoted artifacts
- separate buckets or prefixes for training, staging, and production
- least-privilege service accounts
- promotion service is the only writer to production model locations
- audit logs for writes, reads, and policy changes

### Validation

Attempt to overwrite a promoted artifact using a training role and confirm access is denied. Attempt to write directly to production without the promotion service and confirm access is denied. Verify audit logs show attempted violations.

### Residual risk

Storage controls do not protect against a compromised promotion service. That risk is reduced through approval gates, signed manifests, runtime verification, and monitoring.

## Finding 6: Notebook-based training contains unsafe operational patterns

Severity: Medium

### Evidence

The training notebook contains runtime package installation and a fake inline secret. It also performs training and export steps in a way that is difficult to reproduce and review as a controlled pipeline.

### Why this matters

Notebooks are useful for exploration, but production training requires reproducible, reviewable, and controlled execution. Inline secrets and runtime dependency installation are signals that experimentation code is being promoted without enough hardening.

### Security property at risk

- Secret hygiene
- Reproducibility
- Reviewability

### Weak remediation

"Tell data scientists not to put secrets in notebooks."

Policy alone is insufficient. The pipeline should prevent secret exposure and provide safe ways to access approved resources.

### Strong remediation

Separate experimentation from production training:

- block inline secrets with scanning before merge and before training
- use workload identity or secret manager integration
- convert production training into reviewed scripts or pipeline components
- disallow runtime package installation in production training
- record code commit, parameters, data version, and environment digest

### Validation

Run secret scanning on notebook changes and confirm the fake secret pattern is detected. Attempt production training from a notebook containing inline package installation and confirm it is blocked or requires explicit exception approval.

### Residual risk

Secret scanning can miss context-specific secrets. It should be paired with secret rotation, scoped credentials, and runtime access monitoring.

## Remediation backlog

### Before production promotion

1. Block promotion unless artifact digest matches registry and signed manifest.
2. Replace mutable `latest` artifact references with immutable artifact URIs.
3. Require model-owner and security approval for production promotion.
4. Add rollback plan evidence to the promotion checklist.
5. Enforce least-privilege storage roles and deny direct writes to production artifact paths.
6. Require dataset manifest and dependency lockfile evidence for every candidate model.

### Before pilot or limited internal rollout

1. Add automated checks for dependency lockfile presence and training environment digest.
2. Add secret scanning for notebooks and training scripts.
3. Create a standard model card or release record with training data, evaluation, limitations, and monitoring plan.
4. Add audit log review for model registration and promotion events.

### Continuous controls

1. Monitor dependency vulnerabilities and base image drift.
2. Review model registry permissions quarterly.
3. Test rollback in a non-production environment.
4. Periodically sample promoted models and verify registry evidence against deployed artifact digests.

## Leadership recommendation

Do not approve production promotion based on the current evidence pack. The model may or may not be good, but the promotion system cannot prove that the reviewed artifact is the deployed artifact, cannot reproduce the training environment, and cannot show sufficient approval evidence.

Recommended decision: **delay production promotion, approve a short remediation sprint, then allow a limited pilot only after artifact identity, provenance, approval, and rollback evidence are demonstrated.**

This is not a recommendation to slow teams down indefinitely. The goal is to create a promotion path that is fast because it is standardized, not fast because it skips evidence.

## What a strong student should learn

A strong answer does not simply list smells. It explains why each missing piece of evidence matters to a real promotion decision. The most important lesson is that model supply-chain security is not only about preventing malicious changes. It is also about being able to prove what changed, who approved it, what evidence supported the decision, and how the team can recover if the decision was wrong.
