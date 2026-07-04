# Module 04  -  BIML and Architectural Risk Analysis

## Purpose

Use BIML as the bridge between classic security engineering and practical ML/LLM architecture review.

This module teaches students how to identify security risks before implementation by reviewing the architecture, lifecycle, assets, trust boundaries, assumptions, and abuse cases of an AI-enabled system.

## Key message

Good AI security starts before exploit payloads. Architecture determines which failures become possible.

The most important question is not only:

> Can I jailbreak the model?

The stronger question is:

> Why does the system allow a model response, retrieved document, dataset, tool call, or workflow step to create security impact?

## Why BIML matters

The Berryville Institute of Machine Learning focuses on building security into ML systems from a security engineering perspective. Its earlier work introduced BIML-78, a set of 78 ML security risks associated with a generic ML process model. Later LLM architectural risk work adapted and extended that approach to LLM systems.

This makes BIML especially useful for this course because it is not only an attack list. It is a design-review mindset.

## Learning objectives

By the end of this module, students should be able to:

1. Explain architectural risk analysis in plain language.
2. Explain why BIML is useful for ML and LLM security design reviews.
3. Distinguish design-level risks from implementation bugs.
4. Identify assets, trust boundaries, assumptions, and abuse cases in an AI architecture.
5. Map ML and LLM risks to lifecycle components.
6. Explain why prompts, datasets, embeddings, model artifacts, tools, and feedback loops change the architecture.
7. Produce an architecture risk review for an AI-enabled system.
8. Recommend security requirements and design controls.
9. Discuss residual risk after mitigations.
10. Communicate architectural AI risk to engineers and leadership.

## Topics

- Architectural risk analysis
- Building security in
- BIML-78
- BIML LLM architectural risk analysis
- ML lifecycle risk
- LLM architecture risk
- Risk categories across components
- System-wide risks
- Abuse-case-driven review
- Security requirements
- Design controls
- Residual risk
- Architecture review deliverables

## Security engineering connection

This module directly connects to classic security engineering:

| Classic concept | AI/ML application |
|---|---|
| Secure design review | Review AI architecture before implementation |
| Threat modeling | Identify attackers, assets, entry points, and trust boundaries |
| Abuse cases | Describe how the system can be intentionally misused |
| Least privilege | Limit model, tool, data, and workflow privileges |
| Complete mediation | Check authorization at every data/tool/action boundary |
| Defense in depth | Combine model guardrails with system controls |
| Secure failure | Ensure low-confidence, blocked, or failed model actions fail safely |
| Auditability | Log decisions, tool calls, retrievals, policy decisions, and approvals |
| Supply chain integrity | Treat datasets, models, adapters, prompts, and dependencies as artifacts |

## Module framing

Architectural risk analysis asks:

1. What are we building?
2. What are the valuable assets?
3. Who can interact with the system?
4. What can the system observe?
5. What can the system change?
6. What trust boundaries exist?
7. What assumptions must be true for the system to be safe?
8. What happens when those assumptions are false?
9. What security requirements should be added?
10. What residual risk remains?

## Reference architecture

```text
user / attacker
  |
  v
AI application interface
  |
  +-- identity and session context
  +-- prompt builder
  +-- model gateway
  +-- policy layer
  +-- retrieval service
  |     +-- document store
  |     +-- embedding model
  |     +-- vector database
  +-- tool broker
  |     +-- ticketing API
  |     +-- configuration API
  |     +-- email/docs API
  +-- memory service
  +-- logging and monitoring
  +-- feedback pipeline
  +-- model registry
```

## Lab

Students perform an architecture risk review of **DocOps Assistant**, a fictional internal AI assistant that can search internal documents, summarize incidents, and update tickets.

Students must identify design-level risks before writing any prompt injection payloads.

## Deliverable

Architecture risk review containing:

- System summary
- Asset list
- Trust boundaries
- Assumptions
- Abuse cases
- Risk list
- Risk prioritization
- Security requirements
- Defensive architecture recommendations
- Residual risk statement

## Recommended module files

- `slides.md`
- `instructor-notes.md`
- `student-handout.md`
- `exercise-biml-architecture-review.md`
- `checklist.md`
- `quiz.md`
- `references.md`

## Instructor guidance

Students may try to jump straight into prompt injection examples. Redirect them back to architecture.

Ask repeatedly:

- Why does this attack have impact?
- Which trust boundary failed?
- Which authorization decision was missing?
- Which assumption was unsafe?
- Which component should enforce the control?
- What should be redesigned before deployment?

A strong answer should identify not only attacks, but also security requirements.

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
