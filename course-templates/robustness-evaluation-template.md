# Robustness Evaluation Template

## System

- System name:
- Model:
- Version:
- Date:
- Evaluator:

## Model role

Describe what the model decides and what system behavior follows.

## Evaluation goals

- Normal performance:
- Adversarial behavior:
- Edge cases:
- Threshold behavior:
- Fallback behavior:

## Dataset and test set

| Dataset | Source | Sensitivity | Purpose | Trust level |
|---|---|---|---|---|
| | | | | |

## Test categories

| Category | Description | Included? | Notes |
|---|---|---|---|
| Ordinary validation | Expected examples | | |
| Boundary cases | Near decision thresholds | | |
| Semantic variations | Same meaning, different form | | |
| Formatting variations | Whitespace, punctuation, casing | | |
| Missing/malformed inputs | Invalid or incomplete data | | |
| Drift examples | New or shifted distribution | | |
| Abuse patterns | Repeated or suspicious inputs | | |
| Fallback tests | Low confidence or model failure | | |

## Results

| Test | Expected result | Actual result | Impact | Follow-up |
|---|---|---|---|---|
| | | | | |

## Threshold review

- Current thresholds:
- Calibration evidence:
- False positive impact:
- False negative impact:
- Recommended changes:

## Monitoring recommendations

- Input distribution:
- Prediction distribution:
- Confidence distribution:
- Segment-level performance:
- Abuse indicators:
- Drift indicators:

## Mitigations

| Gap | Recommendation | Priority | Owner |
|---|---|---|---|
| | | | |

## Residual risk

Document what remains uncertain or risky.
