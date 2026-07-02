# Module 08  -  Secure MLOps and AI Supply Chain

## Purpose

Teach students how to secure the machine learning delivery chain: datasets, labels, notebooks, dependencies, training jobs, model artifacts, registries, evaluation gates, deployment pipelines, inference infrastructure, prompts, adapters, embeddings, and monitoring feedback loops.

Traditional software supply chain security already matters. ML systems add new artifacts and new trust decisions. A model is not only code. It is also the result of data, training configuration, dependencies, compute environment, evaluation choices, and promotion decisions.

## Key message

> The ML pipeline is a software supply chain where data, models, prompts, adapters, embeddings, and evaluation results are security-sensitive artifacts.

Secure MLOps is not only about making training reproducible. It is about ensuring that the right data, code, dependencies, parameters, identities, and controls produced the right model, and that only trusted artifacts reach production.

## Learning objectives

By the end of this module, students should be able to:

1. Explain why ML supply chains are broader than classic software supply chains.
2. Identify assets and trust boundaries across an ML delivery pipeline.
3. Recognize risks in notebooks, datasets, dependencies, training code, model files, registries, containers, prompts, and deployment workflows.
4. Explain why model artifacts need provenance, integrity, access control, and safe loading.
5. Describe common model artifact risks, including unsafe deserialization and malicious model formats.
6. Design secure promotion gates from experiment to staging to production.
7. Define security checks for datasets, labels, features, dependencies, containers, and model artifacts.
8. Produce a Secure MLOps review containing risks, mitigations, owners, and residual risk.

## Topics

- ML pipeline threat modeling
- Dataset provenance and lineage
- Label integrity and quality controls
- Notebook security
- Dependency and package risk
- Training environment hardening
- Model artifact integrity
- Unsafe deserialization and model loading
- Model registry security
- Prompt, adapter, embedding, and vector index supply chain
- Container and GPU workload security
- CI/CD and ML pipeline security gates
- Secrets management
- Artifact signing and provenance
- SBOM and ML-BOM concepts
- Model cards and security metadata
- Evaluation and adversarial test gates
- Rollback and emergency model removal
- Monitoring feedback loop security

## Security engineering connection

Secure MLOps reuses classic security principles:

| Principle | MLOps interpretation |
|---|---|
| Least privilege | Training jobs, pipelines, notebooks, and registries should use scoped identities. |
| Complete mediation | Every artifact promotion should be authorized and checked. |
| Fail-safe defaults | Unknown, unsigned, unscanned, or unreviewed artifacts should not be promoted. |
| Separation of duties | The same person or job should not create, approve, and deploy high-impact models without control. |
| Defense in depth | Use provenance, signing, scanning, sandboxing, evaluation gates, registry ACLs, and runtime monitoring. |
| Auditability | Dataset, code, dependency, model, and deployment decisions should be traceable. |
| Secure failure | If an evaluation, provenance, or policy check fails, the deployment should stop safely. |
| Supply chain integrity | Data, code, dependencies, containers, and model artifacts all require integrity controls. |

## Reference architecture

```text
source control
  |
  +-- training code
  +-- pipeline definitions
  +-- prompts / templates
  +-- evaluation tests
  |
  v
CI/CD and ML pipeline orchestrator
  |
  +-- dependency resolution
  +-- container build
  +-- data access
  +-- feature generation
  +-- training job
  +-- evaluation job
  +-- security checks
  +-- provenance generation
  |
  v
artifact stores
  |
  +-- dataset registry
  +-- feature store
  +-- model registry
  +-- container registry
  +-- prompt registry
  +-- embedding / vector index store
  |
  v
promotion workflow
  |
  +-- security approval
  +-- model risk approval
  +-- deployment gate
  +-- rollback plan
  |
  v
production inference
  |
  +-- model serving
  +-- RAG / vector retrieval
  +-- monitoring
  +-- logging
  +-- incident response
  +-- feedback loop
```

## Core design rule

An ML pipeline should be able to answer:

- Which data produced this model?
- Who approved the data source?
- Which code, parameters, dependencies, and container built it?
- Which evaluation results allowed promotion?
- Was the artifact signed or otherwise integrity-protected?
- Who approved deployment?
- Which identity deployed it?
- Which customers, workflows, or systems can it affect?
- How can it be rolled back?
- What monitoring detects model abuse, drift, poisoning, or leakage?

If the organization cannot answer these questions, the model is not production-ready from a security perspective.

## Lab

Students review a deliberately broken ML delivery pipeline with:

- a public dataset of unclear origin;
- an unreviewed notebook with a hardcoded API key;
- unpinned dependencies;
- an unsafe model loading pattern;
- a model artifact with no provenance;
- weak model registry permissions;
- missing security and evaluation gates;
- no rollback plan;
- feedback data flowing back into training without abuse controls.

The goal is not to exploit real ML platforms. The goal is to practice reviewing ML supply chain architecture and designing realistic controls.

## Deliverable

Students produce a **Secure MLOps review** containing:

1. ML pipeline architecture summary
2. Asset and artifact inventory
3. Trust boundaries
4. Dataset provenance review
5. Dependency and environment review
6. Model artifact risk review
7. Registry and access-control review
8. CI/CD and promotion gate review
9. Monitoring and rollback requirements
10. Risk register
11. Residual risk statement

## Files in this module

- `slides.md`  -  Markdown slide deck
- `instructor-notes.md`  -  delivery guidance and facilitation notes
- `student-handout.md`  -  student-facing reference
- `exercise-secure-mlops-review.md`  -  main exercise
- `checklist.md`  -  Secure MLOps checklist
- `quiz.md`  -  quiz and answer key
- `references.md`  -  module-specific references

## Related labs and templates

- `../../labs/mlops-supply-chain-labs/broken-ml-pipeline-lab.md`
- `../../labs/mlops-supply-chain-labs/model-artifact-provenance-lab.md`
- `../../course-templates/secure-mlops-review-template.md`
- `../../course-templates/dataset-provenance-review-template.md`
- `../../course-templates/model-artifact-risk-review-template.md`
- `../../course-templates/model-registry-access-control-template.md`
- `../../course-templates/ml-bom-template.md`

## Executive communication exercise

This module now includes a one-page executive risk memo exercise. Students must translate secure MLOps and AI supply-chain findings into a launch, limited-pilot, or delay recommendation.
