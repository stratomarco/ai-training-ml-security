# Weak Threat Model Example  -  BrokenPilot

## Summary

BrokenPilot uses AI to help with tickets and documents. The main risk is that users can hack the AI with prompt injection.

## Assets

- Tickets
- Documents
- AI

## Threats

- Prompt injection
- Data leak
- Bad output

## Mitigations

- Add guardrails
- Use better prompts
- Monitor the system

## Why this is weak

This threat model is too vague.

Problems:

- It does not identify trust boundaries.
- It does not explain who the attacker is.
- It does not distinguish user input from retrieved content.
- It does not identify which tools are sensitive.
- It does not define what "guardrails" means.
- It does not specify where controls are enforced.
- It does not discuss residual risk.

A better submission should describe concrete attack paths, root causes, impact, and enforceable controls.
