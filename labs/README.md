# Labs

Labs are the hands-on substrate of the course. The first version should reuse existing vulnerable environments where possible, especially DVAIA for LLM application security.

The course value is not the vulnerable app itself. The course value is the explanation, mapping to frameworks, threat modeling, mitigation design, and assessment.

## Lab principles

Every lab must:

1. Map to a real engineering decision.
2. Explain the vulnerable behavior.
3. Explain the root cause.
4. Show the security impact.
5. Connect to OWASP, BIML, NIST, MITRE ATLAS, or classic security principles.
6. Provide mitigation options.
7. Discuss trade-offs.
8. Capture residual risk.

## Lab categories

| Folder | Purpose |
|---|---|
| [`dvaia-guides/`](dvaia-guides/) | Wrappers for DVAIA-style LLM application security exercises. |
| [`rag-labs/`](rag-labs/) | RAG and indirect prompt injection exercises. |
| [`agent-labs/`](agent-labs/) | Agent/tool security, memory poisoning, and approval-gate exercises. |
| [`toy-ml-attacks/`](toy-ml-attacks/) | Classical ML attack exercises. |
| [`mlops-supply-chain-labs/`](mlops-supply-chain-labs/) | Secure MLOps and AI supply chain review exercises. |
| [`privacy-labs/`](privacy-labs/) | Privacy leakage, cross-tenant RAG, membership inference, and model inversion tabletop exercises. |
| [`architecture-risk-review-labs/`](architecture-risk-review-labs/) | Architecture review tabletop exercises. |
| [`brokenpilot/`](brokenpilot/) | Final capstone paper design for an internal AI operations assistant. |

## Standard lab format

Use [`../templates/lab-guide-template.md`](../templates/lab-guide-template.md) for every lab.
