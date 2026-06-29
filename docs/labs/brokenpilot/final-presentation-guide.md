# BrokenPilot Final Presentation Guide

## Purpose

Use this guide to prepare the final capstone readout.

The audience is a mixed group of engineering leaders, security leaders, product owners, and senior engineers.

Your presentation should be clear enough for leadership and specific enough for engineers.

## Recommended structure

### 1. What we reviewed

Briefly explain BrokenPilot:

- business purpose;
- major capabilities;
- sensitive assets;
- AI components;
- tool/action capabilities.

### 2. Why the review matters

Explain why risk exists:

- the system can retrieve internal data;
- the model can be influenced by untrusted context;
- the agent can call tools;
- memory can persist state;
- users may rely on generated recommendations.

### 3. Top three risks

Present only the most important risks.

For each risk:

- title;
- affected component;
- attacker persona;
- impact;
- root cause;
- recommended fix.

### 4. Evidence summary

Keep evidence short.

Show enough to prove the finding, but avoid excessive payload details.

Evidence should include:

- role used;
- input or condition;
- observed behavior;
- failed control;
- business impact.

### 5. Root causes

Group root causes across findings.

Common examples:

- security decisions rely on model behavior;
- retrieval authorization is missing;
- tool permissions are too broad;
- approval gates are missing;
- memory is not scoped;
- logs are insufficient.

### 6. Recommended target state

Show the secure reference architecture.

Emphasize:

- policy outside the model;
- least-privilege tools;
- retrieval authorization;
- approval gates;
- safe output handling;
- scoped memory;
- auditability;
- monitoring and rollback.

### 7. Remediation roadmap

Use four priority buckets:

| Priority | Meaning |
|---|---|
| P0 | Must fix before broad deployment. |
| P1 | Fix soon; use compensating controls if needed. |
| P2 | Planned hardening. |
| P3 | Future improvement. |

### 8. Residual risk

Explain what remains even after fixes.

Examples:

- prompt injection cannot be completely eliminated;
- retrieved content can remain adversarial;
- humans may overtrust generated answers;
- new tools create new attack paths;
- monitoring must mature over time.

### 9. Decision request

End with a recommendation:

- approve limited pilot;
- approve only read-only mode;
- block high-impact tool actions until controls exist;
- require specific P0 fixes before deployment;
- require a follow-up review.

## Suggested slide count

For a 5–8 minute presentation:

1. Context
2. Architecture risk summary
3. Top risks
4. Evidence summary
5. Recommended controls
6. Roadmap and residual risk

## What to avoid

Avoid:

- long prompt payloads;
- unexplained jargon;
- claiming the system is “completely broken” without impact;
- recommending unrealistic controls;
- hiding residual risk;
- ignoring business value.

## Strong closing sentence

> BrokenPilot can be useful, but it should move forward with scoped permissions, retrieval authorization, approval gates, observable tool execution, and explicit residual-risk ownership.
