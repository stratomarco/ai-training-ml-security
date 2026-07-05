# BrokenPilot Standalone Facilitation Guide

Use this guide when BrokenPilot is the primary hands-on target for the one-week course.

## Instructor positioning

Tell students:

```text
BrokenPilot is intentionally small. That is a feature. We are using it to isolate security properties without cloud accounts, external model providers, or unstable third-party dependencies.
```

## Delivery plan

| Course point | Activity | Time |
|---|---|---:|
| Day 2, Module 05 | prompt injection standalone lab | 45 minutes |
| Day 2, Module 06 | retrieval authorization standalone lab | 60 minutes |
| Day 3, Module 07 | tool authz and memory poisoning | 75 minutes |
| Day 4, Module 11 | finding rewrite from evidence | 60 minutes |
| Day 5, Module 12 | capstone report and presentation | 3 to 4 hours |

## What to emphasize

- BrokenPilot uses fake data and deterministic behavior.
- Repeatability is more important than realism for the core lab path.
- The model is not the security boundary.
- Retrieval, memory, and tools are separate trust boundaries.
- A weak finding says "add guardrails." A strong finding names the failed authorization, policy, or trust-boundary control.

## When students challenge the marker filter

Agree with them. The marker filter is intentionally weak. The lesson is that signature detection is not a reliable control. Ask them to rewrite the mitigation as architectural controls:

- instruction/data separation;
- retrieval authorization;
- tool authorization;
- approval gates;
- memory review and isolation;
- monitoring and audit.

## Grading guardrails

Do not require more findings than the target can support. For BrokenPilot, the required runnable finding set is:

1. prompt injection or instruction/data confusion;
2. retrieval authorization failure;
3. tool confused deputy;
4. memory poisoning and defense in depth.

Supply chain, privacy, and adversarial ML can appear as tabletop risks, not demonstrated runnable findings.
