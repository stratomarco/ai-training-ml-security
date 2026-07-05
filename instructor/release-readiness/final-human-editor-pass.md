
# Final Voice and Content Polish Pass

This pass is for the final human edit before release. Do not treat it as a rewrite of the course. The goal is to make the material feel authored, coherent, and practical without weakening the technical content.

## Editing principles

1. Preserve the security argument.
   - Do not remove evidence, root cause, control, validation, or residual-risk language.
   - Do not simplify a finding into vague advice.

2. Prefer concrete engineering language.
   - Say what the engineer should inspect, enforce, test, or document.
   - Avoid generic lines that could fit any security course.

3. Reduce repeated generated-looking patterns.
   - Avoid starting many adjacent sections with the same phrase.
   - Replace repeated boilerplate with context-specific transitions.
   - Keep repeated structure where it helps grading, but vary explanatory prose.

4. Keep the course voice.
   - Direct, practical, security-engineering oriented.
   - Reading-first, lab-supported.
   - Honest about what is runnable, what is tabletop, and why.

5. Do not overclaim.
   - BrokenPilot demonstrates LLM/RAG/agent/privacy/red-team application risk.
   - The toy classifier demonstrates classical ML attack concepts.
   - The MLOps evidence pack demonstrates review of supply-chain evidence.
   - Tabletops are reasoning labs, not failed runnable labs.

## High-value files to review manually

Review these first because they shape the student experience:

- `README.md`
- `syllabus.md`
- `PUBLISHED_COURSE_VIEW.md`
- `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md`
- `labs/LAB_QUALITY_STANDARD.md`
- `modules/*/README.md`
- `modules/*/student-reading-guide.md`
- `labs/brokenpilot/worked-examples/current-complete-final-report.md`
- `labs/mlops-supply-chain-labs/worked-examples/complete-mlops-evidence-pack-model-answer.md`
- `labs/toy-ml-attacks/toy-classifier-app/README.md`

## Phrases to treat as review prompts, not automatic errors

The style reporter flags phrases such as:

- "This package"
- "checked twice"
- "apply script"
- "the apply script creates"
- "generated"
- "placeholder"
- "TODO"
- "student should"
- repeated openings such as "This module" or "This lab"

These are not always wrong. They are prompts for a human editor to inspect context.

## What good final prose looks like

Good final prose answers:

- What decision is the student learning to make?
- What evidence would change that decision?
- What control would actually enforce the boundary?
- How would the student validate the control?
- What residual risk remains?

## What to avoid

Avoid prose that only says:

- "Add guardrails."
- "Use monitoring."
- "Improve security."
- "The model can be tricked."
- "Follow best practices."

Those phrases are acceptable only when followed by concrete control placement, validation, and residual risk.
