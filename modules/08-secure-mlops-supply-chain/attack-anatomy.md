# Attack anatomy: MLOps supply-chain failure

## Scenario

A team trains a fraud-prioritization model in a notebook. The notebook installs dependencies at runtime, reads training data from a shared bucket, exports `model.pkl`, and uploads it to a model registry under a mutable `latest` path. The CI promotion workflow checks that accuracy is above a threshold and then deploys the model.

Nothing in this story requires an advanced attacker. It can fail through accident, insider shortcut, compromised dependency, compromised storage, or weak promotion rules.

## Path 1: dependency drift

1. The notebook runs `pip install` without pinned versions.
2. A newer package version changes preprocessing behavior.
3. The model is retrained and passes a narrow accuracy check.
4. Production behavior changes, but the team cannot reproduce the old result.
5. Incident review cannot prove whether the change came from code, data, or dependencies.

Security property lost: repeatability.

Good finding: the pipeline lacks dependency locking and training-environment identity, so model behavior cannot be reproduced or audited after release.

Weak finding: dependencies should be updated carefully.

## Path 2: artifact tampering

1. The registry stores an artifact under `models/latest/model.pkl`.
2. A user or job with write access replaces the file.
3. The promotion workflow reads the mutable path.
4. The deployment job does not verify a signed manifest or expected digest.
5. A different artifact reaches production than the one evaluated.

Security property lost: artifact integrity.

Good finding: production promotion accepts a mutable artifact URI without digest verification, so evaluation and deployment are not bound to the same object.

Weak finding: the model registry needs better security.

## Path 3: poisoned or wrong data

1. Training data comes from a shared bucket.
2. The training metadata records a bucket path but not a dataset version or hash.
3. A data slice is changed before retraining.
4. Evaluation still passes aggregate accuracy.
5. A protected segment or high-risk case type is degraded.

Security property lost: data provenance.

Good finding: the training run records a mutable data location but no dataset identity, so reviewers cannot prove which records shaped the promoted model.

Weak finding: the data should be protected.

## Path 4: approval bypass

1. A workflow promotes any model with accuracy above 0.90.
2. No security approval, rollback target, model-card review, or risk owner signoff is required.
3. A model with weak provenance is promoted because the metric passes.
4. The release later causes business or privacy harm.

Security property lost: controlled promotion.

Good finding: promotion is metric-only and lacks independent checks for provenance, artifact identity, privacy risk, and rollback readiness.

Weak finding: the approval process should be improved.

## What makes this an AI security issue

The risk is not that the system uses ML. The risk is that production decisions now depend on artifacts and metadata outside normal application-code review. The model is part of the supply chain. If the organization cannot control that chain, it cannot make a trustworthy launch decision.
