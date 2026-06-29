# LLM Application Security Checklist

Use this checklist during design review, security testing, or release readiness review for LLM-enabled applications.

## 1. System purpose

- [ ] The application purpose is clearly defined.
- [ ] The intended users are defined.
- [ ] The allowed actions are defined.
- [ ] The disallowed actions are defined.
- [ ] High-risk workflows are identified.
- [ ] Human approval requirements are documented.

## 2. Assets and data

- [ ] Sensitive data types are identified.
- [ ] Data classification is defined.
- [ ] Prompt data is classified.
- [ ] Retrieved context is classified.
- [ ] Tool results are classified.
- [ ] Logs are classified.
- [ ] Chat history retention is defined.
- [ ] Memory retention is defined.

## 3. Authentication and authorization

- [ ] Users are authenticated.
- [ ] User roles are defined.
- [ ] Tenant boundaries are enforced.
- [ ] Retrieval is authorized before context injection.
- [ ] Tool calls are authorized independently.
- [ ] Authorization does not rely on the model.
- [ ] Admin capabilities are separated from normal user capabilities.

## 4. Prompt and context handling

- [ ] System, developer, user, retrieved, and tool contexts are separated.
- [ ] Untrusted content is labeled.
- [ ] Retrieved content is treated as untrusted.
- [ ] The prompt does not include unnecessary sensitive data.
- [ ] Secrets are not included in prompts.
- [ ] Prompt templates are version-controlled.
- [ ] Prompt changes are reviewed.

## 5. Prompt injection resilience

- [ ] Direct prompt injection is tested.
- [ ] Indirect prompt injection is tested.
- [ ] RAG/document injection is tested.
- [ ] Tool-output injection is tested.
- [ ] The system remains safe when the prompt fails.
- [ ] Security decisions are enforced outside the model.

## 6. Output handling

- [ ] LLM output is treated as untrusted.
- [ ] Output is validated against schemas where possible.
- [ ] Output is encoded before rendering.
- [ ] Markdown/HTML rendering is sanitized.
- [ ] LLM output is not directly executed.
- [ ] LLM output is not directly used to build SQL or shell commands.
- [ ] Unsafe output is rejected or routed to review.

## 7. Tool and function calling

- [ ] Tools have narrow purpose.
- [ ] Tool arguments are schema-validated.
- [ ] Tool calls are logged.
- [ ] Tool calls have rate limits.
- [ ] Tool calls have timeout limits.
- [ ] Dangerous tools require approval.
- [ ] Destructive actions default to disabled or dry-run.
- [ ] Tool credentials are scoped.
- [ ] Tool results are treated as untrusted input.

## 8. Sensitive information disclosure

- [ ] Retrieval is filtered by user authorization.
- [ ] Cross-tenant retrieval is tested.
- [ ] PII/secret redaction is applied where appropriate.
- [ ] Logs avoid storing unnecessary sensitive data.
- [ ] System prompts do not contain secrets.
- [ ] Model responses are checked for sensitive output in high-risk flows.

## 9. Model denial of service and cost control

- [ ] Input size limits exist.
- [ ] Token budgets exist.
- [ ] Per-user rate limits exist.
- [ ] Per-tenant rate limits exist.
- [ ] Tool-call limits exist.
- [ ] Timeouts exist.
- [ ] Retry loops are bounded.
- [ ] Expensive workflows are monitored.
- [ ] Abuse patterns generate alerts.

## 10. Supply chain

- [ ] Model provider dependencies are documented.
- [ ] Local model artifacts are verified.
- [ ] Prompt templates are controlled.
- [ ] Dependencies are scanned.
- [ ] Plugins/tools are reviewed.
- [ ] Vector database configuration is reviewed.
- [ ] Third-party data sources are assessed.

## 11. Overreliance

- [ ] High-impact outputs require human verification.
- [ ] Generated code is tested before use.
- [ ] Generated security advice is reviewed.
- [ ] Summaries are linked to sources.
- [ ] Confidence and uncertainty are communicated.
- [ ] Users are trained on limitations.

## 12. Monitoring and response

- [ ] Prompts and responses are logged safely.
- [ ] Tool calls are auditable.
- [ ] Retrieval sources are recorded.
- [ ] Policy denials are logged.
- [ ] Abuse alerts exist.
- [ ] Incident response procedures include LLM-specific events.
- [ ] The system can disable tools quickly.
- [ ] The system can roll back prompt or model changes.

## 13. Release readiness

- [ ] Threat model completed.
- [ ] Abuse cases reviewed.
- [ ] LLM-specific tests completed.
- [ ] Privacy review completed.
- [ ] Monitoring enabled.
- [ ] Rollback plan exists.
- [ ] Residual risk accepted by the right owner.
