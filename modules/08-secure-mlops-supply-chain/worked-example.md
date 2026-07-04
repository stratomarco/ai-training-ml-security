# Worked example: Evidence-pack review finding

## Weak finding

The model pipeline is insecure because the notebook uses unpinned dependencies and the registry metadata is incomplete. The team should improve MLOps security before launch.

## Why this is weak

This finding names symptoms but does not explain the security property lost, how the release can fail, what control must change, or how to validate the fix. It sounds reasonable, but an engineering team cannot implement it directly.

## Strong finding

**Finding:** Production promotion does not bind the evaluated model to the deployed artifact.

**Evidence:** The evidence pack proposes deployment from `models/latest/model.pkl`, while the registry metadata records a different expected artifact hash than the observed artifact hash. The promotion workflow checks only model accuracy and does not verify an immutable artifact digest, signed manifest, approval record, or rollback target.

**Root cause:** The release process treats the model registry path as trusted storage rather than an enforced promotion boundary. The evaluation record, registry metadata, and deployment input are not cryptographically or procedurally bound to the same artifact.

**Impact:** A modified or wrong model can be deployed even if it was not the artifact evaluated by the team. This breaks auditability and makes incident response unreliable because the team cannot prove which model reached production.

**Remediation:** Replace mutable artifact paths with immutable artifact IDs. Require the promotion workflow to verify artifact digest, training-run ID, dataset version, evaluation report, approval owner, and rollback target before deployment. Fail promotion if any field is missing or mismatched.

**Validation:** Attempt to promote an artifact whose digest differs from the evaluation record. The workflow should fail. Attempt to promote an artifact with no rollback target. The workflow should fail or require explicit risk acceptance from the model owner and security reviewer.

**Residual risk:** This control proves artifact identity and promotion integrity. It does not prove the model is robust, fair, or privacy-preserving. Those still require evaluation and monitoring controls.

## Instructor note

Use this example to show the difference between finding symptoms and finding control failure. Students should leave Module 08 able to write findings that an MLOps platform team can implement.
