# 40-Hour Module Delivery Profiles

This guide turns the course into a realistic one-week professional training plan. It answers a practical instructor question: what should be taught live, what should be compressed, what should become lab work, and what should move to self-study?

The course has enough material for deeper study, but the live 40-hour version must be selective. The instructor should protect the concepts, labs, and reporting work that make the course credible with a real security engineering audience.

## Delivery rule

Do not try to teach every page live.

Use the live sessions for:

- core concepts and mental models,
- attack anatomy,
- security property mapping,
- lab validation,
- concrete controls,
- report quality,
- leadership communication.

Use self-study for:

- extended references,
- optional quizzes,
- extra framework mapping,
- detailed standards reading,
- implementation notes,
- optional labs that are not needed for the final capstone.

## Module treatment table

| Module | Title | Course day | Treatment | Suggested time |
|---|---|---|---|---|
| 01 | Security Engineering for AI | Day 1 | Foundation | 75 min live plus 30 min discussion |
| 02 | ML System Architecture | Day 1 | Foundation | 75 min live plus 60 min diagram exercise |
| 03 | OWASP ML Security Top 10 | Day 1 | Survey | 45 to 60 min survey |
| 04 | BIML Architectural Risk Analysis | Day 1 | Architecture review | 60 to 75 min live plus group review |
| 05 | LLM Application Security | Day 2 | Deep coverage | 90 min live plus 60 min lab |
| 06 | RAG Security and Indirect Prompt Injection | Day 2 | Deep coverage | 90 min live plus 75 min lab |
| 07 | Agent and Tool Security | Day 3 | Deep coverage | 120 min live plus 120 min BrokenPilot validation |
| 08 | Secure MLOps and AI Supply Chain | Day 3 | Deep coverage | 75 min live plus 60 min memo exercise |
| 09 | Privacy Attacks and Data Protection | Day 4 | Focused coverage | 60 min focused coverage plus 45 min tabletop |
| 10 | Adversarial ML and Robustness | Day 4 | Focused coverage | 75 min focused coverage plus 45 min worked example |
| 11 | AI Red Team Methodology | Day 4 | Deep coverage | 90 min live plus 60 min finding rewrite |
| 12 | BrokenPilot Capstone | Day 5 | Capstone | Full day capstone |

## Non-negotiable live outcomes

By the end of the week, every student should be able to:

1. explain why the model is not the security boundary,
2. draw a basic ML or AI system trust model,
3. reproduce at least one LLM or RAG failure in a controlled lab,
4. reproduce the BrokenPilot tool authorization failure and controlled behavior,
5. explain the Module 07 defense-in-depth lesson: poisoned intent can still be blocked by independent tool authorization,
6. write at least one finding with evidence, root cause, control, validation, and residual risk,
7. produce a final BrokenPilot report that supports a leadership decision.

## What to protect when time slips

Protect these parts first:

- Module 01 boundary framing,
- Module 05 prompt injection as a control-boundary failure,
- Module 06 retrieved content as untrusted input,
- Module 07 tool authorization and memory poisoning,
- Module 08 executive risk memo,
- Module 11 finding rewrite,
- Module 12 final report.

Cut these first:

- long reference reviews,
- optional quizzes,
- broad standards comparison,
- advanced adversarial ML math,
- extra lab variants,
- implementation details that do not affect a control decision.

## Daily delivery shape

A healthy day has five parts:

1. short recap from the previous day,
2. focused concept explanation,
3. attack or failure anatomy,
4. lab or artifact-producing exercise,
5. debrief tied to controls and reporting.

Avoid full-day lecture. Avoid full-day hacking without explanation. The course should feel like security engineering practice.

## Module profile index

- [Module 01 Delivery Profile](../modules/01-security-engineering-for-ai/delivery-profile.md)
- [Module 02 Delivery Profile](../modules/02-ml-system-architecture/delivery-profile.md)
- [Module 03 Delivery Profile](../modules/03-owasp-ml-top-10/delivery-profile.md)
- [Module 04 Delivery Profile](../modules/04-biml-architectural-risk-analysis/delivery-profile.md)
- [Module 05 Delivery Profile](../modules/05-llm-application-security/delivery-profile.md)
- [Module 06 Delivery Profile](../modules/06-rag-security/delivery-profile.md)
- [Module 07 Delivery Profile](../modules/07-agent-tool-security/delivery-profile.md)
- [Module 08 Delivery Profile](../modules/08-secure-mlops-supply-chain/delivery-profile.md)
- [Module 09 Delivery Profile](../modules/09-privacy-attacks/delivery-profile.md)
- [Module 10 Delivery Profile](../modules/10-adversarial-ml-robustness/delivery-profile.md)
- [Module 11 Delivery Profile](../modules/11-ai-red-team-methodology/delivery-profile.md)
- [Module 12 Delivery Profile](../modules/12-capstone-brokenpilot/delivery-profile.md)
