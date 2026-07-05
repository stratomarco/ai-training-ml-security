> **Round 3 consolidation note:** This legacy paper lab is no longer the primary 40-hour course path. Use the BrokenPilot runnable lab for observable failure/fix behavior. Keep this file only as optional background or a discussion prompt.

# DVAIA Course Mapping

## Purpose

This file maps DVAIA-style labs to the **AI Training  -  ML Security** curriculum.

The goal is to use DVAIA as a hands-on substrate while keeping the course focused on security engineering, architecture, threat modeling, and practical mitigation.

DVAIA should not be treated as the curriculum itself. It is a lab environment. The course provides the explanation, framing, assessment, and secure design work around it.

## Safety boundary

Use DVAIA only in local, isolated, intentionally vulnerable, or explicitly authorized training environments.

Do not test prompt injection, model extraction, data leakage, or agent/tool abuse against real systems without authorization.

## Course mapping table

| DVAIA-style lab area | Course module | Primary concept | Security engineering connection | Likely OWASP mapping | Student outcome |
|---|---|---|---|---|---|
| Direct prompt injection | Module 05  -  LLM Application Security | User input manipulates model behavior | Input handling, trust boundaries, policy outside the model | LLM01 Prompt Injection | Explain why prompt-only controls are insufficient |
| System prompt leakage | Module 05 | Hidden instruction disclosure | Information disclosure, secrets handling | LLM06 Sensitive Information Disclosure | Distinguish prompt secrecy from real security controls |
| Insecure output handling | Module 05 | Model output used unsafely | Output encoding, validation, downstream injection | LLM02 Insecure Output Handling | Treat model output as untrusted output |
| Sensitive data disclosure | Module 05 / Module 09 | Model reveals confidential data | Access control, privacy, logging | LLM06 Sensitive Information Disclosure | Identify where data should have been blocked before model context |
| RAG prompt injection | Module 06  -  RAG Security | Retrieved content manipulates response | Untrusted input, context separation | LLM01 Prompt Injection | Treat retrieved documents as untrusted data |
| RAG data leakage | Module 06 / Module 09 | Unauthorized retrieval enters context | Authorization, tenant isolation, privacy | LLM06 Sensitive Information Disclosure | Design permission-aware retrieval |
| Poisoned knowledge base | Module 06 / Module 08 | Malicious or low-trust document affects answers | Supply chain, provenance, ingestion controls | LLM03 Training Data Poisoning / LLM05 Supply Chain | Track source trust and ingestion controls |
| Agent tool misuse | Module 07  -  Agent and Tool Security | Model causes unauthorized or unsafe action | Authorization, least privilege, approval gates | LLM07 Insecure Plugin Design / LLM08 Excessive Agency | Design tool boundaries outside the model |
| Excessive agency | Module 07 | Agent performs too much autonomously | Workflow security, human approval, fail-safe defaults | LLM08 Excessive Agency | Scope autonomy by risk level |
| Tool argument injection | Module 07 | Model sends unsafe arguments to tools | Schema validation, command/query safety | LLM02 / LLM07 | Validate tool calls deterministically |
| Model denial of service | Module 05 / Module 07 | Expensive prompts or loops exhaust resources | Rate limiting, quotas, circuit breakers | LLM04 Model Denial of Service | Add cost and resource controls |
| Model theft / extraction | Module 03 / Module 11 | API abuse to infer model behavior | Abuse monitoring, rate limits, IP protection | LLM10 Model Theft | Build query monitoring and throttling strategy |
| Overreliance | Module 05 / Module 11 | User trusts incorrect output | Human factors, safety-critical review | LLM09 Overreliance | Add source review, uncertainty, and human checks |
| Multi-modal manipulation | Module 05 / Module 10 | Non-text input influences behavior | Input validation, adversarial robustness | Depends on scenario | Expand threat model beyond text prompts |

## How to use a DVAIA lab in this course

Each lab should be wrapped with this structure:

1. **Security concept**  -  What are we teaching?
2. **System context**  -  What application are we testing?
3. **Asset at risk**  -  What could be harmed?
4. **Attack path**  -  What does the student observe in the lab?
5. **Root cause**  -  Why did the system allow it?
6. **Mitigation**  -  What would a real engineering fix look like?
7. **Residual risk**  -  What remains after the fix?
8. **Mapping**  -  Which OWASP/BIML/NIST/MITRE category does this relate to?

## Example lab wrapper

### Lab: Direct prompt injection

**Module:** Module 05  -  LLM Application Security

**Concept:** Prompts are not security boundaries.

**Scenario:** A chatbot has a system instruction that says it should not reveal internal information. A user attempts to override the instruction through crafted input.

**Root cause:** The system relies on model behavior instead of deterministic access control and context management.

**Defensive discussion:**

- Do not place secrets in prompts.
- Do not rely on prompt secrecy for access control.
- Enforce authorization before data reaches the model.
- Treat model refusal as one layer, not the main control.
- Log suspicious interaction patterns.

**Student deliverable:** Short lab report with vulnerability, impact, root cause, mitigation, and residual risk.

## Instructor notes

When students complete a lab, always ask:

1. What asset was at risk?
2. Which trust boundary failed?
3. Was the failure in the model, the application, the workflow, or the architecture?
4. What deterministic control would reduce impact?
5. What would you monitor in production?
6. What risk remains?

## Mapping to course modules

| Module | DVAIA role |
|---|---|
| Module 01  -  Security Engineering for AI | Use DVAIA examples only as motivation, not as the first hands-on lab |
| Module 02  -  ML System Architecture | Map where the lab component fits in the AI lifecycle |
| Module 03  -  OWASP ML Top 10 | Use only where classical ML attack behavior is represented |
| Module 04  -  BIML Risk Analysis | Use lab scenarios as concrete examples of architecture risks |
| Module 05  -  LLM Application Security | Main DVAIA usage begins here |
| Module 06  -  RAG Security | Use RAG and indirect injection labs |
| Module 07  -  Agent and Tool Security | Use agent/tool labs where available |
| Module 08  -  Secure MLOps and Supply Chain | Use supply chain or poisoning scenarios if available; otherwise use custom labs |
| Module 09  -  Privacy Attacks | Use data leakage and sensitive disclosure scenarios |
| Module 10  -  Adversarial ML and Robustness | Use custom toy ML labs more than DVAIA |
| Module 11  -  AI Red Team Methodology | Combine multiple DVAIA labs into an attack-chain exercise |
| Module 12  -  BrokenPilot Capstone | DVAIA concepts inform the custom capstone design |

## Gap analysis

DVAIA can support many LLM application and RAG security topics, but the course still needs custom material for:

- Classical ML poisoning and evasion
- Membership inference
- Model inversion
- Secure MLOps
- Model registry security
- Dataset provenance
- Agent workflow authorization at enterprise depth
- Full capstone architecture and reporting

## Next steps

1. Install DVAIA locally.
2. Inventory available labs.
3. Map each lab to a module and risk category.
4. Write a lab wrapper for each selected exercise.
5. Create instructor solution notes.
6. Decide which gaps require custom labs.
