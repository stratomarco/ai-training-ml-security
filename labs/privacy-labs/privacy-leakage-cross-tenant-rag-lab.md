# Lab  -  Privacy Leakage and Cross-Tenant RAG

## Module

Module 09  -  Privacy Attacks and Data Protection

## Lab type

Architecture review and tabletop exercise.

This lab can be adapted to a local DVAIA-style RAG environment later, but the first version is intentionally paper-based so students focus on reasoning and controls.

## Learning objectives

Students will learn to:

1. Identify sensitive data in a RAG system.
2. Explain how cross-tenant retrieval can happen.
3. Review whether source ACLs survive chunking and embedding.
4. Identify prompt, completion, and retrieval log leakage.
5. Design retrieval authorization and privacy controls.
6. Write a residual privacy risk statement.

## Scenario

**SupportAssist** is a customer-support AI assistant.

It indexes:

- customer support tickets;
- troubleshooting guides;
- account notes;
- incident summaries;
- contract snippets;
- escalation notes.

The product supports multiple enterprise customers. Each customer is a separate tenant.

Support engineers use SupportAssist to answer questions like:

- “Summarize recent incidents for this customer.”
- “What workarounds exist for this product issue?”
- “Draft a response to the customer.”
- “Find similar cases.”

## Current architecture

```text
support engineer
  |
  v
SupportAssist UI
  |
  +-- model gateway
  +-- retrieval service
  |     +-- vector DB with all tenants
  |     +-- source ticket store
  |     +-- documentation store
  |
  +-- prompt/completion logs
  +-- analytics dashboard
```

## Known design issues

1. The vector DB stores chunks from all tenants in one index.
2. Chunks include `tenant_name` but not full ACLs.
3. Retrieval uses semantic similarity first, then applies weak UI-side filtering.
4. Prompt logs include the full user question.
5. Completion logs include the full model answer.
6. Retrieved context is logged for debugging.
7. Engineers can search logs by customer name.
8. Deleted tickets are removed from the source ticket system but not immediately removed from the vector DB.
9. The model is instructed not to reveal data from unrelated customers.
10. There are no automated tests for cross-tenant retrieval.

## Student tasks

### Task 1  -  Data inventory

List sensitive data in:

- source tickets;
- chunks;
- embeddings;
- prompts;
- retrieved context;
- completions;
- logs;
- analytics dashboards.

### Task 2  -  Data-flow map

Draw or describe the data flow from source ticket to final model answer.

Mark where authorization should happen.

### Task 3  -  Abuse cases

Write at least five abuse cases.

Examples:

- Support engineer retrieves another tenant's escalation note.
- Prompt log exposes contract details to broad engineering audience.
- Deleted ticket remains available through vector search.
- Citation reveals another customer's name.
- Similar-case search leaks sensitive incident details.

### Task 4  -  Root cause analysis

Identify the root cause for each privacy failure.

Do not stop at “the model revealed data.”

Look for:

- missing ACL metadata;
- retrieval before authorization;
- weak tenant isolation;
- unsafe logging;
- missing deletion propagation;
- overbroad operational access;
- weak tests.

### Task 5  -  Mitigation design

Design a safer architecture.

Your answer should include:

- tenant isolation strategy;
- chunk metadata requirements;
- server-side retrieval authorization;
- deletion propagation;
- log minimization;
- log access control;
- citation policy;
- test cases;
- monitoring;
- residual risk.

## Expected secure design

```text
authenticated support engineer
  |
  v
policy check: user, role, tenant, purpose
  |
  v
retrieval query constrained by tenant and ACL metadata
  |
  v
authorized chunks only
  |
  v
context minimization
  |
  v
model response
  |
  v
output privacy check
  |
  v
safe logging with retention and access control
```

## Discussion questions

1. Should all tenants share one vector index?
2. What metadata must be attached to every chunk?
3. Should retrieved context be logged?
4. How quickly must deletion propagate to vector indexes?
5. How do you debug model quality without storing sensitive prompts forever?
6. What tests should run before every RAG release?
7. What residual risk remains even after retrieval authorization is fixed?

## Deliverable

Use:

- `course-templates/privacy-risk-assessment-template.md`
- `course-templates/vector-database-authorization-checklist.md`
