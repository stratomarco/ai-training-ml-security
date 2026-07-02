# Instructor Guide — Finding Rewrite Exercise

## Purpose

This exercise helps students move from vulnerability spotting to security engineering communication.

It is especially useful before the BrokenPilot capstone because students often produce findings that are technically interesting but not actionable.

## Recommended timing

| Format | Timing |
|---|---|
| 2-hour workshop | 10 minutes as a quick discussion |
| Half-day workshop | 20 minutes individual + 10 minutes discussion |
| 1-day workshop | 25 minutes group work + 15 minutes review |
| 2-day intensive | 30 minutes rewrite + 20 minutes peer review |
| 12-week course | assign as homework before Module 11 or 12 |

## Facilitation flow

1. Show the weak finding.
2. Ask students what is missing.
3. Give them the evidence block.
4. Ask them to rewrite the finding.
5. Compare against the strong example.
6. Discuss what made the rewritten finding actionable.

## Key teaching points

Students should identify that:

- "The AI can be tricked" is not a root cause.
- The real issue is missing authorization enforcement at the tool layer.
- The model should not be trusted to authorize state-changing operations.
- A useful remediation defines an enforceable rule.
- A good finding includes validation steps.

## What to listen for

Strong student answers mention:

- target-object authorization
- tenant boundary
- confused deputy
- complete mediation
- tool-layer enforcement
- negative and positive tests
- residual risk

Weak student answers say:

- add guardrails
- improve the prompt
- make the AI safer
- block malicious inputs
- use a better model

## Suggested debrief question

Ask:

> If the model behaves perfectly but the tool does not check authorization, is the system secure?

Expected answer:

> No. The tool must enforce authorization independently because model behavior can be influenced by user input, retrieved content, memory, tool descriptions, or implementation errors.
