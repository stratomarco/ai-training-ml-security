# Remediation Plan: MLOps Evidence-Pack Review

## Goal

Move the model promotion path from trust-based promotion to evidence-based promotion.

## Phase 1: Stop unsafe promotion paths

Owner: ML platform team and security architecture

Actions:

1. Disable production promotion from mutable artifact references.
2. Require an immutable artifact digest for every promotion candidate.
3. Block promotion if the observed artifact hash differs from the registry hash.
4. Require model-owner approval for production promotion.
5. Require rollback plan evidence before promotion.

Validation:

- Attempt to promote a model with a mismatched hash. Expected result: blocked.
- Attempt to promote without owner approval. Expected result: blocked.
- Attempt to promote without rollback evidence. Expected result: blocked.

## Phase 2: Establish provenance evidence

Owner: ML engineering and data platform

Actions:

1. Create dataset manifests with dataset version, hash, schema version, and transformation commit.
2. Add dependency lockfiles with exact versions and hashes.
3. Record training image digest for every production training run.
4. Store training parameters and code commit with the model registry entry.
5. Generate a model release record for each candidate artifact.

Validation:

- Candidate with missing dataset manifest is rejected.
- Candidate with missing lockfile is rejected.
- Candidate with missing training image digest is rejected.

## Phase 3: Harden storage and promotion permissions

Owner: Cloud platform and ML platform

Actions:

1. Separate training, staging, and production artifact paths.
2. Make production artifact paths write-once or object-locked.
3. Remove shared write permissions from production artifact storage.
4. Allow only the promotion service to write production artifacts.
5. Enable audit logs for artifact writes and policy changes.

Validation:

- Training role cannot write to production artifact path.
- Engineer role cannot overwrite promoted artifact directly.
- Audit log captures attempted writes and policy changes.

## Phase 4: Improve notebook and training hygiene

Owner: ML engineering

Actions:

1. Keep notebooks for exploration, not production training.
2. Convert production training to reviewed scripts or pipeline components.
3. Block runtime package installation in production training jobs.
4. Add secret scanning for notebooks and training scripts.
5. Use secret manager or workload identity instead of inline secrets.

Validation:

- Notebook with fake secret is flagged by scanning.
- Production job with runtime package installation fails policy check.
- Training job accesses approved resources without inline secrets.

## Phase 5: Operate the control

Owner: Security, ML platform, model owner

Actions:

1. Review promotion exceptions monthly.
2. Sample deployed models and verify runtime artifact digest against registry evidence.
3. Test rollback quarterly.
4. Review model registry permissions quarterly.
5. Track model supply-chain findings in the same risk system used for application security exceptions.

Validation:

- Sampled deployed artifacts match registry digests.
- Rollback test completes within target recovery time.
- Registry permission review identifies no stale privileged accounts.

## Residual risk after remediation

Even after these controls, the model can still fail because of data drift, weak labels, adversarial input, or incorrect business assumptions. The remediation plan reduces supply-chain uncertainty. It does not replace model validation, robustness testing, privacy review, or monitoring.
