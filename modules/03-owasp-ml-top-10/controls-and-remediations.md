# Controls and Remediations: OWASP ML Security Top 10

## Control objective

Use OWASP ML categories to select concrete controls for the system under review. Do not stop at category mapping.

## Control families

### Data controls

Data provenance, source trust, dataset versioning, label review, dataset hashing, schema validation, and retention rules reduce poisoning, privacy, and supply-chain risk.

### Model controls

Evaluation, adversarial testing, robustness checks, confidence calibration, fallback behavior, and model versioning reduce unsafe reliance on brittle behavior.

### Application controls

Authentication, authorization, retrieval filters, output validation, tool brokers, rate limits, and audit logs prevent model behavior from becoming unauthorized system impact.

### Pipeline controls

Dependency lockfiles, artifact digests, signed releases, promotion gates, registry policy, and rollback procedures protect training and deployment.

### Monitoring controls

Runtime monitoring, drift detection, abuse signals, extraction indicators, privacy alerts, and control regression tests help detect failures after release.

## Weak remediations

"Retrain the model" is not enough if the root cause is missing authorization or weak artifact promotion.

"Add guardrails" is not enough without specifying where enforcement happens.

"Add more data" is not enough if the data source can be poisoned.

"Improve accuracy" is not enough if the system uses the output as a hard security gate.

## Strong remediation examples

For input manipulation: add adversarial evaluation, confidence threshold, secondary review for uncertain cases, and avoid using the classifier as the only authorization control.

For poisoning: add source allowlists, dataset diffs, label review, training run approvals, and rollback to known-good datasets.

For extraction: reduce score detail, limit query rate, monitor probing patterns, and protect artifacts.

For output integrity: sign threshold configuration, require review for decision-policy changes, and monitor decision distribution.

For supply chain: require dataset hash, dependency lockfile, artifact digest, approval, registry metadata, and rollback plan before promotion.

## Validation

A remediation is credible only if it has a validation method. The validation should recreate the failure and show that the control changes the security property.

In the toy-classifier lab, evasion should flip a label before controls are discussed, and the mitigation discussion should focus on whether the classifier can safely be a hard gate.

In the MLOps evidence pack, the artifact should be blocked because provenance and integrity evidence are missing or inconsistent.

In BrokenPilot, prompt injection should not bypass output handling, retrieval authorization, or tool authorization.

## Residual risk

Even with category-specific controls, residual risk remains where model behavior is probabilistic, monitoring coverage is incomplete, or humans must interpret uncertain cases. The risk register should state which categories remain partially mitigated and what evidence would trigger re-evaluation.
