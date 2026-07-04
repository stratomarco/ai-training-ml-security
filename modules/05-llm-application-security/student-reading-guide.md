# Student Reading Guide: Module 05: LLM Application Security

## What this module is really about

This module teaches the difference between text generation and authority. Prompt injection matters because untrusted text can be mistaken for instruction. Insecure output handling matters because model text can be passed into a downstream context that has different safety rules.

## Question to keep in mind

Where is untrusted text being treated as instruction or as safe output for another interpreter?

## Decisions students must learn to make

- Separate direct prompt injection from indirect prompt injection by entry point, not by root cause.
- Decide what the model is allowed to influence and what must be enforced outside the model.
- Choose output encoding or validation based on the downstream context.
- Reject controls that only make the prompt sound stricter.

## Lab or exercise connection

Use BrokenPilot for direct injection, indirect injection, and output handling. DVAIA can remain optional enrichment. The graded artifact should show vulnerable behavior, controlled behavior, the root cause, and a control that lives at the right boundary.

## What a strong submission looks like

A strong submission explains why marker detection is a teaching stand-in, then recommends instruction/data separation, privilege reduction, contextual output handling, and validation evidence.

## Common misreadings to avoid

- Thinking the attack is the specific marker string rather than the trust-boundary failure.
- Calling escaped output safe in every context.
- Treating prompt hardening as an authorization control.

## Exit ticket

Name one input boundary and one output boundary in the lab, then state the correct control for each.
