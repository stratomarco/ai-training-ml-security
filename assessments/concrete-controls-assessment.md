# Concrete Controls Assessment Model

The course should reward students for designing controls, not only identifying vulnerabilities.

## Assessment principle

A good finding should answer:

1. What can go wrong?
2. Why is it possible?
3. What security property is violated?
4. What is the impact?
5. What control would prevent or detect it?
6. Who owns the control?
7. How would an engineer implement it?
8. What residual risk remains?

## New required deliverables

Add at least one concrete control deliverable to Modules 06, 07, 08, 11, and 12.

| Module | Concrete deliverable |
|---|---|
| 06 — RAG Security | Retrieval authorization rule set |
| 07 — Agent and Tool Security | Tool permission matrix + approval policy |
| 08 — Secure MLOps | Model registry access control and provenance policy |
| 11 — AI Red Team | Remediation-ready finding with control owner |
| 12 — BrokenPilot | Remediation backlog with implementable controls |

## Rubric

| Score | Description |
|---:|---|
| 1 | Identifies issue but gives vague mitigation |
| 2 | Describes mitigation but lacks owner, enforcement point, or implementation detail |
| 3 | Provides specific control with owner and enforcement point |
| 4 | Provides implementable control with validation and residual risk |
| 5 | Provides implementable control, detection, rollout plan, and tradeoff analysis |

## Example: weak mitigation

> Add better guardrails to prevent prompt injection.

Problem: this does not specify what control exists, where it runs, who owns it, or how it is tested.

## Example: stronger mitigation

> Add a retrieval authorization filter in the RAG service before chunks are added to model context. The filter must evaluate `user_id`, `tenant_id`, `document_acl`, `document_sensitivity`, and `purpose`. Chunks failing authorization must not be passed to the LLM. Denied retrieval attempts should be logged with user, document ID, policy rule, and request ID, but not full document content. The platform team owns the service control; application teams own document ACL accuracy. Validate with cross-tenant test cases before release.

This is stronger because it identifies the control, enforcement point, data needed, owner, logging rule, and validation method.
