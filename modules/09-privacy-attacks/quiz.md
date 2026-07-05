# Module 09 Quiz  -  Privacy Attacks and Data Protection

## Questions

### 1. Why is privacy risk in AI systems broader than ordinary database access control?

### 2. What is membership inference?

### 3. What is model inversion?

### 4. Why are embeddings and vector databases privacy-sensitive?

### 5. Why is “the model provider does not train on our prompts” not enough to conclude that the system is private?

### 6. In a RAG system, why must source ACLs be preserved during chunking and embedding?

### 7. Name four AI-specific places where sensitive data may be stored or exposed.

### 8. Why are prompt and completion logs risky?

### 9. What controls should exist for agent memory?

### 10. What is the difference between data minimization and redaction?

### 11. Why is a system prompt saying “do not reveal sensitive data” insufficient as a privacy control?

### 12. What should a privacy risk assessment include for an AI assistant?

---

## Answer key

### 1. Why is privacy risk in AI systems broader than ordinary database access control?

Because sensitive information may be transformed, embedded, inferred, logged, retrieved, memorized, summarized, or reused through feedback loops. The database is only one of many data surfaces.

### 2. What is membership inference?

An attack or analysis that tries to determine whether a particular record or person was included in a model's training data.

### 3. What is model inversion?

An attack or analysis that tries to reconstruct sensitive attributes, representative examples, or hidden information from model behavior.

### 4. Why are embeddings and vector databases privacy-sensitive?

They can preserve semantic information about sensitive text and enable retrieval, inference, or cross-tenant exposure even when they do not store the original text in obvious form.

### 5. Why is “the model provider does not train on our prompts” not enough to conclude that the system is private?

The application may still store prompts, completions, retrieved context, logs, traces, feedback, memory, and tool outputs. Privacy risk exists outside provider training.

### 6. In a RAG system, why must source ACLs be preserved during chunking and embedding?

Because retrieval must enforce the same access rules as the source system. If chunks lose ACL metadata, unauthorized users may retrieve sensitive context.

### 7. Name four AI-specific places where sensitive data may be stored or exposed.

Examples: prompts, completions, retrieved context, embeddings, vector DBs, model traces, agent memory, feedback queues, evaluation datasets, fine-tuning datasets, tool outputs.

### 8. Why are prompt and completion logs risky?

They may contain full sensitive user inputs, internal documents, tool outputs, model responses, and business context. They are often accessible to engineers or vendors and may be retained too long.

### 9. What controls should exist for agent memory?

Provenance, scope, access control, expiry, user visibility where appropriate, deletion, review, and safeguards against cross-user reuse.

### 10. What is the difference between data minimization and redaction?

Data minimization avoids collecting, processing, retrieving, or storing unnecessary data in the first place. Redaction removes or masks sensitive data after it appears.

### 11. Why is a system prompt saying “do not reveal sensitive data” insufficient as a privacy control?

Prompts are not hard security boundaries. Privacy enforcement needs architecture controls such as authorization, minimization, logging governance, output checks, and access control.

### 12. What should a privacy risk assessment include for an AI assistant?

Sensitive data inventory, data-flow map, abuse cases, attack paths, existing controls, gaps, mitigations, retention/deletion design, auditability, and residual risk.
