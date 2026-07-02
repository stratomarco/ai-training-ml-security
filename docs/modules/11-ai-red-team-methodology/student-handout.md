# Module 11 Student Handout — AI Red Team Methodology

## Core idea

AI red teaming is structured security testing for AI-enabled systems.

The goal is not only to make a model produce a bad answer. The goal is to understand whether an adversary can cause an unsafe, unauthorized, privacy-violating, costly, or misleading outcome in the real system.

## AI red team workflow

```text
1. Define mission and scope
2. Understand the system
3. Identify assets and trust boundaries
4. Build threat model and abuse cases
5. Plan attack paths
6. Execute controlled tests
7. Capture evidence
8. Analyze impact and root cause
9. Score severity
10. Recommend mitigations
11. Communicate residual risk
```

## What to include in scope

An AI system may include:

- user interface;
- API gateway;
- LLM provider or local model;
- prompts and system instructions;
- retrieval pipeline;
- vector database;
- tools and function calls;
- memory;
- logs and traces;
- model registry;
- datasets;
- notebooks;
- deployment platform;
- identities and permissions;
- approval workflows;
- business decisions.

## Testing categories

| Category | Example questions |
|---|---|
| LLM application | Can user input override intended behavior? Is output handled safely? |
| RAG | Can malicious documents influence answers or tool calls? Is retrieval authorized? |
| Agent/tool use | Can the model trigger unauthorized actions? Are approval gates enforced? |
| Privacy | Can the system leak prompts, retrieved context, memory, logs, or tenant data? |
| MLOps | Can data, model artifacts, dependencies, or registries be tampered with? |
| Robustness | Can inputs evade, skew, poison, or degrade the model? |
| Infrastructure | Are IAM, secrets, network egress, sandboxing, and logs sufficient? |

## Rules of engagement checklist

Before testing, define:

- systems in scope;
- systems out of scope;
- test environment;
- allowed accounts and roles;
- allowed data;
- forbidden actions;
- rate limits;
- tool-use restrictions;
- evidence rules;
- escalation contacts;
- stop conditions.

## Finding quality checklist

A good finding has:

- clear title;
- affected component;
- security property violated;
- prerequisites;
- attack path;
- evidence;
- impact;
- root cause;
- severity;
- recommended fixes;
- detection opportunities;
- residual risk.

## Severity thinking

Do not score based only on prompt complexity.

Consider:

- data sensitivity;
- user privilege required;
- attacker control;
- reproducibility;
- business impact;
- blast radius;
- automation potential;
- detectability;
- compensating controls.

## Common mitigation patterns

| Risk | Common controls |
|---|---|
| Prompt injection | Limit blast radius, treat model output as untrusted, enforce policy outside the model. |
| RAG poisoning | Retrieval authorization, source trust, document provenance, context labeling. |
| Tool misuse | Least-privilege tools, per-action authorization, approval gates, audit logs. |
| Sensitive disclosure | Data minimization, access control, logging controls, redaction, tenant isolation. |
| Model DoS | Token budgets, rate limits, timeouts, circuit breakers, cost monitoring. |
| Supply chain | Provenance, signing, registry access control, safe artifact loading, promotion gates. |
| Overreliance | Human review, confidence communication, fallback behavior, decision limits. |

## Final reminder

A prompt may trigger the exploit, but the root cause is often architectural.

Always ask:

> What control should have prevented this even if the model was confused?

## Finding rewrite practice

This module includes [`exercise-finding-rewrite.md`](exercise-finding-rewrite.md), a short exercise where students rewrite a weak AI security finding into a decision-grade finding with evidence, root cause, implementable control, validation, and residual risk. Use it before the BrokenPilot capstone to improve report quality.
