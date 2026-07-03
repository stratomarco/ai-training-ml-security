# Module 5  -  LLM Application Security

## Purpose

This module teaches LLM application security as **application security plus model-mediated behavior**.

The goal is not to teach a bag of jailbreak tricks. The goal is to teach how LLM-enabled applications fail when untrusted language is connected to privileged context, business data, tools, workflows, and downstream interpreters.

The module uses the OWASP Top 10 for LLM Applications as the main practitioner taxonomy and connects it back to the security engineering foundations from Modules 1–4.

## Core message

> LLM security is not solved by better prompts. Prompts are control hints, not hard security boundaries.

An LLM application is a software system. It has:

- users
- APIs
- identity
- permissions
- data stores
- prompts
- retrieved context
- tools
- logs
- output renderers
- downstream systems
- monitoring
- business workflows

The model is one component in that system. Security controls must be implemented around the model, not only inside the prompt.

## Learning objectives

By the end of this module, students should be able to:

1. Explain why LLM security is an application security problem.
2. Describe the major OWASP LLM/GenAI risk categories.
3. Distinguish direct prompt injection from indirect prompt injection.
4. Explain why insecure output handling can become XSS, SQL injection, SSRF, command injection, or workflow abuse.
5. Identify sensitive information disclosure paths in LLM applications.
6. Explain model denial of service as both availability and cost risk.
7. Identify excessive agency and overreliance risks.
8. Design basic security controls around LLM applications.
9. Map LLM findings to engineering fixes, not only prompt changes.
10. Produce a short LLM application security review.

## Topics

- LLM application architecture
- Prompt injection
- Indirect prompt injection
- System prompt leakage
- Insecure output handling
- Sensitive information disclosure
- Model denial of service
- Training data poisoning in the LLM context
- AI supply chain vulnerabilities
- Excessive agency
- Overreliance
- Model theft
- Secure LLM gateway patterns
- Input and output validation
- Context separation
- Retrieval and tool authorization
- Rate limits and budget controls
- Human approval gates
- Audit logging and monitoring

## Security engineering connection

| Classic security concept | LLM application equivalent |
|---|---|
| Injection | Prompt injection, output-to-code injection, output-to-query injection |
| Confused deputy | LLM acts using privileges granted to the app, not the attacker |
| Access control | Retrieved data and tools must be authorized outside the model |
| Least privilege | LLM tools and context should be scoped to the task |
| Complete mediation | Each tool call and data access must be checked independently |
| Input validation | Prompts, documents, retrieved content, tool arguments |
| Output encoding | LLM output rendered in HTML, Markdown, SQL, shell, code, JSON |
| Resource exhaustion | Long prompts, repeated tool calls, context-window abuse, expensive inference |
| Secure defaults | Safe mode, no destructive actions, approval required by default |
| Auditability | Record prompt, context sources, tool calls, decisions, and approvals |

## OWASP LLM risk framing

This module primarily maps to the OWASP Top 10 for LLM Applications. The 2025 OWASP LLM Top 10 uses the following numbering:

- LLM01: Prompt Injection
- LLM02: Sensitive Information Disclosure
- LLM03: Supply Chain
- LLM04: Data and Model Poisoning
- LLM05: Improper Output Handling
- LLM06: Excessive Agency
- LLM07: System Prompt Leakage
- LLM08: Vector and Embedding Weaknesses
- LLM09: Misinformation
- LLM10: Unbounded Consumption

The 2023/2024 OWASP LLM release used different numbering for several categories, including insecure output handling, sensitive information disclosure, excessive agency, and overreliance/model-theft-related themes. The engineering lesson should not depend on memorizing numbering. Students should learn the underlying failure modes and check the current OWASP GenAI project when producing reports.


## Reading-first deepening materials

Module 05 now includes additional reading-first material intended to make the topic understandable without relying only on labs:

- `deep-dive.md`  -  explains LLM application security as security engineering around a probabilistic component.
- `attack-anatomy.md`  -  breaks down prompt injection, indirect prompt injection, sensitive disclosure, improper output handling, excessive agency, system prompt leakage, and unbounded consumption.
- `controls-and-remediations.md`  -  maps weak mitigations to stronger implementable controls and validation tests.
- `common-mistakes.md`  -  captures common design and reporting mistakes teams make with LLM applications.
- `worked-example.md`  -  shows how to turn a vague “the model was jailbroken” observation into an engineering-grade finding.

Students should read these before or alongside the DVAIA lab. The lab reinforces the concepts; it does not replace the explanation.

## Lab

Recommended lab base:

- `labs/dvaia-guides/llm-application-security-lab.md`

The lab should be run in a local, intentionally vulnerable environment only.

The lab covers:

1. Direct prompt injection
2. System prompt leakage attempt
3. Insecure output handling review
4. Sensitive disclosure through context misuse
5. Model DoS risk analysis
6. Overreliance scenario
7. Mitigation design

## Deliverables

Students should produce:

- LLM application threat summary
- Vulnerability write-up
- Root cause explanation
- Mitigation plan
- Residual risk statement

## Recommended timing

| Section | Time |
|---|---:|
| LLM app architecture refresher | 15 min |
| OWASP LLM risk walkthrough | 35 min |
| Attack-to-root-cause discussion | 20 min |
| DVAIA-style lab | 60–90 min |
| Mitigation workshop | 30 min |
| Review and quiz | 15 min |

## Instructor emphasis

Keep returning to this question:

> Where should the security decision live?

Usually the answer is not: “inside the prompt.”

Security decisions should live in:

- authorization services
- policy engines
- tool gateways
- output validators
- workflow approval systems
- data access layers
- monitoring and detection pipelines
- deployment controls

The LLM can help reason, summarize, and assist. It should not be the sole enforcement point for critical security decisions.


## BrokenPilot observable Module 05 lab

Use `brokenpilot-direct-injection-output-lab.md` to observe two Module 05 failures in the local BrokenPilot prototype:

- direct prompt injection through the user message;
- insecure output handling when model-derived text reaches an HTML sink without encoding.

This lab is course-owned and deterministic. DVAIA remains useful as an optional external comparison, but this path keeps the core Module 05 hands-on work runnable without external dependencies.
