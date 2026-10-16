# 40-hour student workbook

This workbook gives students a single path through the one-week version of the course.

## How to use it

For each day, complete the required labs or reasoning exercises, fill the lab journal, and submit the checkpoint. Keep the same evidence and wording for the final capstone where possible.

Open each module overview below, then follow its student reading guide and lab path. Use the [lab journal](../labs/STUDENT_LAB_JOURNAL_GUIDE.md) to record the input, active controls, observation, root cause, validation, and residual risk. The [course map](40-hour-course-map.md) explains how the week fits together.

## Day 1

Focus: security foundations, system boundaries, and abuse cases.

Study [Module 01](../modules/01-security-engineering-for-ai/README.md), [Module 02](../modules/02-ml-system-architecture/README.md), [Module 03](../modules/03-owasp-ml-top-10/README.md), and [Module 04](../modules/04-biml-architectural-risk-analysis/README.md). Complete their reasoning exercises and run the [toy classifier](../labs/toy-ml-attacks/toy-classifier-app/README.md) for observable ML behavior.

Submit: system context, trust boundaries, two abuse cases, and one early risk statement.

## Day 2

Focus: LLM, RAG, direct and indirect injection, and output handling.

Study [Module 05](../modules/05-llm-application-security/README.md) and [Module 06](../modules/06-rag-security/README.md). Start the [BrokenPilot local lab](../labs/brokenpilot/prototype-app/README.md), follow the [ticket-to-agent investigation](../labs/brokenpilot/prototype-app/TICKET_TO_AGENT_LAB.md), and compare the vulnerable result with a controlled profile.

Submit: one vulnerable observation, one controlled observation, and one control validation.

## Day 3

Focus: agent/tool security and MLOps supply chain.

Study [Module 07](../modules/07-agent-tool-security/README.md) and [Module 08](../modules/08-secure-mlops-supply-chain/README.md). Use the [BrokenPilot tool lab](../labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md) for authorization and approval decisions. Review the [static MLOps evidence pack](../labs/mlops-supply-chain-labs/evidence-pack-review/README.md) as evidence; do not execute its notebook or load a pickle artifact.

Submit: one permission or approval decision, and one evidence-pack supply-chain finding.

## Day 4

Focus: privacy, adversarial ML, and red-team reporting quality.

Study [Module 09](../modules/09-privacy-attacks/README.md), [Module 10](../modules/10-adversarial-ml-robustness/README.md), and [Module 11](../modules/11-ai-red-team-methodology/README.md). Reuse BrokenPilot's cross-tenant retrieval evidence, the toy classifier observations, and the [finding rewrite](../modules/11-ai-red-team-methodology/exercise-finding-rewrite.md).

Submit: one privacy or adversarial finding and one rewritten strong finding.

## Day 5

Focus: BrokenPilot capstone report and readout.

Follow [Module 12](../modules/12-capstone-brokenpilot/README.md) and its [student handout](../modules/12-capstone-brokenpilot/student-handout.md). Use the [current final-report template](../course-templates/current-brokenpilot-final-report-template.md) and label paper-design risks separately from reproduced prototype behavior.

Submit: final report, remediation backlog, residual-risk statement, and leadership recommendation.
