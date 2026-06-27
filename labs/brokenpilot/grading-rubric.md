# BrokenPilot Grading Rubric

## Total score: 100 points

| Area | Points |
|---|---:|
| Architecture understanding | 10 |
| Asset and trust-boundary identification | 12 |
| Threat model and abuse cases | 15 |
| Vulnerability discovery | 15 |
| Attack explanation and evidence | 10 |
| Mitigation quality | 15 |
| Secure reference architecture | 8 |
| Residual risk reasoning | 8 |
| Communication quality | 7 |

## 1. Architecture understanding — 10 points

Strong submissions:

- Explain the end-to-end BrokenPilot workflow.
- Identify UI, API, model gateway, retrieval service, vector DB, tool gateway, memory, and logging.
- Explain what the assistant can see and do.

Weak submissions:

- Describe BrokenPilot only as a chatbot.
- Ignore tools, retrieval, memory, or logging.

## 2. Asset and trust-boundary identification — 12 points

Strong submissions identify:

- Internal documents.
- Tickets.
- Incidents.
- Service configuration.
- Memory.
- Tool permissions.
- Prompts and policies.
- Logs.
- Model/retrieval index versions.

They also identify trust boundaries between user input, retrieved content, model context, tools, and backend systems.

## 3. Threat model and abuse cases — 15 points

Strong submissions include:

- At least three attacker personas.
- Realistic abuse cases.
- Data-flow diagram.
- Security assumptions.
- Prioritized risks.

High-quality submissions connect abuse cases to classic security principles.

## 4. Vulnerability discovery — 15 points

Strong submissions identify issues across multiple categories:

- Prompt injection.
- Indirect prompt injection.
- RAG authorization failure.
- Tool confused deputy.
- Excessive agency.
- Memory poisoning.
- Sensitive disclosure.
- Insecure output handling.
- Audit gaps.
- Overreliance.

Full credit does not require finding every issue. It requires breadth and depth.

## 5. Attack explanation and evidence — 10 points

Strong submissions explain:

- What was attempted.
- What happened.
- Why it matters.
- Which trust boundary failed.
- Which evidence supports the finding.

Screenshots or payloads alone are not enough.

## 6. Mitigation quality — 15 points

Strong mitigations are:

- Practical.
- Specific.
- Mapped to root cause.
- Prioritized.
- Usable by engineering teams.

Expected controls include:

- Policy outside the model.
- Retrieval authorization.
- Per-action tool authorization.
- Risk-tiered approval gates.
- Memory provenance and expiry.
- Safe output handling.
- Audit logging.
- Rate limits and budgets.

## 7. Secure reference architecture — 8 points

Strong submissions show a target design with:

- Deterministic policy layer.
- Authorized retrieval.
- Source-labeled context.
- Tool gateway with authorization and approval.
- Audit and monitoring.
- Clear ownership.

## 8. Residual risk reasoning — 8 points

Strong submissions explain what remains unsafe after mitigations.

Examples:

- Prompt injection cannot be fully eliminated.
- RAG can still retrieve stale content.
- Human approval can fail.
- Strong controls can reduce speed.
- Logs can create privacy risk.

## 9. Communication quality — 7 points

Strong submissions include:

- Clear executive summary.
- Developer-focused recommendations.
- Leadership-level risk framing.
- No unnecessary hype.
- Clear trade-offs.

## Grade bands

| Score | Meaning |
|---|---|
| 90–100 | Excellent: strong architecture reasoning, realistic controls, clear communication. |
| 75–89 | Good: finds major issues and proposes reasonable fixes. |
| 60–74 | Acceptable: understands main risks but lacks depth or prioritization. |
| <60 | Needs improvement: too focused on prompts, missing architecture/security fundamentals. |
