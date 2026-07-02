# BrokenPilot Instructor Solution Guide

This guide is intended for instructors. It should not be given to students before the capstone.

## Expected student path

Strong students should move through the following pattern:

1. Understand business purpose.
2. Map architecture and trust boundaries.
3. Identify assets and attacker goals.
4. Recognize that BrokenPilot is an AI-enabled application, not a model-only problem.
5. Demonstrate a few representative attacks.
6. Explain root causes in security engineering language.
7. Propose controls that preserve usability and developer velocity.
8. Communicate residual risk.

## Minimum expected findings

A passing submission should identify at least:

1. Prompt injection risk.
2. RAG authorization risk.
3. Tool authorization/confused-deputy risk.
4. Missing approval gates for high-risk actions.
5. Memory poisoning or insecure persistent context.
6. Audit/logging gaps.

## Strong expected findings

A strong submission should also identify:

- Unsafe feedback loops from tickets into RAG.
- Insecure output handling.
- Overreliance on incident summaries.
- Sensitive config disclosure.
- Privacy leakage through logs.
- Model/tool DoS risk.
- Missing provenance for prompts, model versions, retrieval indexes, and policy versions.
- Need for risk-tiered action policy.

## Instructor scoring guidance

Grade higher when students:

- Identify trust boundaries precisely.
- Connect findings to classic security principles.
- Avoid relying only on prompt filters.
- Separate model behavior from system authorization.
- Provide realistic mitigations.
- Explain trade-offs.
- Communicate clearly to engineering and leadership.

Grade lower when students:

- Only list prompt-injection payloads.
- Treat the system as if the model alone is responsible.
- Propose vague controls such as "use a better model" or "improve the prompt".
- Ignore authorization and auditability.
- Ignore usability and operational velocity.

## Expected finding examples

### Finding 1  -  RAG authorization bypass

**Observation:** A user can receive summaries of documents outside their team because vector retrieval returns semantically similar chunks without checking access metadata.

**Root cause:** Authorization is not enforced at the retrieval layer. Chunks do not reliably preserve source document permissions.

**Impact:** Cross-team data disclosure, possible security ticket leakage, incident information leakage.

**Mitigation:** Metadata-preserving chunking, pre-retrieval authorization filters, post-retrieval checks, separate indexes for high-sensitivity domains, tests for cross-team leakage.

### Finding 2  -  Tool confused deputy

**Observation:** BrokenPilot can update a ticket using a broad service account even when the real user cannot perform that update directly.

**Root cause:** The tool gateway authorizes the assistant rather than the user/action/object tuple.

**Impact:** Unauthorized ticket tampering, priority manipulation, false operational status, workflow abuse.

**Mitigation:** Delegated user identity, scoped tokens, per-action authorization, approval gates for high-risk actions, full audit trail.

### Finding 3  -  Memory poisoning

**Observation:** The assistant stores persistent instructions without explicit confirmation or expiry.

**Root cause:** Memory is treated as trustworthy context rather than untrusted persistent state.

**Impact:** Long-lived manipulation of future responses or tool choices.

**Mitigation:** User confirmation, provenance, scope, expiry, review UI, memory never overrides policy, suspicious-memory detection.

### Finding 4  -  Insecure output handling

**Observation:** Generated Markdown or HTML is rendered without adequate safety treatment.

**Root cause:** Model output is treated as trusted UI content.

**Impact:** Misleading links, unsafe copy/paste commands, UI manipulation, possible XSS depending on renderer.

**Mitigation:** Safe rendering, sanitization, command warning UI, generated-content labels, no automatic execution.

### Finding 5  -  Overreliance on incident summary

**Observation:** BrokenPilot produces confident incident summaries without showing source freshness, missing data, or uncertainty.

**Root cause:** The product workflow treats generated summaries as authoritative.

**Impact:** Wrong operational decisions, delayed response, incorrect customer communication.

**Mitigation:** Mark summaries as drafts, show source citations, require human review, display freshness and uncertainty.

## Expected secure design themes

Students should recommend:

1. Policy enforcement outside the model.
2. Per-user, per-action, per-object authorization.
3. Risk-tiered approval gates.
4. Source-labeled RAG context.
5. Retrieval authorization.
6. Memory provenance and expiry.
7. Tool schema validation.
8. Sandboxed tools.
9. Rate limits and token budgets.
10. Security logging and detection.
11. Data minimization and redaction.
12. Prompt/model/index versioning.
13. Clear UI for draft/generated content.
14. Human review for customer-visible or high-impact actions.

## Suggested discussion prompts

Ask students:

- Which control would you implement first and why?
- Which issue is highest impact but hardest to exploit?
- Which issue is easiest to exploit but lower impact?
- How would you keep the assistant useful after adding approval gates?
- What would you log, and what would you avoid logging for privacy reasons?
- Which actions should BrokenPilot never be allowed to perform?
- How would your answer change for customer-facing AI?
- How would your answer change for production infrastructure access?

## Model answer: executive summary shape

A strong executive summary should sound like this:

> BrokenPilot creates useful operational leverage, but its current architecture gives the model too much influence over data access and tool execution. The highest risks are unauthorized retrieval, model-mediated ticket updates, indirect prompt injection from retrieved content, and persistent memory poisoning. These are not solved by prompt tuning alone. We recommend enforcing authorization outside the model, applying document-level retrieval controls, adding risk-tiered approval gates for tools, making memory inspectable and expiring, and improving audit logs for model-mediated actions. With these changes, BrokenPilot can remain useful for summarization and drafting while reducing the chance that untrusted content or compromised users cause unauthorized actions.
