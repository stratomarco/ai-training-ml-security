# Controls and remediations: Adversarial ML and robustness

## Control objective

The goal is not to make the model unbreakable. The goal is to prevent model brittleness from becoming silent unsafe behavior.

## Strong controls by failure mode

### Evasion

- Add adversarial and perturbation testing to evaluation.
- Monitor feature distributions and unusual input patterns.
- Use confidence thresholds and abstention for uncertain cases.
- Route high-impact or low-confidence cases to fallback review.
- Avoid using a single model as the only authorization or safety gate.

Validation: run known perturbation cases and confirm they are detected, abstained, or routed for review rather than silently accepted.

### Poisoning

- Version datasets and labels.
- Restrict write access to training data and labels.
- Review label changes for high-impact classes.
- Compare behavior before and after retraining on fixed evaluation slices.
- Use canary examples to detect unexpected boundary movement.

Validation: inject a small controlled label-flip test in a non-production dataset and confirm review gates catch behavior changes.

### Extraction

- Limit query rates and high-volume probing.
- Avoid exposing unnecessary confidence scores.
- Monitor systematic boundary exploration.
- Consider model access tiering for sensitive decision models.

Validation: run a query harness and confirm monitoring detects repeated boundary-probing patterns.

### Output integrity

- Version thresholds and serving configuration.
- Require review for threshold changes.
- Bind threshold changes to evaluation reports.
- Log the score, threshold, and decision for audit.
- Alert on threshold changes in production.

Validation: change a threshold in staging and confirm the promotion process requires approval and records the impact.

## Weak controls

- Claiming the model is safe because test accuracy is high.
- Adding a warning banner without changing decision handling.
- Blocking a few known words and calling it adversarial robustness.
- Hiding confidence scores while allowing unlimited probing.
- Reviewing the model file but ignoring serving thresholds.

## Remediation backlog language

Good backlog items are specific:

- Add an adversarial evaluation slice for message perturbations before release.
- Add an abstain state when confidence falls between 0.45 and 0.65.
- Require approval for threshold changes and store the approval with the deployment record.
- Add dataset hash and label-change summary to every training run.
- Add monitoring for repeated queries that differ by one or two tokens.

## Residual risk

Adversarial testing samples possible attacks. It does not cover every future input. The residual-risk statement should explain what the model is still allowed to decide, where fallback exists, and what monitoring will detect when assumptions fail.
