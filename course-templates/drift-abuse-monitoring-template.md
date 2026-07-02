# Drift and Abuse Monitoring Template

## System overview

- System:
- Model:
- Version:
- Owner:
- Business process:

## Monitoring objectives

- Detect model quality degradation.
- Detect attacker adaptation or abuse.
- Detect distribution shift.
- Detect feedback-loop manipulation.
- Trigger safe fallback or human review.

## Key model decisions

| Decision | Downstream action | Impact if wrong |
|---|---|---|
| | | |

## Monitoring signals

| Signal | Description | Why it matters | Owner |
|---|---|---|---|
| Input distribution | | Detect changed inputs | |
| Prediction distribution | | Detect label skew | |
| Confidence distribution | | Detect uncertainty shifts | |
| Segment performance | | Detect targeted degradation | |
| Feedback volume | | Detect feedback abuse | |
| Label disagreement | | Detect label quality issues | |
| Near-threshold decisions | | Detect boundary probing | |
| False positives | | Measure business harm | |
| False negatives | | Measure missed abuse | |

## Alert criteria

| Condition | Severity | Action | Owner |
|---|---|---|---|
| | | | |

## Response playbook

### Suspected evasion

- Increase sampling for human review.
- Capture examples.
- Add cases to adversarial evaluation.
- Review thresholds and features.

### Suspected poisoning

- Pause retraining if needed.
- Quarantine suspected data.
- Review provenance and labels.
- Roll back model if needed.

### Suspected drift

- Compare production data to evaluation data.
- Evaluate recent model performance.
- Adjust fallback or human review.
- Plan retraining from trusted data.

### Suspected backdoor

- Search for trigger patterns.
- Review data provenance.
- Evaluate model variants.
- Roll back or quarantine model if required.

## Recovery requirements

- Known-good model version:
- Rollback owner:
- Data quarantine process:
- Retraining approval:
- Communication owner:

## Residual risk

Summarize remaining monitoring limitations and accepted risk.
