# Strong Risk Register Example — BrokenPilot

| ID | Risk | Scenario | Impact | Likelihood | Severity | Control | Owner | Residual risk |
|---|---|---|---|---|---|---|---|---|
| BP-R1 | Indirect prompt injection causes unsafe ticket update | Malicious document retrieved during incident summary instructs agent to lower priority | Incident response delay and audit failure | Medium | High | Treat retrieved docs as untrusted, external policy check, approval gate for priority changes | AI platform + Ops | Model may still summarize malicious content misleadingly |
| BP-R2 | Cross-tenant retrieval leaks restricted docs | Vector search returns chunks without checking document ACL at retrieval time | Confidential data exposure | Medium | High | Retrieval-time authorization using tenant, user, role, document ACL, sensitivity | Platform | Metadata errors can still cause incorrect access |
| BP-R3 | Agent memory persists malicious instruction | Attacker plants instruction that affects future sessions | Long-lived workflow compromise | Medium | Medium | Memory write approval, memory scope, memory review and reset | AI platform | User-approved bad memory remains possible |
