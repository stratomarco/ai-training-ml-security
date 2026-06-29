# Module 11 Slides — AI Red Team Methodology

## Slide 1 — Title

# AI Red Team Methodology

From prompt hacking to structured security testing.

---

## Slide 2 — The core problem

Many AI security tests stop at:

> “I got the model to say something bad.”

That is not enough.

A useful AI red team exercise must explain:

- what failed;
- why it failed;
- what security property was violated;
- what business impact exists;
- what control should change;
- what risk remains.

---

## Slide 3 — Key message

# AI red teaming should produce engineering decisions, not only screenshots.

The output should help teams decide:

- what to fix;
- what to monitor;
- what to restrict;
- what to approve manually;
- what not to automate;
- what risk to accept.

---

## Slide 4 — AI red teaming is not one thing

AI red teaming can include:

- model evaluation;
- LLM application security testing;
- RAG testing;
- agent and tool testing;
- privacy testing;
- adversarial ML testing;
- infrastructure review;
- supply chain review;
- governance and process review.

---

## Slide 5 — OWASP GenAI red team framing

A useful GenAI red team program should be holistic.

It should consider:

- model behavior;
- implementation security;
- infrastructure exposure;
- runtime behavior.

Do not test the model in isolation when the real risk is created by tools, documents, permissions, memory, and workflows.

---

## Slide 6 — Red team vs evaluation vs pentest

| Activity | Main question |
|---|---|
| Model evaluation | Does the model behave acceptably under defined tests? |
| AppSec testing | Does the application enforce security properties? |
| Infrastructure assessment | Are platforms, secrets, IAM, and networks secure? |
| AI red teaming | Can realistic adversaries cause unsafe or unauthorized outcomes across the full system? |

---

## Slide 7 — The system is the target

An AI system includes:

- users;
- prompts;
- models;
- tools;
- APIs;
- data sources;
- vector databases;
- documents;
- memory;
- logs;
- monitoring;
- identity;
- approval workflows;
- business processes.

The model is only one component.

---

## Slide 8 — Methodology overview

```text
1. Mission and scope
2. System understanding
3. Threat model
4. Attack planning
5. Controlled testing
6. Evidence collection
7. Impact and severity
8. Remediation design
9. Executive readout
10. Residual risk
```

---

## Slide 9 — Step 1: mission and scope

Define:

- why the test is happening;
- what systems are in scope;
- what systems are out of scope;
- what data can be used;
- what actions are allowed;
- what safety limits exist;
- when to stop testing;
- who approves exceptions.

No scope, no red team.

---

## Slide 10 — Rules of engagement

Rules of engagement should define:

- approved environments;
- approved accounts;
- rate limits;
- allowed payload classes;
- forbidden actions;
- data handling rules;
- evidence requirements;
- escalation contacts;
- emergency stop conditions.

---

## Slide 11 — Safety boundaries

AI red team exercises must avoid:

- real customer data exposure;
- uncontrolled destructive actions;
- unauthorized system access;
- live phishing or social engineering outside scope;
- persistence in production;
- unsafe automated actions;
- bypassing legal or policy limits.

Use local labs, staging, fake data, and approval gates.

---

## Slide 12 — Step 2: understand the system

Before testing, capture:

- architecture;
- data flows;
- trust boundaries;
- user roles;
- model role;
- tool permissions;
- retrieval sources;
- memory behavior;
- logging and monitoring;
- deployment and rollback process.

Testing without architecture becomes random guessing.

---

## Slide 13 — Step 3: threat model

Ask:

- What assets matter?
- Who can influence inputs?
- Who can add documents?
- Who can trigger tools?
- What can the model see?
- What can the model cause?
- What is the blast radius of a bad output?
- What decisions rely on the model?

---

## Slide 14 — Step 4: attack-path planning

An attack path chains conditions:

```text
attacker controls input
  -> model follows attacker instruction
  -> retrieved context is overbroad
  -> tool executes without independent authorization
  -> sensitive ticket is modified
  -> logs do not capture enough evidence
```

Single findings matter. Attack chains reveal system risk.

---

## Slide 15 — Test categories

| Category | Examples |
|---|---|
| Prompt injection | direct, indirect, hidden instructions |
| RAG | poisoned documents, cross-tenant retrieval, source confusion |
| Agent | tool misuse, memory poisoning, excessive agency |
| Privacy | sensitive disclosure, log leakage, training-data extraction |
| MLOps | unsafe artifacts, weak registry controls, poisoned data |
| Robustness | evasion, poisoning, backdoors, drift |
| Infrastructure | IAM, secrets, egress, sandboxing |

---

## Slide 16 — Prompt injection testing

Test whether attacker-controlled instructions can:

- override developer intent;
- expose hidden context;
- change output policy;
- cause unsafe formatting;
- influence tool calls;
- persist through memory;
- manipulate downstream systems.

But remember: prompt injection impact depends on what the system can access or do.

---

## Slide 17 — RAG testing

Test whether malicious or unauthorized content can:

- be retrieved;
- outrank trusted content;
- inject instructions;
- leak documents across tenants;
- confuse citation/source trust;
- cause the model to reveal hidden context;
- manipulate business decisions.

---

## Slide 18 — Agent testing

Test whether the agent can:

- call tools without independent authorization;
- exceed user intent;
- perform destructive actions without approval;
- use stale or poisoned memory;
- chain actions unexpectedly;
- leak data through tools;
- operate without sufficient logs.

---

## Slide 19 — Privacy testing

Test whether the system leaks:

- prompt content;
- completion content;
- retrieved documents;
- vector DB metadata;
- hidden context;
- memory;
- training examples;
- cross-tenant data;
- internal system instructions.

---

## Slide 20 — Supply chain testing

Review:

- datasets;
- labels;
- notebooks;
- dependencies;
- model files;
- adapters;
- prompts;
- vector indexes;
- registries;
- promotion gates;
- rollback process.

A compromised model artifact is a supply chain incident.

---

## Slide 21 — Runtime behavior testing

Observe:

- tool-call traces;
- retrieval traces;
- policy decisions;
- refusal behavior;
- rate-limit behavior;
- fallback behavior;
- approval events;
- monitoring alerts;
- audit logs.

If it is not observable, it is hard to defend.

---

## Slide 22 — Evidence collection

Good evidence includes:

- exact test objective;
- account and role used;
- prompt/input;
- retrieved context;
- model output;
- tool-call request and response;
- logs or traces;
- screenshot or transcript;
- impact explanation;
- reproduction steps;
- safety notes.

---

## Slide 23 — Severity scoring

Score based on:

- asset sensitivity;
- privilege required;
- attacker control;
- reproducibility;
- business impact;
- blast radius;
- automation potential;
- detectability;
- available compensating controls.

Do not score only on how clever the prompt is.

---

## Slide 24 — Finding structure

Each finding should include:

- title;
- summary;
- affected component;
- security property violated;
- attack path;
- evidence;
- impact;
- root cause;
- severity;
- remediation;
- detection opportunity;
- residual risk.

---

## Slide 25 — Common weak reports

Weak reports say:

- “The model was jailbroken.”
- “The prompt was bypassed.”
- “The answer was bad.”

Strong reports say:

- “An untrusted retrieved document caused the assistant to call a ticket-update tool without independent authorization, modifying a restricted incident record.”

---

## Slide 26 — Remediation design

Common mitigations:

- least-privilege tools;
- per-action authorization;
- policy outside the model;
- retrieval authorization;
- source trust and provenance;
- output encoding and validation;
- approval gates;
- sandboxing;
- rate limits and budgets;
- monitoring and audit trails;
- incident response and rollback.

---

## Slide 27 — Residual risk

After mitigation, ask:

- Can prompt injection still influence text?
- Can it cause unauthorized action?
- Can it access sensitive data?
- Can it persist?
- Can it be detected?
- Is human review required?
- Is the use case appropriate for an LLM or agent?

---

## Slide 28 — Executive readout

Leadership needs:

- what was tested;
- what matters most;
- what could happen;
- likelihood and exposure;
- business impact;
- remediation priorities;
- decisions needed;
- residual risk.

Avoid hype. Avoid minimization.

---

## Slide 29 — BrokenPilot attack-chain example

```text
malicious runbook inserted
  -> RAG retrieves it
  -> assistant follows hidden instruction
  -> assistant calls ticket update tool
  -> no per-action authorization
  -> restricted incident is modified
  -> logs show only final natural language summary
```

The finding is not “prompt injection.”

The finding is an authorization and workflow-control failure triggered through prompt injection.

---

## Slide 30 — Closing principle

# Red teaming is a feedback loop into secure design.

A mature AI red team program improves:

- architecture;
- controls;
- developer guidance;
- monitoring;
- incident response;
- governance;
- business risk decisions.
