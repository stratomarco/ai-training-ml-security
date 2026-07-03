# Strong Example: Membership Inference and Model Inversion Risk Review

## Scope

The review covers a hypothetical customer-support model trained on support tickets. The concern is whether an attacker with query access could infer that a specific customer record was present in training data or recover sensitive fragments from model behavior.

## Evidence used

- The scenario gives an attacker repeated query access.
- The model is trained on support tickets that may contain names, account identifiers, and support history.
- No retention, minimization, or redaction control is described.
- No monitoring rule is described for repeated confidence-probing queries.

## Risk statement

If an external or internal user can repeatedly query a model trained on identifiable support tickets, they may infer membership of a target customer or recover sensitive fragments because training data minimization, output controls, and query monitoring are not defined.

## Naive fix that is not enough

A simple banner saying "do not reveal private data" is not enough. The failure is not only model behavior. It is a data-governance, access-control, and monitoring problem.

## Recommended controls

| Control | Owner | Validation |
|---|---|---|
| Remove direct identifiers before training | Data platform | Sample training data and verify redaction rules |
| Separate high-sensitivity tickets from general training | Data governance | Confirm dataset lineage excludes restricted classes |
| Rate-limit and monitor confidence-probing query patterns | Platform security | Replay repeated probing queries and confirm alerting |
| Reduce or avoid exposing raw confidence scores | ML platform | Confirm API contract returns calibrated bands or decisions only |
| Retain training-set lineage and approval evidence | ML governance | Review dataset card and approval record |

## Defense-in-depth

Data minimization reduces what can leak. Query monitoring catches abuse if minimization fails or if a sensitive fragment still enters training.

## Residual risk

Some membership signal can remain for rare or unique records. The residual risk should be accepted only for low-sensitivity datasets or after a documented privacy review.

## Decision

Pilot only. The system should not be broadly deployed until data minimization, dataset lineage, and query-abuse monitoring are implemented and tested.
