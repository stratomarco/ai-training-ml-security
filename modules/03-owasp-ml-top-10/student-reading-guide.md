# Student Reading Guide: Module 03: OWASP ML Security Top 10

## What this module is really about

This module turns OWASP categories into engineering judgment. The point is not to memorize a list. The point is to recognize when a failure is about input manipulation, poisoned data, model theft, output integrity, supply-chain weakness, or excessive agency, and then select the right control family.

## Question to keep in mind

Which failure mode is present, and what evidence would prove that the proposed control changes the security property?

## Decisions students must learn to make

- Map an observed behavior to a risk category without forcing a poor fit.
- Distinguish model-level attacks from application-level authorization failures.
- Decide whether a classifier can safely be used as a hard gate.
- Choose validation evidence for evasion, poisoning, extraction, and output integrity.

## Lab or exercise connection

Use the toy-classifier app for observable classical ML attacks. BrokenPilot is not the right target for these attacks. The graded artifact is a short attack-to-control mapping with test evidence and residual risk.

## What a strong submission looks like

A strong submission shows before and after behavior, explains why the naive fix is insufficient, and recommends whether the model should be advisory, gated, monitored, or backed by fallback review.

## Common misreadings to avoid

- Using BrokenPilot for classical ML attacks just because it is the main app.
- Reporting an evasion example without explaining the deployment decision it affects.
- Assuming accuracy is the same thing as security assurance.

## Exit ticket

Pick one OWASP ML category and write the smallest test that would demonstrate a control improving it.
