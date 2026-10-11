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

This module uses the [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) as its current practitioner map. The closest 2025 labels are shown so older reports and exercises remain readable; they are not claims that the two editions define every risk identically.

| 2026 ID | 2026 risk | Closest 2025 ID and label |
|---|---|---|
| LLM01:2026 | Prompt Injection | LLM01:2025 Prompt Injection |
| LLM02:2026 | Sensitive Information Disclosure | LLM02:2025 Sensitive Information Disclosure |
| LLM03:2026 | Excessive Agency | LLM06:2025 Excessive Agency |
| LLM04:2026 | Supply Chain | LLM03:2025 Supply Chain |
| LLM05:2026 | Data and Model Poisoning | LLM04:2025 Data and Model Poisoning |
| LLM06:2026 | Unbounded Consumption | LLM10:2025 Unbounded Consumption |
| LLM07:2026 | Misinformation | LLM09:2025 Misinformation |
| LLM08:2026 | Hidden Context Exposure | LLM07:2025 System Prompt Leakage; broader in 2026 |
| LLM09:2026 | Vector and Embedding Weaknesses | LLM08:2025 Vector and Embedding Weaknesses |
| LLM10:2026 | Improper Output Handling | LLM05:2025 Improper Output Handling |

The 2023/2024 editions also used different numbering. Cite the edition with the ID in a report. The engineering lesson does not depend on memorizing numbers: identify the failure, the enforcement point, and evidence that a control works. For agent actions and memory, pair this application list with the [OWASP Agentic Applications 2026 guide](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).

## Reading-first deepening materials

Module 05 now includes additional reading-first material intended to make the topic understandable without relying only on labs:

- `deep-dive.md`  -  explains LLM application security as security engineering around a probabilistic component.
- `attack-anatomy.md`  -  breaks down prompt injection, indirect prompt injection, sensitive disclosure, improper output handling, excessive agency, system prompt leakage, and unbounded consumption.
- `controls-and-remediations.md`  -  maps weak mitigations to stronger implementable controls and validation tests.
- `common-mistakes.md`  -  captures common design and reporting mistakes teams make with LLM applications.
- `worked-example.md`  -  shows how to turn a vague “the model was jailbroken” observation into an engineering-grade finding.

Students should read these before or alongside the BrokenPilot lab. The lab reinforces the concepts; it does not replace the explanation.

## Lab

Recommended lab base:

- [BrokenPilot standalone path](brokenpilot-standalone-lab.md)
- [Direct injection and output handling](brokenpilot-direct-injection-output-lab.md)

DVAIA is an optional external comparison, not required for the core lab.

The lab should be run in a local, intentionally vulnerable environment only.

The runnable BrokenPilot path covers direct prompt injection, indirect injection through retrieved content, output handling, cross-tenant disclosure, and the boundary between a proposed action and a ticket update. Use reading and discussion for unbounded consumption, misinformation, and model theft; the prototype does not reproduce those risks. End with a mitigation design and a validation method for the observed failure.

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
| BrokenPilot guided lab | 60–90 min |
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

<!-- lab-routing-content-pass:start -->

## Lab routing note

Module 05 uses BrokenPilot for direct prompt injection, indirect prompt injection, and insecure output handling. DVAIA remains an optional external comparison lab, not a survival dependency.

Suggested practice deliverable: A Module 05 control note that identifies the trust boundary, shows the vulnerable and controlled behavior, recommends an architectural control, and states residual risk.

See `lab-path.md` in this module and `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md` for the full lab modality map.

<!-- lab-routing-content-pass:end -->

<!-- student-reading-guide-link -->

## Student reading guide

Before starting the lab or exercise, read [student-reading-guide.md](student-reading-guide.md). It explains the module's core security decision, lab path, common mistakes, and exit ticket.

<!-- cohesion-note-link -->

## Course cohesion note

For instructor handoff language and the module's place in the full course story, see [cohesion-note.md](cohesion-note.md).

## Round 3 Module 05 output-handling confirmation

Module 05 includes two BrokenPilot paths: direct prompt injection and insecure output handling. The output-handling path uses `POST /render` and the `ENABLE_OUTPUT_ENCODING` control so students can observe raw versus encoded output in a deterministic HTML sink.
