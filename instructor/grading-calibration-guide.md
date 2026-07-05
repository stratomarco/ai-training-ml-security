# Instructor Grading Calibration Guide

This guide helps instructors grade the BrokenPilot capstone and related Module 07 exercises consistently.

The course now includes strong and weak examples for major BrokenPilot deliverables. These examples should be used before grading live student work so instructors share a common understanding of what "good" looks like.

## Why grading calibration matters

AI security work is easy to grade inconsistently.

Two students may both identify prompt injection, tool misuse, or memory poisoning, but one may provide a shallow description while the other explains the violated security property, the affected asset, the root cause, the exploit evidence, the control design, and the residual risk.

The goal of this course is not to reward students for merely naming vulnerabilities. The goal is to reward complete security reasoning.

Good submissions should show that students can:

- identify the relevant trust boundary;
- connect the issue to a security property such as authorization, integrity, confidentiality, availability, or auditability;
- provide evidence, not just claims;
- explain root cause in system terms;
- design implementable controls;
- validate whether the control works;
- communicate risk to developers and leadership;
- describe residual risk honestly.

## Calibration workflow

Before grading a cohort, instructors should complete this short calibration sequence.

1. Read the BrokenPilot scenario and architecture.
2. Review the grading rubric.
3. Read one strong and one weak example for each deliverable type.
4. Score the examples independently.
5. Compare scores with another instructor or against the scoring anchors below.
6. Agree on what evidence is required for full credit.
7. Grade student submissions using the same anchors.

If there is only one instructor, perform the same process alone and write down scoring decisions before reading student submissions.

## Deliverables to calibrate

| Deliverable | Strong example | Weak example | Primary grading question |
|---|---|---|---|
| Threat model | Strong threat model | Weak threat model | Did the student identify real assets, trust boundaries, actors, and abuse cases? |
| Risk register | Strong risk register | Weak risk register | Did the student describe impact, likelihood, owner, mitigation, and residual risk? |
| Tool permission matrix | Strong tool permission matrix | Weak tool permission matrix | Did the student specify concrete permissions and enforcement points? |
| Evidence log | Strong evidence log | Weak evidence log | Did the student collect reproducible, decision-grade evidence? |
| Remediation backlog | Strong remediation backlog | Weak remediation backlog | Did the student create implementable engineering work? |
| Executive readout | Strong executive readout | Weak executive readout | Did the student communicate business risk without hype? |

## Scoring anchors

Use a four-level scoring model.

| Score | Meaning | Characteristics |
|---|---|---|
| 4 | Strong | Specific, evidence-based, implementable, tied to architecture and residual risk |
| 3 | Acceptable | Mostly correct, some evidence, reasonable mitigations, minor gaps |
| 2 | Weak | Names the issue but lacks root cause, impact, or implementable controls |
| 1 | Insufficient | Generic, inaccurate, unsupported, or not tied to the system |

## What a strong submission looks like

A strong submission does not need to be long. It needs to be precise.

For example, a strong finding about tool misuse should include:

- the user identity used in the test;
- the target object;
- both tenants or authorization domains;
- the exact request or UI action;
- the observed result;
- the violated security property;
- the root cause;
- the control that should prevent the issue;
- how the control was validated;
- residual risk.

A strong finding would say something like:

> Alice is an `ops` user in tenant `alpha`. She can update ticket `TCK-2001`, which belongs to tenant `beta`, through the tool endpoint when `ENABLE_TOOL_AUTHZ=false`. The tool layer accepts the model/user-provided ticket ID and does not perform object-level authorization. Enabling `ENABLE_TOOL_AUTHZ=true` blocks the same request with `tool_authorization_denied`. The root cause is missing complete mediation at the tool execution boundary.

A weak finding would say:

> The agent can update tickets it should not update. Add access control.

The weak finding names the general issue, but it does not provide enough evidence or implementation detail to support remediation.

## Concrete-control grading

This course should reward students for producing controls that engineers could implement.

A control is strong when it answers:

- Where is the control enforced?
- What inputs does it evaluate?
- What decision does it make?
- What happens when the decision is deny?
- What gets logged?
- How is the control tested?
- What failure modes remain?

For example, "add authorization" is too vague.

A stronger control statement is:

> Before executing `update_ticket`, the tool service must load the authenticated user and the target ticket, compare `user.tenant` to `ticket.tenant`, verify that `user.role` is allowed to perform the requested action, deny by default on missing metadata, and log the user ID, ticket ID, decision, reason, and request correlation ID. The LLM is not allowed to decide authorization.

## Evidence grading

Evidence should be reproducible.

A strong evidence log includes:

- timestamp or test sequence;
- environment and relevant control settings;
- request or prompt used;
- response or screenshot summary;
- expected vs observed result;
- security meaning;
- affected asset;
- link to finding or risk-register entry.

Evidence is weak when it only says:

- "jailbreak worked";
- "the model leaked data";
- "authorization failed";
- "see screenshot" without context;
- "the agent did something bad".

The evidence must help another instructor, engineer, or reviewer reproduce and understand the issue.

## Common grading mistakes

Avoid these mistakes:

1. Rewarding exploit novelty over security reasoning.
2. Giving full credit for naming an OWASP category without showing system impact.
3. Accepting "prompt hardening" as a complete mitigation for authorization or tool-execution failures.
4. Treating the model as the only control point.
5. Ignoring whether the proposed control is implementable.
6. Ignoring residual risk after mitigation.
7. Penalizing students for not finding every issue if their reasoning and evidence are strong.
8. Overvaluing long reports that are generic.

## Suggested grading weights

For the BrokenPilot capstone, use this weighting unless the instructor has a reason to change it.

| Area | Weight |
|---|---:|
| Threat model and architecture reasoning | 20% |
| Findings and evidence quality | 25% |
| Control design and remediation quality | 25% |
| Validation and residual risk | 15% |
| Communication and executive readout | 15% |

This weighting intentionally gives as much importance to mitigation quality as to finding issues.

## Calibration exercise

Use this before grading live submissions.

### Step 1  -  Independent scoring

Each instructor reads:

- strong threat model example;
- weak threat model example;
- strong evidence log example;
- weak evidence log example;
- strong remediation backlog example;
- weak remediation backlog example.

Each instructor assigns a score from 1 to 4 for each example.

### Step 2  -  Compare scoring

Discuss differences.

Questions to resolve:

- What evidence is required for a 4?
- What makes a remediation backlog implementable?
- How much detail is enough for the threat model?
- When does a finding become too generic for full credit?
- How should partial control validation be scored?

### Step 3  -  Agree on anchors

Write down local grading decisions.

Example:

```text
For full credit on tool authorization findings, student must include:
- user identity
- target object
- tenant mismatch or permission mismatch
- request/action evidence
- observed result
- root cause
- implementable authorization rule
- validation or test plan
```

### Step 4  -  Grade consistently

Use the same anchors for every student or team.

## Instructor notes for feedback

Good feedback should be specific and actionable.

Instead of:

> Needs more detail.

Say:

> The finding identifies cross-tenant tool misuse, but it does not show which user, which ticket, which tenant boundary, or what control setting was active. Add the request, observed response, and the authorization rule that should have blocked it.

Instead of:

> Mitigation is vague.

Say:

> "Add guardrails" is not implementable. Specify where the control runs, what decision inputs it uses, and what happens when the decision is deny.

## Minimum acceptable capstone evidence

For a passing capstone submission, students should provide at least:

- one architecture or data-flow diagram;
- one threat model or abuse-case table;
- three findings with evidence;
- one concrete tool or retrieval control design;
- one validation or retest result;
- one residual risk statement;
- one short executive summary.

For a strong submission, students should also provide:

- a tool permission matrix;
- a prioritized remediation backlog;
- detection or audit recommendations;
- clear separation between model behavior, application control failure, and operational risk;
- leadership-level risk framing.

## Final principle

Do not grade only whether students found the vulnerability.

Grade whether they can turn the vulnerability into a clear engineering decision.
