# Adversarial ML Labs

These labs support Module 10  -  Adversarial ML and Robustness.

The goal is to teach practical robustness thinking in controlled, fake-data environments.

## Labs

| Lab | Purpose |
|---|---|
| [`evasion-robustness-lab.md`](evasion-robustness-lab.md) | Demonstrate how a toy classifier can be bypassed with controlled input variations, then design mitigations. |
| [`poisoning-backdoor-tabletop.md`](poisoning-backdoor-tabletop.md) | Tabletop review of poisoned training data, feedback-loop abuse, and trigger-based model behavior. |

## Lab philosophy

These labs should not be used against real systems.

Students should focus on:

- model role;
- attacker goals;
- attacker control points;
- root cause;
- monitoring;
- fallback;
- mitigation;
- residual risk.

<!-- LAB_QUALITY_STANDARD_ADVERSARIAL_ANCHORS:START -->
## Worked examples

Use the poisoning and backdoor worked examples to calibrate tabletop grading:

- `worked-examples/strong-poisoning-backdoor-tabletop.md`
- `worked-examples/weak-poisoning-backdoor-tabletop.md`

The evasion lab is backed by the toy-classifier app. The poisoning and backdoor tabletop remains a reasoning lab unless a future runnable target is added.
<!-- LAB_QUALITY_STANDARD_ADVERSARIAL_ANCHORS:END -->
