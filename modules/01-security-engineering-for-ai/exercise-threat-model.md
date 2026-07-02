# Exercise  -  Threat Model DocAssist

## Exercise purpose

This exercise teaches students to threat model an AI-enabled application using classic security engineering principles.

The goal is not to find clever jailbreak strings. The goal is to identify assets, trust boundaries, abuse cases, and practical mitigations.

## Scenario

Your company is building **DocAssist**, an internal AI assistant that helps employees search and summarize internal documents.

Employees can ask questions such as:

- “Summarize the onboarding policy.”
- “What is the deployment process for Service A?”
- “Find the incident response runbook for database outages.”
- “What did the architecture review say about Project Falcon?”

The product team wants DocAssist to improve productivity and reduce the time engineers spend searching documentation.

## System capabilities

DocAssist can:

- Authenticate employees through the company identity provider.
- Search internal documents.
- Retrieve document snippets from a vector database.
- Send the user question and retrieved snippets to an LLM.
- Return a summarized answer with source links.
- Store chat history.
- Log prompts, retrieved snippets, model responses, and errors.

## Simplified architecture

```text
employee browser
  |
  v
DocAssist web app
  |
  +-- identity provider
  +-- document permission service
  +-- document store
  +-- ingestion pipeline
  +-- embedding service
  +-- vector database
  +-- LLM gateway
  +-- chat history database
  +-- logs and monitoring
```

## Assumptions

Use these assumptions unless your instructor changes them:

1. Employees have different document permissions.
2. Some documents contain confidential project information.
3. Some documents contain customer or employee information.
4. The vector database stores embeddings and document chunks.
5. The first prototype uses one backend service account to access the document store.
6. The app logs prompts, responses, and retrieved chunks for debugging.
7. The LLM is accessed through an internal model gateway or external provider.
8. The assistant cannot modify documents yet.
9. The product team wants to ship quickly.

## Student tasks

### Task 1  -  Identify assets

List at least eight assets.

Examples:

- Documents
- Embeddings
- Logs
- User identity
- Service account credentials

Add your own.

### Task 2  -  Identify actors

List legitimate users, privileged users, attackers, and system operators.

Consider:

- Normal employee
- Employee with limited access
- Malicious insider
- External attacker with compromised account
- Admin
- Developer/operator
- Model provider or dependency

### Task 3  -  Draw trust boundaries

Draw a simple diagram or list boundaries such as:

- Browser to application
- Application to identity provider
- Application to document store
- Application to vector database
- Application to LLM gateway
- Application to logging system

### Task 4  -  Write abuse cases

Write at least five abuse cases in this format:

```text
As an attacker, I want to [action], so that [impact].
```

Examples:

```text
As an employee with limited access, I want DocAssist to summarize documents I cannot directly open, so that I can read confidential project information.
```

```text
As a malicious insider, I want to place instructions inside a document that DocAssist retrieves, so that the assistant follows my instructions instead of the system instructions.
```

### Task 5  -  Identify root causes

For each abuse case, identify likely root causes.

Root cause examples:

- Retrieval does not enforce user authorization.
- Retrieved content is treated as trusted instruction.
- The assistant uses an overly broad service account.
- Logs store sensitive data without access controls.
- Model output is rendered without validation or encoding.
- There is no monitoring for unusual document access.

### Task 6  -  Propose mitigations

For each abuse case, propose at least one mitigation.

Prefer mitigations that are:

- Enforced outside the model
- Testable
- Auditable
- Fail-closed
- Reasonable for developer velocity

### Task 7  -  Discuss residual risk

Write a short residual risk statement.

Use this format:

```text
After applying the proposed controls, the remaining risk is [low/medium/high] because [...]. We accept or do not accept this risk because [...]. Additional work should include [...].
```

## Expected findings

Students should find several of these:

| Risk | Example |
|---|---|
| Broken retrieval authorization | User receives snippets from documents they cannot access |
| Prompt injection | User asks the assistant to ignore instructions or reveal hidden context |
| Indirect prompt injection | A document contains instructions that manipulate the model |
| Sensitive logging | Prompts and retrieved snippets expose confidential data in logs |
| Cross-tenant or cross-team leakage | Search returns documents from the wrong business unit |
| Overbroad service account | Backend can access more documents than the user |
| Unsafe output rendering | Model output contains unsafe HTML or links |
| Weak retention | Chat history stores sensitive data indefinitely |
| Lack of monitoring | No alerting on unusual retrieval patterns |
| Weak incident response | No clear process after data exposure |

## Suggested mitigations

| Control | Purpose |
|---|---|
| Per-user retrieval authorization | Prevent unauthorized documents from entering context |
| Permission-aware indexing | Avoid returning chunks the user cannot access |
| Scoped service accounts | Limit backend blast radius |
| Treat retrieved content as data | Avoid following instructions from documents |
| Prompt construction with source labeling | Separate system instructions, user input, and retrieved content |
| Output encoding and validation | Prevent unsafe rendering or downstream injection |
| Sensitive log controls | Reduce exposure through prompts, responses, and retrieved snippets |
| Rate limiting | Reduce scraping, extraction, and cost abuse |
| Audit logs | Support detection and investigation |
| Retention policy | Avoid indefinite storage of sensitive interactions |
| Human review for high-impact answers | Reduce overreliance in sensitive workflows |

## Submission format

Submit one Markdown file with:

```text
# DocAssist Threat Model

## System diagram

## Assets

## Actors

## Trust boundaries

## Abuse cases

## Root causes

## Mitigations

## Residual risk
```

## Instructor evaluation rubric

| Criteria | Strong answer | Weak answer |
|---|---|---|
| Assets | Includes data, credentials, logs, embeddings, user context | Only mentions documents |
| Trust boundaries | Identifies model, retrieval, logs, identity, data stores | Only draws user/app/model |
| Abuse cases | Concrete attacker goals and business impact | Generic “jailbreak the model” statements |
| Root cause | Links abuse to architecture | Blames the model only |
| Mitigations | Enforceable, layered, practical | “Improve the prompt” only |
| Residual risk | Honest and specific | Missing or vague |
