# Exercise  -  RAG Threat Model

## Scenario

Your company is building **DocuPilot**, an internal RAG assistant.

DocuPilot helps employees answer questions from internal documents.

It can search:

- engineering runbooks
- security policies
- incident reports
- HR FAQs
- customer support notes
- vendor documentation
- public webpages saved by employees

The system uses a vector database. Documents are chunked and embedded. The assistant retrieves the top matching chunks and sends them to an LLM with the user's question.

## User roles

| Role | Access |
|---|---|
| Employee | public internal policies and general docs |
| Engineer | engineering runbooks and incident summaries |
| Security engineer | security policies, incident reports, detection notes |
| HR | HR documents |
| Finance | finance documents |
| Customer support | customer support notes for assigned customers |
| Admin | configuration and index management |

## Known design details

- The current vector index stores chunks from all teams.
- Some chunks have document IDs but no access-control metadata.
- The application checks whether the user is logged in, but not whether each retrieved chunk is authorized.
- The assistant is instructed in the system prompt not to reveal confidential information.
- Some source documents are user-editable wiki pages.
- Some vendor documents are copied from public webpages.
- Logs store the user prompt, retrieved chunks, and generated answer.
- The assistant shows citations, but users can sometimes see citations to documents they cannot open.

## Task 1  -  Draw the system

Create a simple data-flow diagram showing:

- user
- application
- identity provider
- document stores
- ingestion pipeline
- embedding service
- vector database
- prompt builder
- LLM provider
- output renderer
- logs/monitoring

Mark trust boundaries.

## Task 2  -  Identify assets

List at least 10 security-relevant assets.

Consider:

- documents
- chunks
- embeddings
- metadata
- access-control labels
- prompts
- logs
- API keys
- user identity
- generated answers

## Task 3  -  Identify threats

Identify at least 8 threats.

Include at least one threat from each category:

- indirect prompt injection
- retrieval authorization failure
- cross-tenant or cross-team leakage
- poisoned document
- metadata loss
- sensitive logging
- source trust failure
- output/citation problem

## Task 4  -  Root cause analysis

For each threat, explain the root cause.

Avoid writing only symptoms.

Example:

```text
Symptom: Employee receives finance content.
Root cause: Retrieval uses semantic similarity without enforcing document-level or chunk-level authorization before prompt construction.
```

## Task 5  -  Mitigation design

Propose controls at these stages:

1. Ingestion
2. Chunking
3. Indexing
4. Retrieval
5. Prompt construction
6. Generation
7. Output handling
8. Logging and monitoring

## Task 6  -  Residual risk

Write a short residual risk statement.

Include:

- what remains possible
- what is accepted
- what must be monitored
- what should trigger human review

## Expected deliverable

Use `course-templates/rag-threat-model-template.md`.

