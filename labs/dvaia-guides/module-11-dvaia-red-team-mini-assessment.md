> **Round 3 consolidation note:** This legacy paper lab is no longer the primary 40-hour course path. Use the BrokenPilot runnable lab for observable failure/fix behavior. Keep this file only as optional background or a discussion prompt.

# Module 11 Mini-Assessment  -  DVAIA AI Red Team Workflow

## Status

Status: **Validated external lab target available**  
External target: **DVAIA**  
Validation baseline: DVAIA commit `23c115252554caa445c0e6ba28641c1110c118e1`, local mode, Ollama backend, `http://127.0.0.1:5000`

This mini-assessment turns the DVAIA-backed labs into a structured AI red team exercise. It is designed for Module 11 and can be run after Modules 05, 06, and 07.

## Goal

Students must perform a small, controlled AI red team assessment against the local DVAIA environment and produce a concise report with evidence, impact, root cause, mitigation, and residual risk.

## Scope

In scope:

- Local DVAIA instance only.
- Prompt injection behavior.
- Indirect prompt injection or RAG behavior where available.
- Agent/tool behavior where available.
- Output handling and sensitive-disclosure behavior where available.
- Evidence capture and report writing.

Out of scope:

- Attacking real systems.
- Internet-exposed targets.
- Cloud provider abuse.
- Credential theft.
- Destructive local system actions.
- Denial-of-service stress testing beyond small local validation.

## Rules of engagement

1. Only test your local DVAIA instance.
2. Do not connect real data or real credentials.
3. Do not attempt host escape or Docker escape.
4. Do not scan unrelated networks.
5. Do not attempt to attack the upstream DVAIA project maintainers or infrastructure.
6. Keep evidence concise and reproducible.
7. Prefer benign validation markers over harmful actions.

## Assessment tasks

### Task 1  -  Scope and setup

Document:

- DVAIA commit.
- Docker version.
- Docker Compose version.
- Run mode.
- LLM backend.
- Target URL.
- Panels/features tested.

### Task 2  -  Finding 1: direct prompt injection

Reproduce a direct prompt-injection behavior or document why the attempted behavior was blocked.

Required output:

- Prompt used.
- Response summary.
- Security property violated or protected.
- Root cause.
- Mitigation.

### Task 3  -  Finding 2: indirect/RAG-style injection

Reproduce or simulate indirect prompt injection through retrieved or external content.

Required output:

- Malicious content/sample.
- Benign user prompt.
- Response summary.
- Trust-boundary failure.
- Mitigation.

### Task 4  -  Finding 3: agent/tool behavior or control-design gap

If DVAIA exposes agent/tool behavior, test it directly.

If not, perform a control-design assessment using a fictional tool list and DVAIA model behavior as the model-risk component.

Required output:

- Available/simulated tools.
- Sensitive action tested.
- Expected secure behavior.
- Observed or hypothesized failure.
- Concrete permission/approval control.

### Task 5  -  Executive readout

Write a short executive summary using this format:

```text
We tested the local DVAIA AI security lab environment to validate course exercises for LLM, RAG, and agent security. The main lesson is that model behavior cannot be treated as an enforcement boundary. The most important controls are external authorization, retrieval-time access control, tool permission scoping, approval gates, output validation, logging, and regression testing.
```

Students should adapt this to their actual findings.

## Deliverables

Students must submit:

1. Scope statement.
2. Evidence log.
3. Three findings or test results.
4. One tool permission matrix or approval policy.
5. One executive summary.
6. Residual risk statement.

## Grading rubric

| Area | Strong submission | Weak submission |
|---|---|---|
| Scope | Clear, bounded, reproducible | Vague or unsafe |
| Evidence | Includes prompts, response summaries, environment details | Screenshots only, no context |
| Root cause | Explains trust boundary and control failure | Says only "the model was jailbroken" |
| Mitigation | Specific implementable controls | Generic "improve prompt" advice |
| Executive communication | Connects technical issue to business risk | Overhyped or too technical |
| Residual risk | Explains what remains uncertain | Claims problem is fully solved |

## Instructor notes

This mini-assessment is the bridge between isolated labs and the BrokenPilot capstone. It should teach students to report like security engineers, not merely collect jailbreak examples.
