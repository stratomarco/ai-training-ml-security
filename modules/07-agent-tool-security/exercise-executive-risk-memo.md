# Exercise  -  Executive Risk Memo for Agentic AI

## Purpose

This exercise forces students to explain agent/tool risk to leadership without relying on jargon or exploit screenshots.

## Scenario

Your company wants to deploy an internal AI operations agent. The agent can:

- Search internal documentation
- Summarize incidents
- Read tickets
- Create tickets
- Update ticket priority
- Query configuration data
- Store memory across conversations

The engineering team wants to ship quickly because the agent saves time during incident response.

The security team is concerned about excessive agency, tool misuse, indirect prompt injection, and weak auditability.

## Task

Write a one-page memo to a fictional CISO.

The memo must include:

1. The business benefit.
2. The top three security risks.
3. A realistic example of how one risk could happen.
4. The minimum controls required before launch.
5. What can be deferred.
6. The residual risk after controls.
7. A recommendation: launch, limited pilot, or delay.

## Constraints

- Do not use more than one page.
- Do not rely on OWASP numbering.
- Do not write like a vulnerability scanner report.
- Include a clear decision recommendation.

## Strong answer characteristics

A strong memo:

- Makes the risk understandable to leadership.
- Connects the risk to business impact.
- Avoids fear-based language.
- Distinguishes launch blockers from improvements.
- Explains tradeoffs.
- Recommends a controlled path forward.

## Weak answer characteristics

A weak memo:

- Says only "prompt injection is possible."
- Lists vulnerabilities without business impact.
- Recommends blocking all AI usage.
- Recommends vague "guardrails" without concrete controls.
- Ignores usability and incident-response value.

## Suggested minimum controls

Students may propose different controls, but a reasonable minimum set includes:

- Least-privilege tool permissions
- Per-action authorization outside the model
- Human approval for destructive or high-impact actions
- Tool argument validation
- Audit logs for tool calls
- Memory review/reset controls
- Egress restrictions
- Pilot rollout with monitoring

## Deliverable

Submit the memo and a short appendix mapping each recommended control to the risk it reduces.

## Related template

Use `course-templates/executive-risk-memo-template.md` for a structured version of this exercise. Instructors can also compare student work against the strong and weak executive memo examples in `labs/brokenpilot/worked-examples/`.
