# Module 5 Slides — LLM Application Security

## Slide 1 — Title

# LLM Application Security

Security engineering for applications that contain large language models.

---

## Slide 2 — Why this module exists

LLM applications are becoming production software.

They are connected to:

- internal documents
- customer data
- tickets
- email
- code repositories
- cloud APIs
- business workflows
- tools and plugins

That means LLM security is no longer only about model behavior.

It is about application architecture.

---

## Slide 3 — Core message

> LLM security is not solved by better prompts.

Prompts are useful.

Prompts are not hard security boundaries.

Security controls must exist around the model.

---

## Slide 4 — The LLM as a component

An LLM application usually includes:

```text
User
  -> Application UI/API
  -> Prompt builder
  -> LLM gateway
  -> Model provider or local model
  -> Retrieval system
  -> Tools/functions/plugins
  -> Databases
  -> Logs/monitoring
  -> Output renderer
```

Each component has a security role.

Each component can fail.

---

## Slide 5 — Classic AppSec still applies

LLM applications still have:

- authentication bugs
- authorization bugs
- insecure APIs
- exposed secrets
- injection flaws
- SSRF
- XSS
- supply chain issues
- logging problems
- weak monitoring
- bad defaults

The model does not remove normal AppSec.

It adds new ways to trigger old failures.

---

## Slide 6 — What is different?

LLM systems blend:

- instructions
- user input
- retrieved data
- memory
- tool results
- policies
- examples
- generated output

The model receives all of this as language-like context.

This creates ambiguity between **data** and **instructions**.

---

## Slide 7 — OWASP LLM framing

OWASP LLM risks provide a useful practitioner map:

- Prompt injection
- Insecure output handling
- Training data poisoning
- Model denial of service
- Supply chain vulnerabilities
- Sensitive information disclosure
- Tool/plugin design issues
- Excessive agency
- Overreliance
- Model theft

Do not memorize numbers.

Understand failure modes.

---

## Slide 8 — Prompt injection

Prompt injection happens when untrusted input causes the model to follow attacker-controlled instructions instead of the intended task.

Examples:

- user directly asks the model to ignore prior instructions
- malicious text in a document changes model behavior
- tool output contains instructions that hijack the workflow

Security lesson:

> The model cannot be treated as a reliable instruction firewall.

---

## Slide 9 — Direct vs indirect prompt injection

Direct prompt injection:

```text
The attacker sends the malicious instruction directly to the assistant.
```

Indirect prompt injection:

```text
The attacker hides the malicious instruction in content the assistant later reads.
```

Indirect injection is often more dangerous because the user may never see the malicious instruction.

---

## Slide 10 — Prompt injection is not just jailbreaks

Prompt injection can cause:

- wrong decisions
- data exposure
- tool misuse
- policy bypass
- workflow manipulation
- reputation damage
- unsafe automation
- cost increase

The impact depends on what the application can access and do.

---

## Slide 11 — Root cause of prompt injection

Root causes often include:

- mixing instructions and untrusted data
- granting the model too much authority
- using prompts as policy enforcement
- weak authorization around retrieved data
- unsafe tool design
- no approval gates
- no output verification
- no monitoring of tool calls

The prompt is only one layer.

---

## Slide 12 — Insecure output handling

LLM output is untrusted.

If the application passes LLM output into another interpreter, the result can become a classic vulnerability.

Examples:

- HTML renderer -> XSS
- SQL builder -> SQL injection
- shell command -> command injection
- browser fetcher -> SSRF
- YAML/JSON parser -> unsafe behavior
- code executor -> RCE

---

## Slide 13 — Treat model output like user input

Model output should be:

- validated
- encoded
- constrained
- schema-checked
- safely rendered
- reviewed before dangerous use

The model can produce text that looks trusted.

That does not make it trusted.

---

## Slide 14 — Sensitive information disclosure

LLM applications may disclose sensitive data through:

- retrieved context
- logs
- prompts
- chat history
- memory
- embeddings
- tool results
- system messages
- model responses

The question is not only:

> Can the model memorize secrets?

The bigger question is:

> Did the application give the model access to secrets it should not expose?

---

## Slide 15 — Authorization must happen before context injection

Bad pattern:

```text
Retrieve broadly -> put everything in prompt -> ask model not to reveal unauthorized data
```

Better pattern:

```text
Authorize user -> retrieve only allowed data -> label sources -> constrain answer -> audit output
```

The model should not be responsible for deciding which documents the user may access.

---

## Slide 16 — Model denial of service

LLM DoS can target:

- availability
- latency
- cost
- token budget
- context window
- tool-call budget
- queue capacity
- human review capacity

A working attack may simply make the system too expensive or too slow to use.

---

## Slide 17 — LLM supply chain risk

LLM applications depend on:

- model providers
- local models
- model weights
- adapters
- datasets
- prompts
- plugins
- tools
- frameworks
- vector databases
- evaluation datasets
- guardrail libraries

Each dependency can be compromised or misconfigured.

---

## Slide 18 — Excessive agency

An LLM has excessive agency when it can do too much with too little control.

Examples:

- create or delete records
- change tickets
- send emails
- run code
- approve access
- trigger deployments
- call external APIs

If the model can act, LLM security becomes workflow security.

---

## Slide 19 — Overreliance

Overreliance happens when humans or systems trust LLM output beyond its reliability.

Examples:

- accepting security advice without review
- relying on generated code without testing
- using summaries as evidence
- allowing the model to make operational decisions
- treating confident text as verified truth

Security lesson:

> Fluency is not evidence.

---

## Slide 20 — Model theft

Model theft can mean:

- stealing weights
- extracting model behavior through queries
- copying a proprietary fine-tuned model
- stealing prompts or system instructions
- abusing APIs to build a competing model

Controls include:

- access control
- rate limits
- abuse detection
- watermarking where appropriate
- monitoring unusual query patterns
- protecting model artifacts

---

## Slide 21 — Secure LLM application pattern

A safer pattern:

```text
User
  -> AuthN/AuthZ
  -> Input validation
  -> Prompt/context builder
  -> Policy-controlled retrieval
  -> LLM gateway
  -> Tool gateway with per-action authorization
  -> Output validation/encoding
  -> Human approval for high-risk actions
  -> Audit logging and monitoring
```

Security decisions are outside the model.

---

## Slide 22 — Control: context separation

Separate:

- system instructions
- developer instructions
- user input
- retrieved data
- tool output
- policy decisions
- citations/sources

Label sources clearly.

Do not rely on labels alone as enforcement.

Use external controls.

---

## Slide 23 — Control: tool gateway

Every tool call should have:

- explicit schema
- argument validation
- user authorization
- task authorization
- rate limits
- audit logging
- safe defaults
- dry-run mode where possible
- approval for sensitive actions

The model proposes.

The system enforces.

---

## Slide 24 — Control: output handling

Before using LLM output:

- validate structure
- reject unexpected fields
- encode before rendering
- avoid direct execution
- avoid direct SQL/shell construction
- enforce content type
- sanitize Markdown/HTML
- log unsafe output events

Treat output as untrusted.

---

## Slide 25 — Control: sensitive data protection

Protect sensitive data by:

- minimizing context
- authorizing retrieval
- redacting secrets
- avoiding secrets in prompts
- limiting retention
- securing logs
- isolating tenants
- using scoped credentials
- reviewing memory writes

Do not solve data access with prompt instructions.

---

## Slide 26 — Control: cost and availability

Defend against LLM DoS with:

- input size limits
- token budgets
- rate limits
- queue limits
- timeout limits
- tool-call limits
- recursion limits
- per-user budgets
- anomaly detection
- graceful degradation

Availability includes cost control.

---

## Slide 27 — Lab framing

In the lab, students should identify:

1. What the attacker controls
2. What the model can see
3. What the model can do
4. What downstream systems trust
5. Which security decision is misplaced
6. What control belongs outside the model

The objective is not only exploit execution.

The objective is engineering judgment.

---

## Slide 28 — Common bad mitigation

Bad mitigation:

```text
Add a stronger system prompt.
```

Better mitigation:

```text
Add external authorization, scoped tools, output validation, retrieval filtering, monitoring, and approval gates.
```

Prompts are useful defense-in-depth.

They are not enough.

---

## Slide 29 — Discussion scenario

An internal assistant can:

- read incident tickets
- search engineering docs
- summarize outages
- create follow-up tickets
- update ticket priority

Question:

> Which actions can the model perform autonomously, and which require approval?

---

## Slide 30 — Final takeaway

LLM application security is about controlling the full system:

- data
- prompts
- retrieval
- tools
- identity
- workflows
- outputs
- monitoring
- human decisions

The model can assist.

The system must enforce.
