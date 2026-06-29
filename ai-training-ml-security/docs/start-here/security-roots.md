# Security Roots of ML Security

ML Security is not a new island. It is security engineering applied to systems where models, data, prompts, tools, memory, and automated actions become part of the attack surface.

This course deliberately connects modern AI risks to older and deeper security traditions.

## Core claim

> The model is not the security boundary.

Security properties must be enforced by architecture, authorization, policy, isolation, validation, monitoring, and operational control. A prompt can express intent, but it cannot replace security engineering.

## Classic roots

| Source | Course relevance |
|---|---|
| Saltzer and Schroeder | Design principles such as least privilege, complete mediation, fail-safe defaults, and psychological acceptability |
| Ross Anderson | Systems thinking, real-world security failures, incentives, economics, and operational constraints |
| Gary McGraw | Building security in, software security touchpoints, architectural risk analysis |
| Adam Shostack | Threat modeling as a practical engineering discipline |
| Jean-Philippe Aumasson | Applied cryptography, misuse-resistant thinking, and practical crypto engineering |
| OWASP | Practitioner taxonomies for web, API, ML, LLM, and agentic application risks |
| BIML | Architectural risk analysis for ML and LLM systems |
| NIST | Risk management, governance, secure development, privacy, and adversarial ML terminology |
| MITRE ATLAS | Adversarial AI tactics and techniques for red-team and blue-team alignment |

## How this applies to AI systems

AI adds new failure modes, but most practical failures still look familiar:

| Classic security problem | AI-era expression |
|---|---|
| Injection | Prompt injection, indirect prompt injection, unsafe model output used as code or commands |
| Confused deputy | Agent uses its own privilege to perform an action requested through untrusted context |
| Broken access control | RAG retrieves documents the user should not access |
| Insecure deserialization | Unsafe model artifact loading |
| Supply chain compromise | Poisoned datasets, malicious model weights, compromised adapters, untrusted prompts |
| Denial of service | Token exhaustion, recursive tool loops, expensive model calls |
| Data leakage | Prompt logs, embeddings, model memorization, cross-tenant retrieval |
| Over-privileged service account | Agent tool token can read or modify too much |
| Weak auditability | Tool calls and model decisions cannot be reconstructed after an incident |

## The course stance

A secure AI system should not rely on the model to decide what is safe. The model can assist with reasoning, classification, summarization, and workflow orchestration, but security-critical decisions need external controls.

Good AI security asks:

1. What is the asset?
2. Who is the actor?
3. What is the trust boundary?
4. What can the model influence?
5. What can the agent do?
6. What data is retrieved?
7. What policy exists outside the model?
8. What is logged?
9. What happens when the model is wrong?
10. What risk remains after controls?
