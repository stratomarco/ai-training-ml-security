# Strong Example: Poisoning and Backdoor Tabletop Review

## Scope

The review covers a training pipeline where new labeled examples can enter the training set through a semi-automated data collection process.

## Evidence used

- The scenario includes training data updates.
- Label quality is not independently reviewed.
- There is no described backdoor or outlier detection before promotion.
- Model release is based mainly on aggregate accuracy.

## Risk statement

If an attacker or compromised data source can introduce mislabeled or trigger-pattern examples into the training set, the model may learn an attacker-controlled behavior while still appearing healthy on aggregate metrics.

## Naive fix that is not enough

Relying only on overall test accuracy is not enough. A backdoored model can retain high aggregate accuracy while failing on trigger-specific or subgroup-specific cases.

## Recommended controls

| Control | Owner | Validation |
|---|---|---|
| Dataset provenance for every training batch | Data platform | Reject records without source and collection metadata |
| Label review for high-impact classes | ML team | Sample labels and measure disagreement rate |
| Trigger and outlier analysis before release | ML security | Run canary trigger tests and nearest-neighbor review |
| Segment-level evaluation, not only aggregate accuracy | ML platform | Compare class, source, and subgroup metrics |
| Promotion gate requiring signed dataset and model manifest | MLOps | Verify manifest before registry promotion |

## Defense-in-depth

Provenance controls reduce the chance of poisoning. Segment-level and trigger-specific testing detect failures that pass aggregate evaluation.

## Residual risk

Novel triggers may not be detected. The release should include monitoring for distribution shift and an emergency rollback path.

## Decision

Approve with conditions. Promotion should be blocked until provenance and segment-level evaluation are enforced.
