# Controls and remediations: Secure MLOps and AI supply chain

## Control objective

The goal is to bind production behavior to reviewed evidence. A deployed model should be traceable to the data, code, dependencies, training environment, evaluation result, approval decision, and artifact digest that justified its release.

## Weak controls

Weak controls sound useful but do not create reliable evidence:

- "Use a model registry" without immutable versions or approval policy.
- "Scan dependencies" without a lockfile or training image digest.
- "Check accuracy" without checking the artifact identity that was evaluated.
- "Restrict bucket access" while allowing shared write paths for training data.
- "Document the release" after promotion instead of enforcing metadata before promotion.
- "Use a private notebook" while storing secrets, runtime installs, and exports in the notebook.

These controls may reduce some risk, but they do not answer the main question: can we prove that the promoted artifact is the reviewed artifact?

## Strong controls

Strong controls make the secure path enforceable:

1. **Immutable model artifacts**
   - Store every artifact under a versioned immutable path.
   - Record a digest for the exact artifact.
   - Reject promotion if the digest does not match the evaluated artifact.

2. **Training-run identity**
   - Record training code commit, data version, dependency lockfile, container image digest, and runtime parameters.
   - Treat missing metadata as a failed release gate, not a warning.

3. **Dataset provenance**
   - Use dataset version IDs or content hashes.
   - Separate read and write permissions for training data.
   - Record dataset approval and retention classification.

4. **Dependency and environment control**
   - Use lockfiles for Python dependencies.
   - Build training images from reviewed manifests.
   - Avoid runtime installs in production training jobs.

5. **Promotion policy**
   - Require checks for accuracy, robustness, privacy, provenance, and rollback readiness.
   - Require human approval for high-impact models.
   - Store approval evidence with the release record.

6. **Artifact signing or attestation**
   - Sign model artifacts or sign release manifests.
   - Verify signatures and digests before deployment.
   - Fail closed on mismatch.

7. **Rollback readiness**
   - Record the last known-good artifact.
   - Test rollback in staging.
   - Keep compatibility notes for feature schemas and serving code.

## Remediation backlog format

A strong remediation backlog should use implementation language, not aspiration language:

- Add a promotion gate that rejects artifacts without a digest and training-run ID.
- Modify the registry schema to require dataset version, code commit, image digest, and approval owner.
- Replace mutable `models/latest/model.pkl` deployment input with immutable artifact IDs.
- Add CI verification that deployed digest equals evaluated digest.
- Remove runtime `pip install` from notebooks used for release training.
- Move secrets from notebooks to managed secret storage and block secret-like strings in committed notebooks.

## Validation

A remediation is not complete when the policy is written. It is complete when the team can demonstrate enforcement:

- Try to promote an artifact without a digest. It should fail.
- Try to promote an artifact whose digest differs from the evaluation record. It should fail.
- Try to train from a mutable data path without a dataset version. It should fail.
- Try to deploy a model without a rollback target. It should fail or require explicit risk acceptance.

## Residual risk

Even with strong controls, residual risk remains:

- The approved data may still be biased or incomplete.
- The evaluation may miss important operating conditions.
- A signed artifact may still encode unsafe behavior.
- A rollback may not fix downstream decisions already taken.

A good review states this clearly. Supply-chain controls prove origin and integrity. They do not prove that the model is good for every use.
