# ML-BOM Template

An ML-BOM is a bill of materials for an ML system or model release. It extends software bill-of-materials thinking to data, model, prompt, evaluation, and deployment artifacts.

## Release metadata

| Field | Value |
|---|---|
| Model/system name |  |
| Release version |  |
| Release date |  |
| Business owner |  |
| Technical owner |  |
| Risk tier |  |
| Production environment |  |

## Software components

| Component | Version | Source | Hash/digest | Notes |
|---|---|---|---|---|
| Training code repository |  |  |  |  |
| Source commit |  |  |  |  |
| Dependency lockfile |  |  |  |  |
| Container image |  |  |  |  |
| Base image |  |  |  |  |

## Data components

| Dataset / feature source | Version | Owner | Classification | Approved use | Notes |
|---|---|---|---|---|---|
| Training dataset |  |  |  |  |  |
| Validation dataset |  |  |  |  |  |
| Evaluation dataset |  |  |  |  |  |
| Feature set |  |  |  |  |  |

## Model components

| Artifact | Version | Source | Hash/signature | Notes |
|---|---|---|---|---|
| Base model |  |  |  |  |
| Fine-tuned model |  |  |  |  |
| Adapter / LoRA |  |  |  |  |
| Tokenizer |  |  |  |  |
| Configuration |  |  |  |  |

## LLM/RAG components if applicable

| Artifact | Version | Source | Owner | Notes |
|---|---|---|---|---|
| System prompt |  |  |  |  |
| Prompt templates |  |  |  |  |
| Tool schemas |  |  |  |  |
| Policy prompts |  |  |  |  |
| Embedding model |  |  |  |  |
| Vector index |  |  |  |  |
| RAG corpus |  |  |  |  |

## Evaluation evidence

| Evaluation | Version/date | Result | Owner |
|---|---|---|---|
| Functional metrics |  |  |  |
| Security tests |  |  |  |
| Privacy tests |  |  |  |
| Robustness tests |  |  |  |
| RAG/agent behavior tests |  |  |  |

## Approval and deployment

| Field | Value |
|---|---|
| Production approver |  |
| Approval date |  |
| Deployment pipeline |  |
| Runtime identity |  |
| Rollback version |  |
| Monitoring dashboard |  |
| Incident playbook |  |
