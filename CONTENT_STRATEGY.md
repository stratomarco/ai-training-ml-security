# Content Strategy — Reading-First, Lab-Supported Learning

This project is not intended to be a collection of prompt payloads, lab notes, or CTF-style exercises. It is a security engineering curriculum for AI-enabled systems.

The course should help students learn by reading, reasoning, discussing, designing controls, and then validating those ideas with labs.

## Core teaching principle

> Labs reinforce understanding. They do not replace explanation.

Every major topic should explain the attack, why it exists, what security principle it violates, what controls can mitigate it, how to test those controls, and how to communicate the residual risk.

## Required structure for attack topics

Major attack topics should use this structure:

1. What is the attack?
2. Why does it exist?
3. What security principle is being violated?
4. What does the attack path look like?
5. What is the technical and business impact?
6. What are weak or incomplete mitigations?
7. What are strong controls?
8. What should engineers implement?
9. How do we test the fix?
10. How does this map to OWASP, BIML, NIST, MITRE ATLAS, and classic security engineering?
11. How would we explain the risk to leadership?
12. What lab or tabletop exercise reinforces the lesson?

## Security roots

This course deliberately connects modern ML, LLM, RAG, and agent security back to classic security engineering:

| Foundation | Role in the course |
|---|---|
| Gary McGraw | Building security in, software security touchpoints, architectural risk analysis |
| Ross Anderson | Systems thinking, incentives, operational constraints, real security failures |
| Adam Shostack | Threat modeling, trust boundaries, abuse cases, practical security review |
| Saltzer and Schroeder | Least privilege, complete mediation, fail-safe defaults, economy of mechanism, psychological acceptability |
| Jean-Philippe Aumasson | Applied cryptography, misuse resistance, key management, signing, provenance |
| OWASP ML/LLM/Agentic projects | Practitioner risk taxonomies for current AI systems |
| BIML | ML and LLM architectural risk analysis; building security into ML systems |
| NIST AI RMF / AI 600-1 / AI 100-2 | Risk management, governance, GenAI risks, adversarial ML terminology |
| MITRE ATLAS | Adversarial AI tactics and techniques for red-team and blue-team alignment |

## What good content looks like

Good content is:

- Conceptual before procedural
- Architecture-aware
- Grounded in security principles
- Clear about assumptions
- Honest about mitigation limits
- Specific enough that an engineer can act
- Mapped to recognized frameworks
- Supported by labs when possible
- Useful even when a lab environment is unavailable

## What weak content looks like

Weak content is:

- Only a payload or screenshot
- Only a list of OWASP categories
- Only a lab walkthrough without root cause analysis
- Only a high-level warning without implementable controls
- Too dependent on a single tool or UI
- Missing residual risk discussion
- Missing business impact
- Missing references to security engineering foundations

## Deep-dive priority modules

The first modules to deepen are:

1. Module 05 — LLM Application Security
2. Module 06 — RAG Security
3. Module 07 — Agent and Tool Security
4. Module 10 — Adversarial ML and Robustness
5. Module 12 — BrokenPilot Capstone

Each of those modules should eventually include:

- `deep-dive.md`
- `attack-anatomy.md`
- `controls-and-remediations.md`
- `common-mistakes.md`
- `worked-example.md`

## Lab role

Labs should answer:

- Can the student observe the failure?
- Can the student explain the root cause?
- Can the student map it to a security principle?
- Can the student design a concrete control?
- Can the student test whether the control works?
- Can the student communicate the residual risk?

A lab is successful only if it improves security reasoning.
