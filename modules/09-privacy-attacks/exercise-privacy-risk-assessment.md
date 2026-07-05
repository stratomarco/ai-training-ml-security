# Exercise  -  AI Privacy Risk Assessment

## Scenario

You are reviewing **PeopleAssist**, an internal HR assistant used by managers and HR staff.

PeopleAssist can:

- answer HR policy questions;
- summarize employee support cases;
- search performance-review notes;
- answer questions about benefits and leave;
- summarize salary-band guidance;
- create draft HR tickets;
- remember user preferences;
- log prompts and model responses for quality improvement.

The company wants to release PeopleAssist to all managers next month.

## Architecture

```text
manager or HR user
  |
  v
PeopleAssist web app
  |
  +-- model gateway
  +-- prompt/completion log store
  +-- retrieval service
  |     +-- vector database
  |     +-- HR policy documents
  |     +-- employee case summaries
  |     +-- performance review excerpts
  |
  +-- ticket creation tool
  +-- assistant memory store
  +-- analytics and feedback queue
```

## Current assumptions

The team tells you:

1. The model provider says customer prompts are not used for foundation-model training by default.
2. The vector database is internal-only.
3. Prompt logs are useful for debugging.
4. HR managers already have access to some employee data.
5. The assistant has a system prompt that says: “Never reveal sensitive personal information.”
6. Source documents have permissions, but the ingestion pipeline currently strips most ACL metadata.
7. The vector database stores chunks with department and document type, but not full document permissions.
8. Prompt and completion logs are retained for one year.
9. The assistant memory store has no expiry.
10. Feedback examples may be used later for evaluation or fine-tuning.

## Student task

Create a privacy risk assessment.

Your assessment must include:

1. Sensitive data inventory.
2. Data-flow map.
3. Privacy abuse cases.
4. Attack paths.
5. Current control weaknesses.
6. Recommended mitigations.
7. Residual risk statement.

## Questions to answer

### Sensitive data

- What sensitive data does PeopleAssist process?
- What sensitive data does it generate?
- What sensitive data does it store indirectly?
- Which data is personal, confidential, regulated, or high-impact?

### Data flows

- Where do prompts go?
- Where do completions go?
- What gets embedded?
- What gets logged?
- What enters feedback?
- What is stored in memory?
- What can be deleted?

### Privacy abuse cases

Write at least five.

Examples:

- Manager retrieves performance notes for employees outside their reporting line.
- User asks indirect questions to infer salary or health-related leave information.
- Prompt logs expose employee case details to engineers.
- Vector retrieval returns another department's sensitive case summary.
- Assistant memory stores private HR details and reuses them later.

### Required mitigations

Your mitigation plan should address:

- data minimization;
- retrieval authorization;
- source ACL preservation;
- tenant/user/role metadata on chunks;
- prompt and completion log governance;
- retention and deletion;
- feedback governance;
- memory governance;
- output privacy review;
- auditability;
- incident response.

## Deliverable format

Use:

- `course-templates/privacy-risk-assessment-template.md`

## Grading guidance

A strong answer does not only say “redact PII.”

A strong answer explains:

- where sensitive data exists;
- why the current design exposes it;
- which controls must be placed before retrieval, before model access, before logging, and before feedback reuse;
- what residual risk remains after mitigation.
