# Module 10 Checklist — Adversarial ML and Robustness

Use this checklist when reviewing model-backed systems that make or influence security-relevant decisions.

## System role

- [ ] The model's decision is documented.
- [ ] The action caused by the model decision is documented.
- [ ] High-impact decisions are identified.
- [ ] False positive and false negative costs are understood.
- [ ] Human review requirements are defined.
- [ ] Policy decisions outside the model are documented.

## Input and inference robustness

- [ ] Attacker-controlled input fields are identified.
- [ ] Input normalization is defined.
- [ ] Feature extraction assumptions are documented.
- [ ] Boundary cases near thresholds are tested.
- [ ] Semantic-preserving input variations are tested.
- [ ] Obfuscation and formatting variations are tested where relevant.
- [ ] The system handles invalid, malformed, missing, and extreme inputs safely.

## Training data and poisoning

- [ ] Training data sources are documented.
- [ ] Data provenance is tracked.
- [ ] Labeling process is documented.
- [ ] Label quality checks exist.
- [ ] Untrusted feedback is separated from trusted labels.
- [ ] Retraining inputs can be quarantined.
- [ ] Poisoning tabletop scenarios have been reviewed.
- [ ] Backdoor or trigger-based behavior has been considered.

## Evaluation and testing

- [ ] Evaluation data is representative of expected production use.
- [ ] Evaluation includes adversarial and edge-case examples.
- [ ] Test data is protected from leakage and contamination.
- [ ] Model performance is measured across relevant subgroups and segments.
- [ ] Confidence scores are calibrated or treated cautiously.
- [ ] Thresholds are reviewed against business impact.
- [ ] Robustness testing is repeated before promotion.

## Deployment and fallback

- [ ] Model promotion has approval gates.
- [ ] Previous model versions can be restored.
- [ ] Safe fallback behavior is defined.
- [ ] Low-confidence cases have an escalation path.
- [ ] High-impact automated actions require policy checks or human approval.
- [ ] Emergency disable or degradation mode exists.

## Monitoring and drift

- [ ] Production input distribution is monitored.
- [ ] Prediction distribution is monitored.
- [ ] Confidence distribution is monitored.
- [ ] False positives and false negatives are tracked.
- [ ] Near-threshold decisions are monitored.
- [ ] Drift detection has owner and escalation criteria.
- [ ] Abuse patterns are monitored.
- [ ] Feedback-loop integrity is monitored.

## Incident response and recovery

- [ ] Model rollback process exists.
- [ ] Suspected poisoned data can be identified and quarantined.
- [ ] Retraining can be paused.
- [ ] Impacted decisions can be reviewed.
- [ ] Incident evidence is logged.
- [ ] Post-incident test cases are added to future evaluation.

## Residual risk

- [ ] Known model limitations are documented.
- [ ] Residual risk is explained to stakeholders.
- [ ] Assumptions are revisited periodically.
- [ ] Monitoring is aligned with known failure modes.
