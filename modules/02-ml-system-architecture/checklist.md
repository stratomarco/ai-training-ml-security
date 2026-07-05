# Module 02 Checklist  -  ML System Architecture Security Review

Use this checklist when reviewing the architecture of an ML, LLM, RAG, or agent system.

The checklist is not a compliance standard. It is a practical review aid.

## 1. System purpose and decision impact

- [ ] The system purpose is clearly documented.
- [ ] The model’s role in the decision or workflow is clear.
- [ ] Human decision points are documented.
- [ ] Automated decision points are documented.
- [ ] Safety, financial, legal, privacy, and operational impacts are understood.
- [ ] The system owner is defined.
- [ ] The model owner is defined.
- [ ] The data owner is defined.

## 2. Data collection

- [ ] Data sources are inventoried.
- [ ] External data sources are identified.
- [ ] User-controlled data sources are identified.
- [ ] Sensitive data is classified.
- [ ] Data provenance is tracked.
- [ ] Consent and allowed use are documented where relevant.
- [ ] Retention rules are defined.
- [ ] Data ingestion has validation controls.
- [ ] Data ingestion has monitoring for anomalies.

## 3. Labeling and curation

- [ ] Label sources are documented.
- [ ] Human labeler access is controlled.
- [ ] Vendor or contractor labeling is governed.
- [ ] Label quality is measured.
- [ ] High-risk labels have review or sampling.
- [ ] Label changes are auditable.
- [ ] Labeling guidelines are versioned.
- [ ] Automated labeling is validated before use.

## 4. Feature engineering and preprocessing

- [ ] Feature definitions are documented.
- [ ] Sensitive or protected attributes are reviewed.
- [ ] Proxy features are considered.
- [ ] Features are tested for manipulation risk.
- [ ] Training and production preprocessing are consistent.
- [ ] Feature code is version controlled.
- [ ] Feature pipeline dependencies are reviewed.
- [ ] Feature pipeline outputs are monitored.

## 5. Training pipeline

- [ ] Training code is version controlled.
- [ ] Notebooks are reviewed before production use.
- [ ] Dependencies are scanned.
- [ ] Containers or environments are reproducible.
- [ ] Secrets are not stored in notebooks or datasets.
- [ ] Training jobs use least-privilege access.
- [ ] Training data access is logged.
- [ ] Training runs are tracked.
- [ ] Training outputs are reproducible enough for investigation.

## 6. Model artifacts and registry

- [ ] Model artifacts are access controlled.
- [ ] Model artifacts have integrity checks or signatures.
- [ ] Model metadata is recorded.
- [ ] Training data version is recorded.
- [ ] Training code version is recorded.
- [ ] Evaluation result is recorded.
- [ ] Model approval workflow exists.
- [ ] Registry write access is restricted.
- [ ] Unsafe artifact loading formats are reviewed.

## 7. Evaluation and release gates

- [ ] Evaluation data is separated from training data.
- [ ] Benchmark contamination is considered.
- [ ] Security tests are included, not only accuracy tests.
- [ ] Privacy leakage testing is considered.
- [ ] Robustness testing is considered.
- [ ] High-risk failure modes are reviewed.
- [ ] Release approval criteria are documented.
- [ ] Rollback criteria are defined.

## 8. Inference and serving

- [ ] Inference API requires authentication where appropriate.
- [ ] Authorization is enforced outside the model.
- [ ] Rate limits exist.
- [ ] Abuse detection exists.
- [ ] Input validation exists where possible.
- [ ] Output handling treats model output as untrusted.
- [ ] Sensitive outputs are controlled.
- [ ] Model version is logged for each decision.
- [ ] High-risk outputs have human review or escalation.

## 9. RAG architecture

- [ ] Document sources are inventoried.
- [ ] Document ingestion is controlled.
- [ ] Chunking and embedding steps are documented.
- [ ] Vector database access is controlled.
- [ ] Retrieval is authorized per user and tenant.
- [ ] Retrieved content is treated as untrusted input.
- [ ] Source provenance is shown or logged.
- [ ] Sensitive documents are excluded or protected.
- [ ] Indirect prompt injection is considered.

## 10. Agent and tool architecture

- [ ] Tool list is documented.
- [ ] Tool permissions are least privilege.
- [ ] Tool calls are authorized outside the model.
- [ ] Tool arguments are validated.
- [ ] Destructive actions require approval.
- [ ] External calls are rate limited.
- [ ] Tool execution is logged.
- [ ] Agent memory is access controlled.
- [ ] Memory writes have review or trust classification.

## 11. Monitoring and logging

- [ ] Model performance is monitored.
- [ ] Data drift is monitored.
- [ ] Abuse patterns are monitored.
- [ ] Model extraction attempts are considered.
- [ ] Privacy leakage signals are considered.
- [ ] Logs are protected.
- [ ] Logs avoid unnecessary sensitive data.
- [ ] Model version, prompt version, and data source version are logged where relevant.
- [ ] Security alerts have owners.

## 12. Feedback loops

- [ ] Feedback sources are documented.
- [ ] Feedback is not automatically trusted for retraining.
- [ ] Feedback is reviewed or sampled.
- [ ] Feedback provenance is tracked.
- [ ] Feedback manipulation is monitored.
- [ ] Promotion from feedback to training data has approval.
- [ ] Rollback is possible if feedback causes behavior degradation.

## 13. Incident response and rollback

- [ ] AI/ML incidents are included in incident response plans.
- [ ] Model rollback process exists.
- [ ] Dataset rollback or quarantine process exists.
- [ ] Compromised model artifact response is defined.
- [ ] Data poisoning investigation steps are defined.
- [ ] Model extraction response is defined.
- [ ] External provider incident dependency is understood.
- [ ] Communication plan exists for high-impact decisions.

## 14. Architecture review conclusion

Use this summary:

```text
The most important assets are:

The most important trust boundaries are:

The highest-risk lifecycle stages are:

The most important missing controls are:

The main usability or velocity tradeoffs are:

The residual risk is:
```
