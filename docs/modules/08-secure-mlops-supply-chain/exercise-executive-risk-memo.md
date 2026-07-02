# Exercise — Executive Risk Memo for Secure MLOps and AI Supply Chain

## Purpose

This exercise gives students practice translating AI supply-chain risk into a leadership decision. It is deliberately placed in Module 08 because by this point students have already learned LLM, RAG, and agent risks, but they have not yet reached the formal red-team reporting module or BrokenPilot capstone.

The goal is not to write an executive summary after the work is done. The goal is to use executive communication as a security design tool: what decision are we asking leadership to make, what risk are we accepting, and what minimum controls are required before deployment?

## Scenario

Your organization is preparing to deploy an internal AI operations assistant. The assistant will summarize incidents, search internal documentation, read tickets, and recommend operational actions. The engineering team wants to fine-tune a small model using internal tickets and run the deployment through a fast MLOps pipeline.

The current proposal includes:

- Training data exported from historical incident tickets
- A shared notebook used by ML engineers
- A model artifact uploaded to an internal registry
- A containerized inference service
- A RAG index built from internal documentation
- A feedback loop where user corrections are stored for future improvement
- A planned pilot with engineering and operations users

During review, you find several concerns:

- The dataset contains sensitive customer and employee information.
- The model artifact is not signed.
- The training notebook contains a plaintext API key.
- The model registry permissions are broad.
- The feedback loop does not distinguish trusted corrections from untrusted user input.
- The team does not have a rollback plan if the model behaves unsafely.

The VP of Engineering asks whether the pilot can launch next week.

## Task

Write a one-page memo to the fictional CISO and VP of Engineering.

Your memo must answer:

1. What business goal does the AI assistant support?
2. What are the top three security or privacy risks?
3. Which risks are launch blockers and which can be managed during a pilot?
4. What minimum controls must be implemented before launch?
5. What residual risk remains after those controls?
6. What is your recommendation: launch, limited pilot, or delay?

## Constraints

- Keep the memo to one page.
- Use plain language.
- Do not write like a vulnerability scanner.
- Do not simply say “AI is risky.”
- Do not recommend blocking all AI usage unless you justify why.
- Do not rely on framework acronyms as the argument. Framework mappings can appear in an appendix.

## Expected recommendation

A strong answer will usually recommend a **limited pilot**, not an unrestricted launch and not a total block.

A reasonable recommendation could be:

> Proceed with a limited pilot only after removing secrets from notebooks, applying dataset redaction, restricting model-registry permissions, signing model artifacts, disabling automatic feedback-to-training, and defining rollback criteria.

Different recommendations are acceptable if the risk reasoning is sound.

## Minimum expected controls

Students should propose concrete controls such as:

| Risk | Minimum control |
|---|---|
| Sensitive data in training set | PII review, redaction, dataset approval gate, retention rules |
| Unsigned model artifact | Artifact signing, provenance record, registry access control |
| Plaintext API key in notebook | Secret rotation, secret scanning, managed secret store |
| Broad registry permissions | Least-privilege model registry roles |
| Untrusted feedback loop | Human review before feedback enters training data |
| Unsafe deployment | Rollback plan, monitoring, pilot scope, incident owner |

## Deliverable

Submit:

1. One-page executive memo.
2. Optional appendix mapping risks to controls.
3. One sentence stating what evidence you would collect during the pilot.

## Grading focus

The memo is graded on decision quality, not fear level.

A strong memo:

- Gives a clear recommendation.
- Connects technical findings to business impact.
- Separates launch blockers from manageable pilot risks.
- Defines concrete controls.
- Explains residual risk.
- Preserves developer velocity where possible.

A weak memo:

- Lists technical issues without a decision.
- Says “implement guardrails” without defining them.
- Uses acronyms instead of explaining impact.
- Treats all risks as equally severe.
- Ignores the business benefit of the AI assistant.

## Instructor notes

This exercise can be run in 20 to 40 minutes.

Suggested facilitation:

1. Give students 10 minutes to draft the memo outline.
2. Ask them to identify the one decision leadership must make.
3. Have them write the recommendation first, then supporting arguments.
4. Review one strong and one weak example.
5. Ask what would change if the system were customer-facing instead of internal.

The most important teaching point is that executive communication is not a watered-down vulnerability report. It is a decision support artifact.
