# Lab Quality Standard

This course uses two different lab classes. They should not be judged by the same mechanism.

Attack labs are runnable or observable labs. Students should see a broken behavior, enable or design a control, and then observe the security property change.

Reasoning labs are design, review, scoping, or tabletop labs. They may not have a process to run. They are judged by the quality of the engineering decision, the evidence used, and the control validation plan.

## Six bars for a good lab

1. Observable failure and observable fix when the lab is an attack lab.
2. The fix is the graded artifact, not the exploit.
3. The naive fix is discussed and rejected when it would not work.
4. At least one defense-in-depth moment is identified.
5. The lab maps to a real engineering decision.
6. The lab is deterministic, resettable, or graded with anchors.

## Required student deliverable

Every lab should end in one of the following artifacts:

- architecture risk review
- permission matrix
- retrieval authorization policy
- output handling control note
- privacy risk assessment
- MLOps evidence review
- red-team scope
- red-team finding
- residual-risk decision

A lab is not complete when the student only proves that something can break. It is complete when the student explains the root cause, proposes a control, validates the control, and states residual risk.

## Strong submission pattern

A strong submission contains:

- clear scope and assumption boundaries
- concrete evidence from the target, artifact pack, or scenario
- root cause in security-engineering language
- weak or naive fixes that were rejected
- implementable control recommendation
- validation method
- residual risk
- owner and priority

## Weak submission pattern

A weak submission usually contains:

- vague claims such as "add guardrails" or "improve security"
- no evidence
- no target object, trust boundary, or asset
- no validation step
- no residual-risk statement
- no decision for engineering or leadership
