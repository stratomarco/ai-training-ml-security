# BrokenPilot Module Mapping

BrokenPilot is the course capstone. It should force students to reuse ideas from every previous module.

## Module mapping

| Module | BrokenPilot connection | Student evidence |
|---|---|---|
| 01  -  Security Engineering for AI | Threat modeling, trust boundaries, least privilege, secure design. | System context diagram and threat model. |
| 02  -  ML System Architecture | AI lifecycle, retrieval, tools, memory, monitoring. | Architecture and data-flow diagram. |
| 03  -  OWASP ML Security Top 10 | Model theft, poisoning, output integrity, supply chain concepts. | Risk mapping and attack summaries. |
| 04  -  BIML Architectural Risk Analysis | Design-level failures and abuse cases. | Architecture risk review. |
| 05  -  LLM Application Security | Prompt injection, output handling, overreliance, DoS. | LLM findings and mitigations. |
| 06  -  RAG Security | Indirect prompt injection, retrieval authorization, source trust. | RAG threat model and retrieval-control design. |
| 07  -  Agent and Tool Security | Tool misuse, excessive agency, memory poisoning, approval gates. | Agent control design and tool permission matrix. |
| 08  -  Secure MLOps and Supply Chain | Model/prompt/index provenance, artifact control, ingestion pipeline. | MLOps risk register and provenance recommendations. |
| 09  -  Privacy Attacks | Sensitive disclosure, logs, cross-team data access, minimization. | Privacy risk assessment. |
| 10  -  Adversarial ML and Robustness | Robustness, abuse monitoring, failure modes under adversarial pressure. | Adversarial test plan. |
| 11  -  AI Red Team Methodology | Scope, attack chains, reporting, residual risk. | Red-team report. |
| 12  -  Capstone | End-to-end synthesis. | Final security review and leadership presentation. |

## Framework mapping

| BrokenPilot issue | OWASP ML | OWASP LLM/GenAI | OWASP Agentic | BIML-style ARA | NIST AI RMF / GenAI | MITRE ATLAS |
|---|---|---|---|---|---|---|
| Direct prompt injection | Partial | Strong | Strong | Strong | Strong | Strong |
| Indirect prompt injection | Partial | Strong | Strong | Strong | Strong | Strong |
| RAG authorization bypass | Partial | Strong | Strong | Strong | Strong | Partial |
| Tool confused deputy | Partial | Strong | Strong | Strong | Strong | Strong |
| Excessive agency | Partial | Strong | Strong | Strong | Strong | Strong |
| Memory poisoning | Partial | Strong | Strong | Strong | Strong | Partial |
| Unsafe ingestion feedback loop | Strong | Strong | Partial | Strong | Strong | Strong |
| Sensitive disclosure | Strong | Strong | Strong | Strong | Strong | Strong |
| Weak auditability | Partial | Strong | Strong | Strong | Strong | Partial |
| Model/tool DoS | Partial | Strong | Strong | Strong | Strong | Strong |
| Supply-chain/provenance gaps | Strong | Strong | Partial | Strong | Strong | Strong |

## Deliverable mapping

| Deliverable | Template |
|---|---|
| Threat model | `course-templates/threat-model-template.md` |
| Abuse cases | `course-templates/abuse-case-template.md` |
| Risk register | `course-templates/risk-register-template.md` |
| Red-team report | `course-templates/red-team-report-template.md` |
| Residual-risk statement | `course-templates/residual-risk-template.md` |
| Agent control design | `course-templates/agent-control-design-template.md` |
| Tool permission matrix | `course-templates/tool-permission-matrix-template.md` |
| Approval policy | `course-templates/agent-action-approval-policy-template.md` |
| RAG threat model | `course-templates/rag-threat-model-template.md` |
| Architecture review | `course-templates/architecture-risk-review-template.md` |
