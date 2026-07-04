# Student Reading Guide: Module 10: Adversarial ML and Robustness

## What this module is really about

This module teaches students not to confuse benchmark accuracy with security assurance. Robustness is about behavior under stress, manipulation, drift, and uncertainty. The engineering decision is often whether a model can safely act as a hard gate.

## Question to keep in mind

What happens when inputs, labels, thresholds, or operating conditions shift away from the clean validation set?

## Decisions students must learn to make

- Design tests for evasion, poisoning, threshold tampering, and drift.
- Decide when a classifier should be advisory rather than authoritative.
- Choose fallback behavior when confidence, input quality, or distribution is questionable.
- Explain why a single evasion example is evidence of a class of risk, not the whole risk story.

## Lab or exercise connection

Use the toy-classifier app for observable evasion and poisoning. Keep poisoning/backdoor tabletop work as reasoning where the question is control design and residual risk.

## What a strong submission looks like

A strong submission reports before and after behavior, explains the deployment implication, and recommends monitoring, fallback, retraining controls, and validation tests.

## Common misreadings to avoid

- Treating word swaps as a magic trick instead of a proxy for input manipulation risk.
- Reporting confidence scores without tying them to an operational decision.
- Assuming retraining alone fixes poisoning risk.

## Exit ticket

State whether the toy classifier should be a hard authorization gate, and justify the answer.
