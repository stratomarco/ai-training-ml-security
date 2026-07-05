# Deep Dive: ML System Architecture

## What this module is really about

This module teaches students to see an ML system as an architecture, not as a model file. The model is one component in a larger system that includes data sources, feature pipelines, retrieval stores, prompts, model services, tool brokers, user interfaces, logs, monitoring, deployment pipelines, and human workflows.

Many AI security failures are architecture failures. A model receives data it should not have received. A tool executes an action without checking the target object. A vector database returns cross-tenant documents. A notebook exports an artifact with no provenance. A dashboard renders model output without encoding. A feedback loop stores poisoned text as trusted memory.

To review an ML system well, the student must draw the system in a way that exposes trust boundaries and security decisions.

## The core engineering decision

The main decision is: where must the architecture enforce security properties, and where is the model only advisory?

A good architecture makes enforcement points visible. Retrieval authorization happens before context is assembled. Tool authorization happens before action execution. Output encoding happens before rendering. Artifact verification happens before promotion. Privacy controls happen before collection, training, retrieval, logging, and retention. Human approval happens before high-impact state change.

If the diagram only shows "user -> model -> answer," it hides the security problem.

## Architectural views that matter

### Data-flow view

The data-flow view shows where data comes from, where it is transformed, where it is stored, where it crosses boundaries, and where it leaves the system. This view is essential for privacy, confidentiality, poisoning, and logging risks.

### Control-flow view

The control-flow view shows who or what can cause actions. It matters for agents, tools, approvals, and state changes. A model that can call a tool is part of control flow, even if the team describes it as "just an assistant."

### Trust-boundary view

The trust-boundary view marks where assumptions change. A user prompt is not trusted like a system policy. A retrieved document is not trusted like application code. A model-generated tool argument is not trusted like a verified user action. A model artifact from a notebook is not trusted like a signed release artifact.

### Lifecycle view

The lifecycle view covers training, evaluation, release, monitoring, feedback, rollback, and retirement. ML systems change over time, and security controls must survive those changes.

## Components to include in a review

A useful ML architecture review should include:

- Users and roles.
- Data sources and ownership.
- Training, tuning, retrieval, and feedback datasets.
- Model hosting and model versioning.
- Prompt construction and context assembly.
- Retrieval systems and metadata filters.
- Tool broker and downstream systems.
- Output sinks and storage.
- Logs, traces, and monitoring.
- CI/CD and artifact promotion.
- Human review and escalation paths.

The goal is not a beautiful diagram. The goal is a diagram that lets someone ask security questions.

## Where architecture creates risk

Risk appears when boundaries are implicit.

If all retrieved documents are placed into context without authorization, the model becomes a cross-tenant data exposure mechanism.

If a service account has broad privileges and the model can produce tool arguments, the agent becomes a confused deputy.

If training and production artifacts are connected by a manual notebook export, the supply chain has weak integrity.

If logs collect prompts, retrieved context, and outputs without retention rules, monitoring becomes a privacy problem.

If a classifier output is used as a hard gate without fallback, uncertainty becomes an availability or fairness issue.

## Architecture review questions

Ask these questions during review:

1. What can the model influence?
2. What data can reach the model?
3. What data can leave the model?
4. What actions can model output trigger?
5. Where is authorization enforced?
6. Where is output validated for the sink?
7. What artifacts are promoted, and how is integrity proven?
8. What is logged, retained, redacted, and reviewed?
9. What happens when confidence is low or context is missing?
10. How can the system be rolled back?

## Reading-to-lab transfer

BrokenPilot is useful because it makes architecture visible. Students can see retrieval, chat, memory, tools, controls, and audit paths as separate pieces. The toy-classifier app is useful because it separates model behavior from threshold and output-integrity decisions. The MLOps evidence pack is useful because it shows architecture through release evidence instead of code execution.

Students should leave this module able to turn a vague AI feature description into a reviewable architecture.
