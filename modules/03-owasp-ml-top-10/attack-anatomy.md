# Attack Anatomy: From OWASP Category to Observable Failure

## The pattern

An OWASP ML category becomes useful when it is tied to a failure path.

Category -> entry point -> vulnerable component -> security property -> impact -> control -> validation.

Without that chain, the category is only a label.

## Input manipulation

Entry point: inference input.

Vulnerable component: classifier, ranker, detector, or LLM application.

Security property: integrity of decision.

Impact: bad classification, missed abuse, false block, or unsafe answer.

Control: adversarial evaluation, confidence threshold, fallback, secondary review, non-model enforcement for critical gates.

Validation: perturb inputs and confirm that high-impact decisions do not rely on brittle model output alone.

## Data poisoning

Entry point: training data, labels, feedback, fine-tuning set, retrieval corpus, or memory.

Vulnerable component: training pipeline or learning loop.

Security property: integrity of learned behavior or retrieved context.

Impact: degraded detection, biased behavior, hidden trigger, or unsafe recommendations.

Control: data provenance, label review, anomaly detection, dataset diffing, source trust, training approval, rollback.

Validation: introduce controlled poisoned examples in a test environment and confirm detection or promotion block.

## Model theft or extraction

Entry point: repeated queries, API access, observable scores, or model artifacts.

Vulnerable component: exposed prediction API or artifact store.

Security property: confidentiality and business value.

Impact: copied decision boundary, abuse optimization, or intellectual-property loss.

Control: rate limits, output minimization, access control, monitoring, watermarking where appropriate, artifact protection.

Validation: query harness shows that excessive access is limited, monitored, or blocked.

## Output integrity failure

Entry point: post-model threshold, mapping, label display, or decision routing.

Vulnerable component: output processing layer.

Security property: integrity of final decision.

Impact: changing outcomes without changing the model.

Control: signed configuration, reviewed thresholds, change control, monitoring, separation of duties.

Validation: threshold tampering cannot be deployed without approval and audit.

## Supply-chain attack

Entry point: dependency, notebook, model artifact, registry metadata, CI workflow, or storage path.

Vulnerable component: build and promotion process.

Security property: integrity of artifact and release.

Impact: malicious model, wrong model, unreviewed artifact, or non-reproducible production behavior.

Control: lockfiles, SBOM or ML-BOM, artifact digest, signed manifests, registry policy, approval gates, rollback.

Validation: artifact with missing provenance or mismatched hash cannot be promoted.

## Privacy attack

Entry point: model query, retrieval query, logs, embeddings, training data, or generated output.

Vulnerable component: model, retrieval layer, or observability path.

Security property: privacy and confidentiality.

Impact: secret leakage, membership inference, reconstruction, cross-tenant exposure, or over-retention.

Control: data minimization, access control, privacy review, redaction, retention, differential privacy where appropriate, output constraints.

Validation: sensitive fragments are not exposed to unauthorized users or broad logs.
