# One-Week Course Runbook

This runbook converts the course into a practical 5-day / 40-hour delivery plan.

The goal is not to cover every file in the repository live. The goal is to give students a coherent security engineering experience: foundations, attack understanding, validated labs, concrete controls, reporting, and capstone.

## Day 1 — Foundations and ML Architecture

### Theme

ML Security is security engineering applied to systems where models, data, prompts, tools, and feedback loops become part of the attack surface.

### Modules

- Module 01 — Security Engineering for AI
- Module 02 — ML System Architecture
- Module 03 — OWASP ML Security Top 10
- Module 04 — BIML Architectural Risk Analysis

### Suggested agenda

| Time | Activity |
|---|---|
| 09:00–09:30 | Course opening, expectations, safety boundaries |
| 09:30–10:45 | Module 01: security engineering for AI |
| 10:45–11:00 | Break |
| 11:00–12:15 | Module 02: ML lifecycle and trust boundaries |
| 12:15–13:00 | Lunch |
| 13:00–14:15 | Exercise: ML lifecycle data-flow diagram |
| 14:15–14:30 | Break |
| 14:30–15:30 | Module 03: OWASP ML Top 10 as risk taxonomy |
| 15:30–16:30 | Module 04: BIML-style architecture review |
| 16:30–17:00 | Debrief: what changes when data becomes part of the program? |

### Deliverable

Students produce a simple AI system context diagram with assets, actors, trust boundaries, and three abuse cases.

### Instructor emphasis

Do not let Day 1 become abstract governance. Keep it grounded in concrete system components and security boundaries.

## Day 2 — LLM and RAG Application Security

### Theme

LLM and RAG risks are application-security problems with model-mediated behavior.

### Modules

- Module 05 — LLM Application Security
- Module 06 — RAG Security and Indirect Prompt Injection

### Suggested agenda

| Time | Activity |
|---|---|
| 09:00–09:30 | Review Day 1: model is not the security boundary |
| 09:30–10:45 | Module 05 deep dive: prompt injection and output/action separation |
| 10:45–11:00 | Break |
| 11:00–12:00 | DVAIA Module 05 walkthrough |
| 12:00–13:00 | Lunch |
| 13:00–14:15 | Module 06 deep dive: RAG trust boundaries |
| 14:15–14:30 | Break |
| 14:30–15:45 | DVAIA or BrokenPilot RAG/indirect injection exercise |
| 15:45–16:30 | Controls: retrieval authorization, source trust, citation validation |
| 16:30–17:00 | Student evidence log review |

### Deliverable

Students produce an evidence log for one LLM/RAG issue and a mitigation design that distinguishes weak mitigations from enforceable controls.

### Instructor emphasis

Keep repeating: retrieved content is untrusted input. The model cannot be the only component deciding whether retrieved content is authoritative.

## Day 3 — Agent Security and AI Supply Chain

### Theme

Once AI can act, the security problem becomes workflow security.

### Modules

- Module 07 — Agent and Tool Security
- Module 08 — Secure MLOps and AI Supply Chain

### Suggested agenda

| Time | Activity |
|---|---|
| 09:00–09:30 | Review Day 2: instruction/data confusion |
| 09:30–10:45 | Module 07 deep dive: tools, permissions, memory, approval gates |
| 10:45–11:00 | Break |
| 11:00–12:15 | BrokenPilot tool-confused-deputy validation |
| 12:15–13:00 | Lunch |
| 13:00–14:00 | BrokenPilot memory poisoning validation and layered controls |
| 14:00–14:15 | Break |
| 14:15–15:30 | Module 08: MLOps and AI supply chain |
| 15:30–16:30 | Exercise: executive supply-chain risk memo |
| 16:30–17:00 | Debrief: what controls belong outside the model? |

### Deliverable

Students produce a tool permission matrix or executive risk memo.

### Instructor emphasis

The model may propose. The system must decide and enforce.

## Day 4 — Privacy, Adversarial ML, and Red Team Reporting

### Theme

AI security testing must produce decision-grade evidence and implementable remediation.

### Modules

- Module 09 — Privacy Attacks and Data Protection
- Module 10 — Adversarial ML and Robustness
- Module 11 — AI Red Team Methodology

### Suggested agenda

| Time | Activity |
|---|---|
| 09:00–09:30 | Review Day 3: tool and memory boundaries |
| 09:30–10:30 | Module 09: privacy failure modes in AI systems |
| 10:30–10:45 | Break |
| 10:45–12:00 | Module 10: adversarial ML worked examples |
| 12:00–13:00 | Lunch |
| 13:00–14:15 | Module 11: AI red team methodology |
| 14:15–14:30 | Break |
| 14:30–15:30 | Finding rewrite classroom exercise |
| 15:30–16:15 | Evidence quality and remediation validation |
| 16:15–17:00 | Capstone briefing and team planning |

### Deliverable

Students rewrite a weak finding into a decision-grade finding with evidence, root cause, control, validation, and residual risk.

### Instructor emphasis

A screenshot of a jailbreak is not a finding. A finding needs impact, root cause, violated property, reproducibility, remediation, and validation.

## Day 5 — BrokenPilot Capstone

### Theme

Students perform a structured security assessment of a realistic internal AI agent.

### Module

- Module 12 — BrokenPilot Capstone

### Suggested agenda

| Time | Activity |
|---|---|
| 09:00–09:30 | Capstone scope, rules, deliverables |
| 09:30–10:45 | Architecture review and threat model |
| 10:45–11:00 | Break |
| 11:00–12:15 | Hands-on testing and evidence collection |
| 12:15–13:00 | Lunch |
| 13:00–14:15 | Remediation backlog and risk register |
| 14:15–14:30 | Break |
| 14:30–15:30 | Final report preparation |
| 15:30–16:30 | Student/team presentations |
| 16:30–17:00 | Instructor debrief and next steps |

### Deliverable

Students submit or present:

- threat model,
- evidence log,
- risk register,
- remediation backlog,
- executive summary,
- residual risk statement.

### Instructor emphasis

Reward students who produce implementable controls and validate fixes. Do not reward only exploit discovery.

## Compression options

If the class falls behind:

- reduce Module 03 to a taxonomy overview,
- assign Module 04 references as self-study,
- shorten Module 09 privacy coverage,
- use one Module 10 worked example instead of several,
- keep the BrokenPilot capstone intact.

## Expansion options

If the class moves quickly:

- add more DVAIA challenge variants,
- require students to implement or modify BrokenPilot controls,
- add a second executive memo,
- require a full red-team report instead of a short final report,
- include peer review of findings.
