# Module 5 Instructor Notes — LLM Application Security

## Teaching goal

The goal of this module is to shift students away from a shallow “jailbreak mindset” and toward security engineering.

Students should leave understanding that prompt injection and LLM-specific failures are important, but the deeper question is:

> What did the application allow the model to see, decide, or do?

## Desired mental model

Use this framing repeatedly:

```text
LLM risk = untrusted language + privileged context + automated action + misplaced trust
```

A harmless chatbot has limited risk. A chatbot connected to tickets, documents, code, cloud APIs, email, and deployment workflows becomes a security-relevant system.

## Suggested flow

### 1. Start with a familiar AppSec analogy

Ask students:

> Why is SQL injection dangerous?

Expected answer:

- user-controlled input crosses into an interpreter
- the system mixes data and commands
- the database has privileges
- the application trusts the result

Then connect to LLMs:

- prompt injection mixes data and instructions
- the model is an interpreter of natural language instructions
- the application may give the model privileges or context
- downstream systems may trust the output

Make it clear that this is an analogy, not a perfect equivalence.

### 2. Distinguish symptoms from root causes

Prompt injection payloads are symptoms.

Root causes include:

- missing trust boundaries
- weak retrieval authorization
- unsafe tool design
- no output validation
- lack of approval gates
- broad credentials
- over-trusting model output
- weak logging and detection

Students should not write findings that say only “prompt injection exists.” They should explain why it matters.

### 3. Emphasize direct and indirect injection

Direct injection is easy to understand.

Indirect injection is where the architecture becomes important.

Use this example:

```text
A user asks an assistant to summarize a web page.
The web page contains hidden instructions telling the assistant to reveal private data.
The assistant follows the page instruction instead of the user task.
```

Ask:

- Who wrote the malicious instruction?
- Did the user intend to execute it?
- What should the assistant be allowed to access while summarizing?
- Should summarization and private-data access be in the same context?

### 4. Make insecure output handling concrete

Students often think LLM output is only text.

Show how text becomes dangerous when passed to:

- HTML renderer
- Markdown renderer
- SQL query builder
- shell command
- Python interpreter
- browser automation
- infrastructure-as-code tool
- ticketing workflow

The security rule:

> Treat LLM output as attacker-influenced unless proven otherwise.

### 5. Teach controls as architecture

When students propose “better system prompt,” accept it as defense-in-depth but ask:

- What happens when the prompt fails?
- What prevents unauthorized data access?
- What prevents dangerous tool calls?
- What prevents unsafe rendering?
- What records evidence for incident response?

Good answer patterns:

- scoped retrieval
- policy checks outside the model
- tool gateways
- schema validation
- output encoding
- human approvals
- rate limits
- audit logs
- evaluation suites

## Common misconceptions

### Misconception 1 — “We can solve this with a stronger prompt”

Correction:

A stronger prompt can reduce accidental failures and some low-effort attacks. It is not a reliable security boundary.

### Misconception 2 — “The model provider handles security”

Correction:

The provider may handle platform security and some safety controls. The application owner remains responsible for data access, tool permissions, workflow design, logging, and business risk.

### Misconception 3 — “Prompt injection is only about leaking the system prompt”

Correction:

System prompt leakage is usually lower impact than unauthorized data access, tool misuse, or workflow manipulation.

### Misconception 4 — “LLM output is safe because the model is trusted”

Correction:

The output is influenced by user input, retrieved content, and model behavior. It must be handled like untrusted data.

### Misconception 5 — “Overreliance is not a security issue”

Correction:

Overreliance can produce security impact when decisions affect access, incident response, production changes, code review, or compliance evidence.

## Discussion prompts

Use these during the lecture:

1. What is the asset in this LLM application?
2. What can the attacker control?
3. What can the model see?
4. What can the model do?
5. Which downstream systems trust the output?
6. Where is authorization enforced?
7. What happens if the prompt is ignored?
8. What is the safe failure mode?
9. What should be logged?
10. What requires human approval?

## Lab facilitation tips

During the DVAIA-style lab, keep students focused on three layers:

### Exploit layer

What happened?

### Root cause layer

Why was it possible?

### Design layer

Where should the control live?

Do not let the lab become only a prompt-writing competition.

## Expected student findings

Good findings should include:

- vulnerability category
- affected component
- attacker capability
- impact
- root cause
- evidence
- recommended control
- residual risk

Weak findings usually say only:

- “Prompt injection worked”
- “The model leaked information”
- “The model can be tricked”

Push students to complete the engineering reasoning.

## Suggested module timing

| Section | Suggested time |
|---|---:|
| Architecture refresher | 10–15 min |
| OWASP LLM risks | 30–40 min |
| Attack/root-cause mapping | 20 min |
| Lab | 60–90 min |
| Mitigation workshop | 25–30 min |
| Quiz and review | 10–15 min |

## Instructor close

End with this:

> The question is not whether the model can be tricked. The question is whether the system remains safe when the model is tricked.

## Teaching the reading-first materials

Use the new deepening files to avoid turning Module 05 into a payload-demo session. A good delivery pattern is:

1. Start with `deep-dive.md` and the claim that the model is not the security boundary.
2. Use `attack-anatomy.md` to show one complete attack path before showing any lab behavior.
3. Use `controls-and-remediations.md` to ask students where the control should live.
4. Use `common-mistakes.md` as a discussion exercise: ask students which mistakes they have seen in real AI prototypes.
5. Use `worked-example.md` to calibrate finding quality before students write their own report.

When students say “the model was jailbroken,” push them to restate the finding in engineering terms:

- What asset was affected?
- Which trust boundary failed?
- What authority did the model appear to have?
- Which deterministic control was missing?
- How would we validate the fix?
