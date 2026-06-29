# Secure MLOps Checklist

Use this checklist when reviewing ML pipelines, model registries, and AI deployment workflows.

## 1. Ownership and scope

- [ ] The model has a named business owner.
- [ ] The model has a named technical owner.
- [ ] The model has a named security/risk reviewer.
- [ ] The production impact is documented.
- [ ] The model risk tier is defined.
- [ ] A rollback owner is defined.

## 2. Dataset provenance

- [ ] Data sources are documented.
- [ ] Data ownership is documented.
- [ ] Data licensing or usage rights are documented.
- [ ] Sensitive data classification is documented.
- [ ] Dataset versions are immutable or traceable.
- [ ] Dataset lineage is preserved.
- [ ] Write access to datasets is restricted.
- [ ] Dataset changes are logged.
- [ ] Data removal or correction process exists.
- [ ] Public/external datasets are reviewed before use.

## 3. Label and feature integrity

- [ ] Labeling process is documented.
- [ ] Labeler identity or source is tracked where appropriate.
- [ ] Critical labels receive review or sampling.
- [ ] Feature definitions are versioned.
- [ ] Feature stores enforce access control.
- [ ] Feature leakage is assessed.
- [ ] Feedback-derived labels are quarantined before retraining.

## 4. Notebook and experiment security

- [ ] Notebooks are scanned for secrets.
- [ ] Notebooks do not directly produce production artifacts without controlled pipeline execution.
- [ ] Notebook outputs are reviewed before sharing.
- [ ] Production data access from notebooks is restricted.
- [ ] Shell commands and downloads are reviewed for production workflows.
- [ ] Experiment tracking does not leak secrets or sensitive data.

## 5. Dependencies and build environment

- [ ] Dependencies are pinned or locked.
- [ ] Dependencies are scanned for known vulnerabilities.
- [ ] Dependency sources are approved.
- [ ] Internal mirrors or allowlists are used for high-risk environments.
- [ ] Containers are built from approved base images.
- [ ] Containers are scanned before use.
- [ ] Build and training jobs run under scoped identities.
- [ ] Training environments do not use broad administrative credentials.

## 6. Model artifact integrity

- [ ] Model artifacts have version identifiers.
- [ ] Model artifacts have hashes or integrity metadata.
- [ ] Model artifacts are signed or tied to provenance where appropriate.
- [ ] Model loading does not execute untrusted code.
- [ ] Unsafe serialization formats are avoided or sandboxed.
- [ ] Artifact storage is access-controlled.
- [ ] Artifact immutability is enforced after registration.
- [ ] Artifact metadata includes owner, training data, code version, and evaluation results.

## 7. Model registry security

- [ ] Registry authentication is enforced.
- [ ] Registry write access is limited.
- [ ] Production promotion requires approval.
- [ ] Stage changes are logged.
- [ ] Artifact deletion is restricted.
- [ ] Rollback versions are preserved.
- [ ] Registry metadata is complete.
- [ ] Registry permissions are reviewed periodically.

## 8. Evaluation and release gates

- [ ] Accuracy or utility metrics are documented.
- [ ] Security abuse-case tests are defined.
- [ ] Privacy leakage tests are defined where relevant.
- [ ] Robustness or adversarial tests are defined where relevant.
- [ ] RAG authorization tests are included for retrieval systems.
- [ ] Agent tool-use tests are included for agentic systems.
- [ ] Evaluation datasets are versioned.
- [ ] Promotion criteria are documented.
- [ ] Failed gates block deployment.

## 9. Deployment and runtime

- [ ] Deployment uses scoped runtime identities.
- [ ] Inference API enforces authentication and authorization.
- [ ] Rate limits and abuse controls exist.
- [ ] Egress is controlled where relevant.
- [ ] Logs avoid unnecessary sensitive data.
- [ ] Runtime configuration is versioned.
- [ ] Production changes are auditable.
- [ ] Rollback is tested.

## 10. Monitoring and feedback loop

- [ ] Model performance is monitored.
- [ ] Drift is monitored.
- [ ] Abuse signals are monitored.
- [ ] Security-relevant anomalies are logged.
- [ ] User feedback is not automatically trusted.
- [ ] Feedback used for retraining has provenance.
- [ ] Poisoning risk is considered.
- [ ] Incident response process exists for bad model behavior.

## 11. Documentation and residual risk

- [ ] Model card or equivalent documentation exists.
- [ ] Security assumptions are documented.
- [ ] Known limitations are documented.
- [ ] Residual risk is documented.
- [ ] Risk acceptance has an owner.
- [ ] Review cadence is defined.
