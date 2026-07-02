# Module 11 Instructor Notes — AI Red Team Methodology

## Teaching goal

Students should leave this module understanding that AI red teaming is not merely adversarial prompting. It is a structured security assessment method for AI-enabled systems.

The module should push students toward disciplined thinking:

- define scope;
- understand the system;
- threat model before testing;
- plan attack paths;
- test safely;
- capture evidence;
- explain root cause;
- recommend architecture-level fixes;
- communicate residual risk.

## Tone to set

Use a professional security-engineering tone.

Avoid turning the class into a competition for clever jailbreaks. Encourage curiosity, but keep students grounded in impact and control design.

A useful phrase:

> The prompt is the trigger. The vulnerability is usually in the surrounding system.

## Suggested timing

For a 90-minute session:

| Time | Activity |
|---|---|
| 0–10 min | Introduce AI red teaming and why screenshots are not enough. |
| 10–25 min | Scope, rules of engagement, safety boundaries. |
| 25–40 min | System understanding, threat modeling, and attack-path planning. |
| 40–55 min | Testing categories: LLM, RAG, agent, privacy, MLOps, robustness, infrastructure. |
| 55–70 min | Evidence, severity, reporting, remediation. |
| 70–85 min | BrokenPilot tabletop exercise. |
| 85–90 min | Discussion and wrap-up. |

For a 3-hour workshop, expand the BrokenPilot attack-chain lab and require teams to present one finding.

## Key concepts to emphasize

### 1. The system is the target

AI security failures usually emerge from system composition:

- model output is trusted too much;
- retrieved context is overbroad;
- tools run with broad permissions;
- policy is implemented only in prompts;
- logs are insufficient;
- humans over-trust fluent output;
- feedback loops are unguarded.

### 2. Red team scope must include model-adjacent components

Do not let students scope only “the model.”

They should ask:

- What does the model read?
- What does it write?
- What tools can it call?
- What identities does it use?
- What documents can influence it?
- What memory persists?
- What logs exist?
- Who reviews actions?

### 3. Findings must be actionable

A weak finding says:

> Prompt injection works.

A strong finding says:

> A user-controlled document can inject instructions into the RAG context, causing the assistant to call a ticket-update tool against restricted incidents because the application does not enforce per-action authorization outside the model.

### 4. Severity is about impact, not trickiness

A simple prompt that causes data leakage may be critical.

A clever jailbreak that only changes harmless text may be low severity.

### 5. Controls must live outside the model where possible

Prompts can help with intent and behavior shaping, but they are not strong security boundaries.

Students should recommend:

- policy checks outside the model;
- retrieval authorization before context construction;
- least-privilege tool tokens;
- approval gates;
- output validation;
- sandboxing;
- monitoring;
- audit trails;
- safe fallback behavior.

## Facilitating the lab

Use the BrokenPilot capstone files as the realistic system under test.

Recommended flow:

1. Assign each group a role: attacker, AppSec reviewer, platform engineer, product owner.
2. Give them the BrokenPilot architecture and role model.
3. Ask them to choose one attack path.
4. Require them to write the finding in report form.
5. Ask them to propose one quick fix and one architectural fix.
6. Ask them to explain residual risk.

## Common student mistakes

| Mistake | Coaching response |
|---|---|
| They focus only on prompts. | Ask what the model can access or do. |
| They ignore authorization. | Ask whether the user or the model identity is being checked. |
| They treat retrieved content as trusted. | Ask who can write documents and how source trust is represented. |
| They overstate certainty. | Ask what was tested, what was not tested, and what evidence supports the claim. |
| They recommend “better prompts” only. | Ask what control would still work if the model output was malicious. |
| They do not mention logs. | Ask how defenders would detect or investigate this issue. |

## Discussion prompts

- When is an LLM red team finding a model issue, and when is it an application issue?
- What should be forbidden during an AI red team test?
- How do you test an agent without allowing unsafe real-world actions?
- What evidence is necessary for a prompt injection finding?
- What makes a red team report useful to developers?
- How should AI red team results feed into governance and release gates?

## Assessment guidance

Reward students for:

- clear scope;
- realistic attacker goals;
- system-level reasoning;
- safe testing;
- evidence quality;
- root-cause analysis;
- practical mitigations;
- trade-off awareness;
- residual-risk communication.

Do not reward unsafe behavior, attacks outside scope, or vague “jailbreak” claims without impact.

## Finding rewrite practice

This module includes [`exercise-finding-rewrite.md`](exercise-finding-rewrite.md), a short exercise where students rewrite a weak AI security finding into a decision-grade finding with evidence, root cause, implementable control, validation, and residual risk. Use it before the BrokenPilot capstone to improve report quality.
