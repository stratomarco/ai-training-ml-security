# Course Map

This file maps modules to frameworks, labs, deliverables, and core security principles.

## Module-to-framework map

| Module | OWASP ML Top 10 | OWASP LLM / GenAI | OWASP Agentic | BIML | NIST AI RMF / GenAI | MITRE ATLAS |
|---|---|---|---|---|---|---|
| 01 Security Engineering for AI | Partial | Partial | Partial | Strong | Strong | Partial |
| 02 ML System Architecture | Strong | Partial | Partial | Strong | Strong | Strong |
| 03 OWASP ML Top 10 | Strong | Partial | Partial | Strong | Partial | Strong |
| 04 BIML Risk Analysis | Strong | Strong | Strong | Strong | Strong | Partial |
| 05 LLM Application Security | Partial | Strong | Partial | Strong | Strong | Strong |
| 06 RAG Security | Partial | Strong | Strong | Strong | Strong | Strong |
| 07 Agent and Tool Security | Partial | Strong | Strong | Strong | Strong | Strong |
| 08 Secure MLOps | Strong | Strong | Partial | Strong | Strong | Strong |
| 09 Privacy Attacks | Strong | Strong | Partial | Strong | Strong | Strong |
| 10 Adversarial ML | Strong | Partial | Partial | Strong | Partial | Strong |
| 11 AI Red Team Methodology | Strong | Strong | Strong | Strong | Strong | Strong |
| 12 Capstone BrokenPilot | Strong | Strong | Strong | Strong | Strong | Strong |

## Module-to-lab map

| Module | Lab source | Lab type |
|---|---|---|
| 01 | Custom | Threat modeling tabletop |
| 02 | Custom | Architecture mapping |
| 03 | Custom toy ML app | Evasion, poisoning, extraction basics |
| 04 | Custom | Architecture risk review |
| 05 | DVAIA | Prompt injection and insecure output handling |
| 06 | DVAIA + custom RAG | Indirect prompt injection and retrieval auth |
| 07 | Vulnerable agent lab + BrokenPilot design | Tool misuse and excessive agency |
| 08 | Custom broken ML pipeline | Supply chain and MLOps review |
| 09 | Custom HR/customer-support RAG | Privacy leakage and cross-tenant retrieval |
| 10 | Custom classifier | Adversarial robustness |
| 11 | DVAIA + custom | Full AI red-team workflow |
| 12 | BrokenPilot | Capstone |

## Module-to-deliverable map

| Module | Deliverable |
|---|---|
| 01 | AI system context diagram and initial threat model |
| 02 | ML lifecycle data-flow diagram |
| 03 | ML attack summary and mitigation proposal |
| 04 | Architecture risk review |
| 05 | LLM vulnerability write-up |
| 06 | RAG threat model and mitigation design |
| 07 | Agent control design |
| 08 | Secure MLOps checklist and risk register |
| 09 | Privacy risk assessment |
| 10 | Adversarial test plan |
| 11 | AI red-team report |
| 12 | Capstone security review |

## Core security principles reused throughout the course

- Least privilege
- Complete mediation
- Fail-safe defaults
- Secure-by-default design
- Defense in depth
- Separation of duties
- Economy of mechanism
- Least astonishment
- Secure failure
- Explicit trust boundaries
- Input validation
- Output encoding
- Authentication and authorization
- Auditability
- Cryptographic key management
- Supply chain integrity
- Privacy by design
- Resilience and recoverability

## Repeated teaching pattern

For each topic, the instructor should connect four things:

1. Classic security principle
2. AI-specific failure mode
3. Practical exploit or abuse case
4. Engineering mitigation

Example:

```text
Classic principle: Least privilege
AI-specific failure: Agent has access to broad tools and data
Exploit: Prompt injection causes the agent to update a ticket or leak data
Mitigation: Per-action authorization, scoped tool tokens, approval gates, audit logs
```

## Current map status

This course map reflects the v1.0 release candidate. Modules 01–12 are complete, labs and templates are mapped to their modules, and BrokenPilot is the final capstone exercise. Historical build notes are tracked in `CHANGELOG.md`.
