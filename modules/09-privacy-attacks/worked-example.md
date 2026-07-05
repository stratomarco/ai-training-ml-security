# Worked example: Cross-tenant privacy leakage finding

## Weak finding

Chris can ask for payment token information and the AI returns alpha data. Retrieval authorization should be enabled.

## Why this is weak

It names the symptom and a likely control, but it does not explain the boundary, evidence, validation, or residual risk. It also ignores logs and traces.

## Strong finding

**Finding:** Retrieval context construction allows beta users to receive alpha restricted documents.

**Evidence:** With `ENABLE_RETRIEVAL_AUTHZ=false`, user `chris` from tenant beta can query for payment or credential terms and receive alpha restricted context from `DOC-002`. The response path exposes a fake restricted fragment, `FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE`, showing that tenant isolation is not enforced before model context construction.

**Root cause:** Retrieval runs across documents without applying tenant, role, and classification filters before context is sent to the model.

**Impact:** The AI application can act as a cross-tenant disclosure proxy. A user who cannot directly read an alpha restricted document can still receive sensitive content through retrieval and summarization.

**Remediation:** Enforce tenant, role, classification, and user-specific authorization in the retriever before context construction. Add privacy regression tests for cross-tenant queries. Apply redaction and access control to traces that store retrieved context.

**Validation:** Re-run the same beta query with `ENABLE_RETRIEVAL_AUTHZ=true`. The result set should exclude `DOC-002` and `DOC-006`. Inspect audit logs and traces to confirm unauthorized restricted fragments are not retained in raw form.

**Residual risk:** Retrieval authorization blocks this direct leakage path, but membership inference, log retention, support exports, and aggregated analytics still require separate privacy controls.

## Instructor note

This example should be used to teach that privacy findings are boundary findings. The best answer is not "the model leaked." The best answer is "the system placed unauthorized restricted context in front of the model."

## What an excellent submission adds

An excellent submission adds a second observation after the retrieval fix: whether audit logs, traces, or support exports still contain the fake restricted fragment. This turns the lab from a simple authorization exercise into a privacy architecture review.

The best answer also separates customer-facing impact from internal exposure. Blocking the response to Chris protects one path. It does not automatically prove that developers, support users, or analytics tools cannot see the same data through retained traces.
