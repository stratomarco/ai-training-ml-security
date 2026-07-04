# Module 02  -  ML System Architecture

## Status

Ready for v0.3 review.

## Purpose

This module teaches how machine learning systems are built before teaching how they break.

Students should leave this module able to describe the normal lifecycle of an ML system, identify where security controls should exist, and explain why ML security is not only about the model. The module introduces the major system components that appear in classical ML, LLM, RAG, and agent architectures: data sources, labeling, feature engineering, training, evaluation, model registries, deployment, inference APIs, vector databases, prompts, tools, monitoring, and feedback loops.

## Core message

> In ML systems, data, models, prompts, and feedback loops become part of the attack surface.

A model is not an isolated algorithm. It is a component inside a larger system that collects data, transforms it, trains or configures behavior, serves predictions, logs interactions, and adapts over time. Security failures can happen anywhere in that lifecycle.

## Learning objectives

By the end of this module, students should be able to:

1. Explain the difference between traditional software architecture and ML system architecture.
2. Describe the major stages of the ML lifecycle: data collection, labeling, feature engineering, training, evaluation, deployment, inference, monitoring, and feedback.
3. Identify assets and trust boundaries in an ML system.
4. Explain how data quality, data provenance, and pipeline integrity affect model behavior.
5. Identify where poisoning, evasion, model theft, model tampering, privacy leakage, and supply chain compromise can occur.
6. Explain how LLM, RAG, and agent systems extend the ML architecture attack surface.
7. Produce a data-flow diagram for a simple ML-enabled product.
8. Propose baseline security controls for each ML lifecycle stage.
9. Explain why secure MLOps must connect AppSec, cloud security, data governance, privacy, and incident response.
10. Prepare students for Module 03 by grounding the OWASP ML Security Top 10 in real system components.

## Audience

Primary audience:

- Application security engineers
- Product security engineers
- Security architects
- ML engineers
- Platform engineers
- Cloud security engineers
- MLOps engineers
- Security champions

Secondary audience:

- Red teamers
- Privacy engineers
- Engineering managers
- Product managers responsible for AI-enabled features

## Required background

Students should know the concepts from Module 01: assets, trust boundaries, least privilege, complete mediation, defense in depth, secure SDLC, and residual risk.

They do not need to understand ML mathematics. This module focuses on system architecture and security reasoning.

## Recommended duration

| Format | Duration | Notes |
|---|---:|---|
| Awareness session | 60 minutes | Use the lifecycle map and discussion only |
| Practitioner session | 90 minutes | Include the DFD exercise |
| Workshop | 2.5–3 hours | Include group work, architecture review, and debrief |

## Module files

| File | Purpose |
|---|---|
| [`slides.md`](slides.md) | Slide-style teaching deck in Markdown |
| [`instructor-notes.md`](instructor-notes.md) | Facilitation guide, timing, expected answers |
| [`student-handout.md`](student-handout.md) | Student-facing summary and working notes |
| [`exercise-ml-lifecycle-dfd.md`](exercise-ml-lifecycle-dfd.md) | Main architecture mapping exercise |
| [`checklist.md`](checklist.md) | ML architecture security checklist |
| [`quiz.md`](quiz.md) | Review questions with answer key |
| [`references.md`](references.md) | Module-specific references |

## Concepts covered

- ML lifecycle
- Data as a security-sensitive asset
- Data provenance
- Data labeling risk
- Feature engineering risk
- Training pipeline integrity
- Evaluation and benchmark leakage
- Model registry security
- Model artifact integrity
- Inference API security
- Monitoring and drift detection
- Feedback loop abuse
- Privacy leakage
- Model theft
- Data poisoning
- Evasion
- ML supply chain
- LLM/RAG/agent architecture extensions

## Reference architecture

```text
external data sources
  |
  v
raw data storage ---- data governance / consent / retention
  |
  v
labeling and curation ---- human labelers / vendors / automation
  |
  v
feature engineering / preprocessing
  |
  v
training pipeline ---- code / dependencies / secrets / compute
  |
  v
model artifact ---- model registry / signing / metadata
  |
  v
evaluation ---- test data / benchmarks / robustness tests
  |
  v
deployment ---- serving platform / API gateway / authz
  |
  v
inference ---- user input / prediction / model output
  |
  v
monitoring ---- logs / drift / abuse / incidents
  |
  v
feedback loop ---- retraining / fine-tuning / prompt updates
```

## LLM/RAG/agent extension

```text
user / attacker
  |
  v
AI application
  |
  +-- identity and authorization
  +-- prompt construction
  +-- LLM gateway
  +-- retrieval service
  |     +-- embedding model
  |     +-- vector database
  |     +-- document store
  +-- tool execution service
  |     +-- ticketing API
  |     +-- email API
  |     +-- cloud API
  +-- memory store
  +-- monitoring and audit logs
```

The architecture expands the attack surface because untrusted inputs can enter through user prompts, retrieved documents, indexed content, tool responses, memory, logs, and feedback loops.

## Key teaching distinction

| Weak framing | Stronger framing |
|---|---|
| “The model is secure.” | “Which lifecycle stages and trust boundaries are controlled?” |
| “The dataset is internal.” | “Who can write to it, label it, transform it, and approve it?” |
| “The model passed evaluation.” | “What attacks, edge cases, and distribution shifts were tested?” |
| “The API is authenticated.” | “Can authenticated users extract, abuse, or poison behavior?” |
| “The vector DB has the right documents.” | “Is retrieval authorized per user and tenant?” |
| “The agent uses approved tools.” | “Are tool calls independently authorized and audited?” |
| “We can retrain if needed.” | “Can we trace, reproduce, roll back, and investigate model changes?” |

## Lab / exercise

Students review **LoanAssist ML**, a fictional ML-enabled loan triage system.

The system ingests application data, third-party credit data, support notes, and historical outcomes. It trains a model that scores applications for manual review. Later, the company adds an LLM assistant that explains model decisions to internal analysts and retrieves supporting documents from a vector database.

Students must:

1. Draw a lifecycle data-flow diagram.
2. Identify assets.
3. Identify trust boundaries.
4. Identify likely attack paths.
5. Map attacks to lifecycle stages.
6. Propose baseline controls.
7. Write a residual risk statement.

See [`exercise-ml-lifecycle-dfd.md`](exercise-ml-lifecycle-dfd.md).

## Deliverable

Students should produce:

1. An ML lifecycle diagram.
2. An asset inventory.
3. A trust-boundary map.
4. A list of at least eight architecture-level risks.
5. A list of at least eight controls.
6. A brief statement explaining how this architecture could fail even if the application code has no classic OWASP Top 10 bug.

## Instructor guidance

Students often jump from “ML system” directly to “prompt injection” or “adversarial examples.” Redirect them toward lifecycle thinking:

- Where did the data come from?
- Who can change it?
- Who labels it?
- What transformations happen before training?
- How is the model artifact protected?
- What is logged during inference?
- Can users query the model repeatedly?
- Can outputs influence future training?
- Can a retrieved document affect a decision explanation?
- Can the system be rolled back after a bad model release?

The goal of this module is to make students see the complete system before they learn individual attack categories.

## Next module

After this module, continue with [`../03-owasp-ml-top-10/README.md`](../03-owasp-ml-top-10/README.md).

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
