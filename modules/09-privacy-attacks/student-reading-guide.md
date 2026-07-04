# Student Reading Guide: Module 09: Privacy Attacks and Data Protection

## What this module is really about

Privacy and security failures in AI systems often come from data exposure paths: retrieval leakage, logs, overbroad access, training data memorization, or inference about membership and sensitive attributes. This module keeps privacy concrete by tying each failure to data handling and access decisions.

## Question to keep in mind

What personal or sensitive information can be inferred, retrieved, logged, or reconstructed, and who can access it?

## Decisions students must learn to make

- Distinguish cross-tenant retrieval leakage from model memorization and membership inference.
- Decide which privacy failures can be demonstrated runnably and which are better reviewed as tabletop risks.
- Choose minimization, authorization, logging, retention, and monitoring controls.
- State residual risk honestly when privacy cannot be reduced to zero.

## Lab or exercise connection

Use BrokenPilot for cross-tenant privacy leakage. Use the membership-inference tabletop for reasoning about privacy attacks that should not be forced into the LLM app.

## What a strong submission looks like

A strong submission shows the leaked fake fragment, proves retrieval authorization changes the privacy property, then discusses secondary leakage through logs and operational access.

## Common misreadings to avoid

- Calling fake training secrets harmless and missing the real privacy property.
- Fixing answer filtering while leaving restricted context retrievable.
- Ignoring logs as a second data exposure surface.

## Exit ticket

Explain how retrieval authorization and log minimization protect different privacy surfaces.
