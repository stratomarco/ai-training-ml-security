# Module 01  -  Security Engineering for AI

## Status

Ready for v0.2 review.

## Purpose

This module establishes the core argument of the course: **AI security starts with security engineering**.

Students should leave this module understanding that ML, LLM, RAG, and agent systems are not outside the normal rules of security. They are software systems with unusual components: probabilistic models, datasets, embeddings, prompts, tools, memory, and automated workflows. Those components change the attack surface, but they do not remove the need for classic security architecture.

## Core message

> The model is not the security boundary. The system around the model is where most security decisions must live.

Prompts can influence behavior, but prompts should not be treated as hard authorization, data isolation, policy enforcement, or audit controls. Security controls should be implemented in deterministic system components wherever possible.

## Learning objectives

By the end of this module, students should be able to:

1. Explain why ML Security is an extension of security engineering.
2. Identify assets, actors, attacker goals, trust boundaries, and security assumptions in an AI-enabled application.
3. Distinguish between model behavior controls and system security controls.
4. Explain why prompts, model alignment, and output filters are not sufficient security boundaries by themselves.
5. Apply classic principles such as least privilege, complete mediation, defense in depth, fail-safe defaults, and auditability to AI systems.
6. Produce a first-pass threat model for a simple AI assistant.
7. Propose practical guardrails that balance security, usability, and developer velocity.
8. Discuss residual risk in language that engineering and leadership can understand.

## Audience

Primary audience:

- Application security engineers
- Product security engineers
- Security architects
- ML engineers
- Platform engineers
- Security champions
- Red teamers

Secondary audience:

- Engineering managers
- Product managers
- Risk and compliance stakeholders
- Privacy engineers

## Required background

Students should know basic application architecture, APIs, authentication, authorization, logs, and common web security concepts. They do not need to be ML researchers.

## Recommended duration

| Format | Duration | Notes |
|---|---:|---|
| Awareness session | 60 minutes | Use slides and discussion only |
| Practitioner session | 90 minutes | Include the threat modeling exercise |
| Workshop | 2.5–3 hours | Include group exercise and review |

## Module files

| File | Purpose |
|---|---|
| [`slides.md`](slides.md) | Slide-style teaching deck in Markdown |
| [`instructor-notes.md`](instructor-notes.md) | Facilitation guide, timing, expected answers |
| [`student-handout.md`](student-handout.md) | Student-facing summary and working notes |
| [`exercise-threat-model.md`](exercise-threat-model.md) | Main threat modeling exercise |
| [`checklist.md`](checklist.md) | AI security engineering checklist |
| [`quiz.md`](quiz.md) | Review questions with answer key |
| [`references.md`](references.md) | Module-specific references |

## Concepts covered

- Security engineering foundations
- Threat modeling
- Trust boundaries
- Assets and attacker goals
- Least privilege
- Complete mediation
- Fail-safe defaults
- Defense in depth
- Secure SDLC
- Abuse cases
- Residual risk
- AI-specific attack surface
- Prompt injection as an architectural problem
- Tool-use and agency as authorization problems
- RAG as an untrusted-input problem
- Model output as untrusted output

## Reference architecture

```text
user / attacker
  |
  v
AI-enabled application
  |
  +-- identity and session layer
  +-- application authorization layer
  +-- prompt construction layer
  +-- model gateway
  +-- policy and safety checks
  +-- retrieval service / vector database
  +-- tool execution service
  +-- business data stores
  +-- logging, monitoring, and audit trail
```

## Key teaching distinction

| Weak framing | Stronger framing |
|---|---|
| “Can we make the prompt safe?” | “Where should security policy be enforced?” |
| “Can the model refuse bad requests?” | “What can the user and model actually access?” |
| “Can we block jailbreaks?” | “What happens when the model is manipulated?” |
| “The assistant has rules.” | “The system has enforceable controls.” |
| “The model should not leak data.” | “The retrieval and authorization layers must prevent unauthorized data access.” |
| “The agent should behave.” | “The agent must only have scoped tools, validated arguments, and approval gates.” |

## Lab / exercise

Students threat model **DocAssist**, a simple internal AI assistant that summarizes internal documents.

The assistant can:

- Search internal documents
- Retrieve document snippets
- Summarize content
- Answer user questions
- Store chat history
- Log prompts and responses

Students identify assets, users, attackers, trust boundaries, likely abuse cases, and practical mitigations.

See [`exercise-threat-model.md`](exercise-threat-model.md).

## Deliverable

Students should produce:

1. A simple system/context diagram.
2. A list of assets.
3. A list of trust boundaries.
4. At least five abuse cases.
5. At least five mitigations.
6. A residual risk statement.

## Instructor guidance

Students often focus too quickly on prompt examples. Redirect them toward architecture:

- Who is authenticated?
- What is authorized?
- What data is retrieved?
- What does the model see?
- What can the model cause the system to do?
- Where are decisions enforced?
- What is logged?
- What happens when the model is wrong?

The goal of this module is not to make students expert LLM red teamers. The goal is to make them reason like security engineers when an AI component appears in the system.

## Next module

After this module, continue with [`../02-ml-system-architecture/README.md`](../02-ml-system-architecture/README.md).

<!-- student-reading-guide-link -->

## Student reading guide

Before starting the lab or exercise, read [student-reading-guide.md](student-reading-guide.md). It explains the module's core security decision, lab path, common mistakes, and exit ticket.

<!-- depth-prose-pass-01-04 -->

## Depth reading path

Use these pages to connect the module reading to later labs and graded deliverables:

- [Deep Dive](deep-dive.md)
- [Attack Anatomy](attack-anatomy.md)
- [Controls and Remediations](controls-and-remediations.md)
- [Common Mistakes](common-mistakes.md)
- [Worked Example](worked-example.md)

<!-- cohesion-note-link -->

## Course cohesion note

For instructor handoff language and the module's place in the full course story, see [cohesion-note.md](cohesion-note.md).
