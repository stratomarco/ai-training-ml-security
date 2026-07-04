# Student Reading Guide: Module 01: Security Engineering for AI

## What this module is really about

Students often enter AI security by looking for AI-specific tricks. This module resets the frame: AI systems still fail through assets, trust boundaries, incentives, confused authority, weak defaults, and missing assurance. The AI part changes the shape of uncertainty, but it does not remove the need for security engineering.

## Question to keep in mind

What security property is at risk, who can influence the system, and where should enforcement live?

## Decisions students must learn to make

- Separate model behavior from system authority.
- Choose security properties that can be validated, not slogans such as safe or aligned.
- Decide which risks belong in architecture, policy, monitoring, or user training.
- Explain why usability and developer velocity matter to whether a control survives production.

## Lab or exercise connection

Use the module exercise to turn a vague AI concern into assets, trust boundaries, abuse cases, controls, validation evidence, and residual risk. This is a reasoning lab. The graded artifact is the security argument, not a running exploit.

## What a strong submission looks like

A strong submission names the security property, explains the root cause, chooses controls that enforce that property, and states what evidence would change the decision.

## Common misreadings to avoid

- Treating AI security as prompt wording instead of system design.
- Listing frameworks without using them to make a decision.
- Assuming the model can enforce permissions that the application did not enforce.

## Exit ticket

Write one sentence that starts with: The model may suggest, but the system must...
