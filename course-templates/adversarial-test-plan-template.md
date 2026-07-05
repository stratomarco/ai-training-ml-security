# Adversarial Test Plan Template

## 1. System overview

- System name:
- Business purpose:
- Model type:
- Model decision:
- Downstream action:
- Users:
- Owners:

## 2. Scope

### In scope

- Models:
- APIs:
- Data sources:
- Workflows:
- Environments:

### Out of scope

- Systems:
- Data:
- Attack types:
- Safety boundaries:

## 3. Assets and security properties

| Asset | Security property | Why it matters |
|---|---|---|
| | Confidentiality / integrity / availability / privacy / safety | |

## 4. Attacker model

| Attacker | Goal | Capability | Access |
|---|---|---|---|
| External user | | | |
| Insider | | | |
| Data contributor | | | |
| Feedback manipulator | | | |

## 5. Attacker control points

- Input fields:
- Metadata:
- Files or documents:
- Feedback:
- Labels:
- Training data:
- Model artifacts:
- Monitoring blind spots:

## 6. Evasion test cases

| Test case | Input variation | Expected behavior | Observed behavior | Severity |
|---|---|---|---|---|
| | | | | |

## 7. Poisoning and feedback-loop scenarios

| Scenario | Data/control point | Expected impact | Existing control | Gap |
|---|---|---|---|---|
| | | | | |

## 8. Backdoor or trigger review

| Trigger hypothesis | Source | Test approach | Result | Follow-up |
|---|---|---|---|---|
| | | | | |

## 9. Drift and distribution-shift scenarios

| Scenario | Assumption that changes | Impact | Monitoring signal | Response |
|---|---|---|---|---|
| | | | | |

## 10. Confidence and threshold review

- Thresholds:
- Calibration evidence:
- False positive cost:
- False negative cost:
- Low-confidence behavior:
- High-confidence/high-impact behavior:

## 11. Fallback behavior

| Failure condition | Fallback behavior | Owner | Evidence/logging |
|---|---|---|---|
| Low confidence | | | |
| Suspected drift | | | |
| Suspected poisoning | | | |
| Model unavailable | | | |
| High-impact decision | | | |

## 12. Monitoring and detection

| Signal | Why it matters | Threshold | Owner | Response |
|---|---|---|---|---|
| | | | | |

## 13. Mitigation plan

| Finding | Mitigation | Owner | Priority | Residual risk |
|---|---|---|---|---|
| | | | | |

## 14. Residual risk statement

Summarize what remains risky after reasonable controls.

Include:

- accepted assumptions;
- known limitations;
- monitoring dependency;
- required follow-up;
- decision owner.
