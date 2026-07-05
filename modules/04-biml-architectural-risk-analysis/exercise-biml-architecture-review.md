# Exercise  -  BIML-Style Architecture Risk Review

## Exercise goal

Perform an architecture risk review of an AI-enabled internal assistant before writing exploit payloads.

The goal is to identify design-level risks and propose security requirements.

## Scenario: DocOps Assistant

Your company is building **DocOps Assistant**, an internal AI assistant for engineering and operations teams.

DocOps Assistant can:

- answer questions about internal documentation
- summarize incidents
- summarize support tickets
- search operational runbooks
- suggest ticket updates
- create draft incident summaries
- store user preferences in memory
- receive feedback on whether answers were useful

The product team wants to later add automatic ticket updates and automated incident status messages.

## Current architecture

```text
employee browser
  |
  v
web application
  |
  +-- identity/session context
  +-- prompt builder
  +-- LLM provider API
  +-- retrieval service
  |     +-- internal document store
  |     +-- embedding service
  |     +-- vector database
  +-- ticket service connector
  +-- memory service
  +-- feedback store
  +-- application logs
```

## Current design assumptions

The team believes:

1. Only employees can access the assistant.
2. Internal documents are trusted.
3. The model will follow the system prompt.
4. Prompt injection is mostly a user-behavior problem.
5. The model can decide whether a ticket update is safe.
6. All retrieved documents can be inserted into context.
7. Full prompts and responses should be logged for debugging.
8. User feedback can be used later to improve the system.
9. Memory improves usability and should be enabled by default.
10. Security can be improved later after the first release.

## Your task

Perform a BIML-style architecture risk review.

You must produce:

1. System summary
2. Asset list
3. Trust boundaries
4. Unsafe assumptions
5. Abuse cases
6. Design-level risks
7. Security requirements
8. Mitigation plan
9. Residual risk statement

## Step 1  -  System summary

Write a short summary of what the system does.

Prompt:

```text
DocOps Assistant is a system that...
```

## Step 2  -  Identify assets

List at least ten assets.

Use this table:

| Asset | Why it matters | Who should access it? |
|---|---|---|
| | | |

Consider:

- internal documents
- runbooks
- incident records
- tickets
- embeddings
- vector database entries
- prompts
- model responses
- memory
- logs
- feedback
- tool credentials
- user identity context

## Step 3  -  Identify trust boundaries

Draw or list at least six trust boundaries.

Use this table:

| Boundary | Data/action crossing it | Why it matters |
|---|---|---|
| Browser → web app | | |
| Web app → LLM provider | | |
| Document store → retrieval service | | |
| Retrieval service → prompt builder | | |
| Model output → application logic | | |
| Model output → ticket connector | | |
| Memory service → prompt context | | |

## Step 4  -  Challenge assumptions

Review the current design assumptions.

For each unsafe assumption, explain what can go wrong.

| Assumption | Why unsafe? | Better assumption |
|---|---|---|
| Internal documents are trusted | | |
| Model will follow system prompt | | |
| Full prompts can be logged | | |

## Step 5  -  Write abuse cases

Create at least five abuse cases.

Use this format:

```text
As a malicious or compromised user,
I want to [abuse action],
so that [security impact].
```

Examples:

```text
As a low-privilege employee,
I want to ask the assistant questions that retrieve documents outside my permission scope,
so that I can access confidential operational data.
```

```text
As a malicious document author,
I want to hide instructions inside a runbook,
so that the assistant follows those instructions when another user retrieves the document.
```

## Step 6  -  Identify risks

Identify at least eight design-level risks.

Use this table:

| Risk | Component | Asset impacted | Impact | Likelihood | Priority |
|---|---|---|---|---|---|
| | | | | | |

Suggested risk areas:

- indirect prompt injection
- retrieval authorization failure
- cross-tenant or cross-team data leakage
- excessive tool privilege
- unsafe ticket updates
- memory poisoning
- sensitive data in logs
- unsafe output rendering
- weak auditability
- feedback poisoning
- no rollback or incident response
- overreliance during incidents

## Step 7  -  Define security requirements

For each high-priority risk, define one or more security requirements.

Use this table:

| Risk | Security requirement | Control owner |
|---|---|---|
| Unauthorized document retrieval | Retrieval must enforce document ACLs before context insertion | Retrieval service |
| Unsafe ticket update | Ticket updates require per-action authorization and human approval | Tool broker / workflow |

## Step 8  -  Propose mitigations

Create a mitigation plan.

Classify each mitigation as:

- prevent
- detect
- respond
- recover

| Mitigation | Type | Risk reduced | Trade-off |
|---|---|---|---|
| | | | |

## Step 9  -  Write residual risk

Write a short residual risk statement.

Use this format:

```text
After applying the proposed controls, the main remaining risks are...
These risks are acceptable/not acceptable because...
The system should be monitored for...
The risk owner should review this again when...
```

## Expected strong findings

A strong review should identify risks such as:

1. Internal documents are not automatically trusted; they can carry malicious instructions.
2. Retrieval must enforce user authorization before prompt construction.
3. The model should not decide whether ticket updates are authorized.
4. Tool credentials must be scoped and mediated by a tool broker.
5. Memory can be poisoned and should not automatically become trusted instruction context.
6. Full prompt/response logging can create sensitive data retention problems.
7. Feedback can be manipulated and should not directly retrain or tune behavior without validation.
8. Output should be treated as untrusted and encoded before rendering.
9. Incident workflows need approval gates and rollback.
10. Monitoring should include abnormal retrieval, repeated denied tool calls, high token usage, prompt injection indicators, and suspicious memory writes.

## Submission format

Submit your review as Markdown using the architecture risk review template:

```text
../../course-templates/architecture-risk-review-template.md
```
