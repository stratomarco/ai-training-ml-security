# Exercise — LLM Application Security Review

## Scenario

Your team is reviewing **SupportPilot**, an internal LLM assistant used by support and engineering teams.

SupportPilot can:

- answer questions using internal support documentation
- summarize customer tickets
- search historical incidents
- draft customer replies
- classify ticket urgency
- suggest remediation steps
- create follow-up engineering tickets

The system has the following components:

```text
Support user
  -> Web app
  -> LLM gateway
  -> Prompt builder
  -> Vector database with support docs
  -> Ticket API
  -> Incident API
  -> Draft reply generator
  -> Ticket creation tool
  -> Audit logs
```

## Current design

The current implementation has these design decisions:

1. The application retrieves the top 10 most relevant documents from the vector database for every question.
2. Documents are retrieved based only on semantic similarity.
3. The prompt includes a system instruction: “Never reveal confidential information.”
4. The model can create follow-up tickets directly.
5. The model can set ticket priority.
6. Draft customer replies are rendered as Markdown in the browser.
7. The application logs full prompts and full model responses.
8. There is no per-tool approval gate.
9. There is rate limiting per IP address, but not per user or tenant.
10. Support managers trust the ticket priority suggested by the assistant.

## Student tasks

### Task 1 — Identify assets

List at least five assets in this system.

Examples:

- customer data
- support tickets
- incident history
- internal documentation
- model prompt templates
- generated replies
- ticket creation capability
- logs

### Task 2 — Identify trust boundaries

Draw or describe the trust boundaries between:

- user and web app
- web app and LLM gateway
- LLM gateway and model provider/local model
- application and vector database
- application and ticket API
- model output and browser renderer
- model output and ticket creation tool

### Task 3 — Map vulnerabilities

Find at least six likely vulnerabilities or weaknesses.

Use this table:

| Finding | Component | Attacker control | Impact | Root cause |
|---|---|---|---|---|
| | | | | |

### Task 4 — Map to LLM risk categories

Map your findings to categories such as:

- prompt injection
- indirect prompt injection
- insecure output handling
- sensitive information disclosure
- model denial of service
- supply chain risk
- excessive agency
- overreliance
- model theft

### Task 5 — Design mitigations

For each finding, propose a mitigation.

Use this table:

| Finding | Weak mitigation | Better mitigation | Where control should live |
|---|---|---|---|
| | | | |

### Task 6 — Residual risk

Write a short residual risk statement.

Include:

- what remains risky
- what is accepted
- what requires monitoring
- what requires future work

## Expected findings

Students may identify:

### Broad retrieval without authorization

Problem:

Documents are retrieved only by semantic similarity.

Impact:

A user may receive context from documents they are not authorized to access.

Better control:

Authorize documents before retrieval or filter retrieval results by user/tenant permissions before adding them to context.

### Prompt as data protection control

Problem:

“Never reveal confidential information” is used as a primary control.

Impact:

Prompt injection or model failure can expose sensitive data.

Better control:

Do not put unauthorized sensitive data into the prompt.

### Excessive agency

Problem:

The model can create tickets and set priority directly.

Impact:

An attacker can manipulate workflow state or cause operational noise.

Better control:

Use a tool gateway, approval gates, and per-action authorization.

### Insecure Markdown rendering

Problem:

Generated Markdown is rendered in the browser.

Impact:

Unsafe HTML/Markdown could become XSS or phishing content.

Better control:

Use safe rendering, sanitization, output encoding, and content security policy.

### Sensitive prompt logging

Problem:

Full prompts and responses are logged.

Impact:

Logs may store customer data, secrets, or confidential context.

Better control:

Redact, minimize, classify, and protect logs.

### Weak rate limiting

Problem:

Rate limiting only by IP address.

Impact:

A user or tenant can cause high cost or degrade service.

Better control:

Use per-user, per-tenant, per-tool, and per-token budget controls.

### Overreliance on priority classification

Problem:

Support managers trust assistant-generated priority.

Impact:

Manipulated or incorrect priority decisions may affect incident response.

Better control:

Use confidence thresholds, explanations, verification, and human review for high-impact decisions.

## Deliverable

Submit:

1. One-page threat summary
2. Vulnerability table
3. Mitigation table
4. Residual risk statement

## Debrief questions

1. Which finding had the highest business impact?
2. Which control should be implemented first?
3. Which risks can be mitigated with prompts?
4. Which risks require architecture changes?
5. Which risks require human process changes?
6. What telemetry would detect abuse?
