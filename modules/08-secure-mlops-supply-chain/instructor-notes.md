# Module 08 Instructor Notes — Secure MLOps and AI Supply Chain

## Module intent

This module should make students comfortable reviewing an ML delivery pipeline the same way they would review a software build and deployment pipeline, while recognizing ML-specific artifacts and failure modes.

The instructor should repeatedly connect ML concepts back to familiar security questions:

- What is the asset?
- Who can modify it?
- How do we know where it came from?
- What trust boundary does it cross?
- What happens if it is malicious, stale, poisoned, or wrong?
- What evidence allows production deployment?
- How do we roll back?

## Suggested timing

For a 90-minute session:

| Time | Activity |
|---|---|
| 0–10 min | Explain why ML supply chains are broader than software supply chains. |
| 10–25 min | Walk through ML pipeline architecture and artifacts. |
| 25–40 min | Discuss dataset, notebook, dependency, and training environment risks. |
| 40–55 min | Discuss model artifact, registry, promotion, and deployment controls. |
| 55–75 min | Run the broken ML pipeline review exercise. |
| 75–85 min | Group discussion and mitigation comparison. |
| 85–90 min | Summarize key takeaways and connect to Module 9. |

For a 45-minute session, compress the lecture and use the exercise as a facilitated tabletop rather than group work.

## Teaching emphasis

### 1. Data is a build input

Many students understand software dependencies as build inputs. Push them to treat datasets, labels, features, prompts, adapters, embeddings, and vector indexes the same way.

A useful phrase:

> If it changes production behavior, it is a security-relevant artifact.

### 2. Model registry is a production boundary

The registry is not only a storage bucket. It is a control point for promotion, integrity, approval, and rollback.

Ask:

- Who can register a model?
- Who can promote it?
- Is the artifact immutable?
- Are previous versions preserved?
- Is deployment tied to an approval record?

### 3. Notebooks are risky because they blur boundaries

Notebooks often combine exploration, code execution, data access, dependency installation, and artifact creation. This is powerful but dangerous.

Make clear that the goal is not to ban notebooks. The goal is to avoid turning unreviewed notebook state into production behavior.

### 4. Artifact loading is a security boundary

Avoid making this only a Python pickle discussion. The general lesson is broader: model artifacts and helper files can be untrusted inputs.

Ask:

- Does loading the artifact execute code?
- Is the artifact from a trusted source?
- Is it hashed or signed?
- Is it loaded in a sandbox?
- Can it access secrets or network resources during load?

### 5. Evaluation is a release gate

Accuracy is not the only requirement. Security, privacy, robustness, and abuse-case testing should be part of promotion.

For LLM/RAG/agent systems, remind students that evaluation also includes behavioral regression tests, prompt injection tests, retrieval authorization tests, and tool-use tests.

## Common student mistakes

| Mistake | Instructor response |
|---|---|
| Only scanning Python dependencies | Ask what protects datasets, labels, model artifacts, and registries. |
| Treating model registry as passive storage | Reframe it as a production deployment control. |
| Assuming internal pipelines are low risk | Ask what happens if the model affects tickets, decisions, customers, or security operations. |
| Focusing only on training | Ask about deployment, monitoring, feedback, rollback, and incident response. |
| Saying “just sign the model” | Ask what signing proves and what it does not prove. |
| Ignoring developer velocity | Ask for minimum viable controls for a fast-moving team. |

## Facilitation questions

Use these questions during the exercise:

1. Which artifacts can change production behavior?
2. Which artifact has the weakest provenance?
3. Which identity has the most dangerous permissions?
4. Which step allows unreviewed input into the pipeline?
5. Where could secrets leak?
6. Which gate would stop a malicious model artifact?
7. Which gate would stop a poisoned dataset?
8. What evidence should be required before promotion?
9. What needs to be logged for incident response?
10. What is the minimum safe rollback plan?

## Security vs velocity framing

Students should not design a process that blocks all ML work. Encourage a tiered model:

| Risk level | Example | Control expectation |
|---|---|---|
| Low | Offline experiment with synthetic data | Lightweight review and no production access. |
| Medium | Internal model affecting engineering workflow | Provenance, registry controls, evaluation gate, monitoring. |
| High | Customer-facing or security-sensitive model | Formal approval, privacy review, adversarial testing, rollback, incident playbook. |
| Critical | Safety, finance, health, or legal impact | Strong governance, independent review, strict auditability, staged rollout. |

## Suggested whiteboard diagram

Draw this flow:

```text
data -> labels -> features -> training code -> dependencies -> training job
  -> model artifact -> evaluation -> registry -> deployment -> monitoring -> feedback
```

Then ask students to mark:

- trust boundaries;
- write paths;
- secrets;
- artifacts;
- approval gates;
- rollback points;
- logs.

## Instructor wrap-up

End with these points:

1. ML supply chain security is not optional once models affect real workflows.
2. Every artifact that shapes behavior needs ownership, provenance, integrity, access control, and rollback.
3. Security gates must be realistic and risk-based.
4. The model registry and promotion pipeline are key enforcement points.
5. Secure MLOps sets the foundation for privacy, robustness, and red-team testing in later modules.

## Facilitating the executive memo exercise

Use the executive memo exercise after students complete the MLOps review. Push students to separate launch blockers from pilot risks. A useful answer should not simply say “delay because AI is risky”; it should define concrete controls that make a limited pilot safe enough to learn from.
