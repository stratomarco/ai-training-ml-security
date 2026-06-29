# AI Data Retention and Log Review Template

Use this template to review prompt, completion, retrieval, tool, trace, memory, and feedback storage.

## 1. System

| Field | Value |
|---|---|
| System name |  |
| Owner |  |
| Reviewer |  |
| Date |  |

## 2. Stored artifacts

| Artifact | Stored? | Why stored? | Contains sensitive data? | Access control | Retention | Deletion path |
|---|---|---|---|---|---|---|
| User prompts |  |  |  |  |  |  |
| Model completions |  |  |  |  |  |  |
| System prompts |  |  |  |  |  |  |
| Retrieved context |  |  |  |  |  |  |
| Tool arguments |  |  |  |  |  |  |
| Tool results |  |  |  |  |  |  |
| Model traces |  |  |  |  |  |  |
| Embeddings metadata |  |  |  |  |  |  |
| Agent memory |  |  |  |  |  |  |
| User feedback |  |  |  |  |  |  |
| Evaluation examples |  |  |  |  |  |  |

## 3. Minimization decisions

For each stored artifact, explain why it cannot be avoided, reduced, sampled, redacted, aggregated, or shortened.

## 4. Access model

| User/group | Artifact access | Reason | Approval required? | Audit? |
|---|---|---|---|---|
|  |  |  |  |  |

## 5. Retention policy

| Artifact | Default retention | Legal/business reason | Deletion method | Exceptions |
|---|---|---|---|---|
|  |  |  |  |  |

## 6. Review questions

- Are full prompts necessary?
- Are full completions necessary?
- Is retrieved context necessary in logs?
- Are tool results overlogged?
- Can sensitive data be redacted before storage?
- Can logs be sampled?
- Who can search logs?
- Are log accesses audited?
- Does deletion propagate to vector indexes, caches, memory, and analytics stores?
- Is feedback reuse governed?

## 7. Findings

| Finding | Severity | Recommendation | Owner | Due date |
|---|---|---|---|---|
|  |  |  |  |  |
