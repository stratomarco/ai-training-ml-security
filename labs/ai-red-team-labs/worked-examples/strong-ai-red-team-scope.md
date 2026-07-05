# Strong Example: AI Red Team Scope

## Objective

Assess whether the AI assistant can cause unauthorized disclosure, unsafe tool use, or misleading operational decisions across LLM, RAG, memory, and tool boundaries.

## In scope

- direct prompt injection through user input
- indirect prompt injection through retrieved documents
- retrieval authorization boundaries
- tool authorization and approval gates
- memory poisoning and memory isolation
- auditability of proposed and executed actions

## Out of scope

- real customer data
- production systems
- destructive testing
- persistence outside the local training environment
- bypass attempts against third-party services

## Rules of engagement

Use only the local training app and fake seed data. Do not target external systems. Capture evidence with request, response, control state, and expected security property.

## Success criteria

A finding is valid only if it includes evidence, root cause, control recommendation, validation method, and residual risk.

## Defense-in-depth target

At least one test must show that one compromised layer does not automatically compromise execution. Example: poisoned memory may influence intent, but tool authorization should block cross-tenant action.

## Final deliverable

The team will produce a red-team report with prioritized findings, one rewritten strong finding, and a leadership recommendation: approve, pilot, delay, or reject.
