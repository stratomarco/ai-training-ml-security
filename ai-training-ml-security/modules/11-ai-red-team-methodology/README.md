# Module 11 — AI Red Team Methodology

## Purpose

Create a repeatable, evidence-driven methodology for testing AI-enabled systems.

This module teaches students how to move from ad-hoc prompt hacking to structured AI red teaming: scope definition, rules of engagement, threat modeling, attack-path planning, controlled testing, evidence collection, risk scoring, mitigation design, executive communication, and residual-risk decisions.

## Key message

AI red teaming should produce engineering decisions, not only screenshots of jailbreaks.

A good AI red team engagement answers:

- what system was tested;
- what the model, application, tools, data, and infrastructure were allowed to do;
- what attackers could realistically influence;
- which controls failed;
- what evidence supports the finding;
- what risk the finding creates;
- what should change in the architecture, policy, monitoring, or workflow;
- what residual risk remains after mitigation.

## Learning objectives

By the end of this module, students should be able to:

1. Define the scope and rules of engagement for an AI red team exercise.
2. Distinguish model evaluation, application testing, infrastructure testing, and runtime behavior testing.
3. Build an attack plan from assets, trust boundaries, user roles, tools, data flows, and business impact.
4. Test LLM, RAG, agent, MLOps, privacy, and adversarial ML risks in a controlled environment.
5. Collect evidence without leaking real data or causing unsafe actions.
6. Map findings to OWASP, MITRE ATLAS, NIST AI RMF, BIML-style architecture risks, and classic security principles.
7. Score findings based on impact, exploitability, exposure, privilege, blast radius, and business context.
8. Write an AI red team report that developers, architects, and leadership can act on.
9. Explain red team limits, false confidence, and residual risk.
10. Translate red team results into a remediation roadmap.

## Topics

- AI red teaming goals and non-goals
- Scope and rules of engagement
- Safety boundaries and legal/ethical limits
- Model evaluation vs application security testing
- Infrastructure and supply chain assessment
- Runtime behavior and abuse testing
- Threat modeling before testing
- Attack-path planning
- Prompt injection testing
- RAG and indirect prompt injection testing
- Agent and tool-use testing
- Privacy and data leakage testing
- Model extraction and abuse testing
- Adversarial robustness testing
- Evidence collection
- Severity scoring
- Reporting
- Executive readout
- Remediation planning
- Residual risk

## Security engineering connection

AI red teaming is an extension of normal security assessment discipline:

| Security testing idea | AI red team equivalent |
|---|---|
| Scope and authorization | Define models, tools, data, environments, and allowed actions. |
| Threat modeling | Identify assets, trust boundaries, attacker goals, and abuse cases before testing. |
| Attack paths | Chain prompt injection, retrieval flaws, tool misuse, weak IAM, and logging gaps. |
| Evidence | Capture prompts, retrieved context, tool calls, logs, screenshots, and impact safely. |
| Severity | Score based on business impact, blast radius, privilege, exposure, and reproducibility. |
| Defense validation | Test whether guardrails, policy engines, permissions, approval gates, and monitoring work. |
| Reporting | Provide actionable remediation, owners, priority, and residual-risk language. |

## Methodology overview

```text
1. Mission and scope
   |
2. System understanding
   |
3. Threat model and attack plan
   |
4. Controlled testing
   |
5. Evidence and impact analysis
   |
6. Risk scoring and prioritization
   |
7. Remediation design
   |
8. Executive readout and residual risk
```

## Testing layers

| Layer | What to test |
|---|---|
| Model behavior | Harmful output, policy bypass, refusal gaps, robustness, memorization. |
| LLM application | Prompt injection, output handling, sensitive disclosure, model DoS, overreliance. |
| RAG pipeline | Indirect prompt injection, retrieval authorization, poisoned documents, source trust. |
| Agent workflow | Tool permissions, excessive agency, approval gates, memory poisoning, auditability. |
| MLOps supply chain | Datasets, notebooks, dependencies, model artifacts, registries, promotion gates. |
| Privacy | Prompt logs, traces, vector DB exposure, cross-tenant retrieval, retention and deletion. |
| Infrastructure | IAM, secrets, network egress, sandboxing, API controls, monitoring, incident response. |

## Lab

Use the labs in [`../../labs/ai-red-team-labs/`](../../labs/ai-red-team-labs/):

1. **AI red team scoping tabletop** — define scope, rules of engagement, assets, users, safety boundaries, and evidence requirements.
2. **BrokenPilot attack-chain lab** — plan and document a full attack chain against the BrokenPilot capstone design.

## Deliverable

Students produce an **AI red team report** that includes:

- scope and rules of engagement;
- system overview;
- threat model summary;
- attack plan;
- executed tests;
- findings;
- evidence;
- impact;
- risk score;
- remediation plan;
- detection opportunities;
- residual risk;
- executive summary.

## Instructor note

The goal is not to reward the most clever jailbreak. The goal is to reward disciplined security judgment.

A strong student submission explains why the system failed, where the control should live, what trade-off the mitigation creates, and what residual risk remains.
