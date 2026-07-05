# Standalone Hands-On Path Rubric

This rubric is used when BrokenPilot is the primary hands-on target.

## Scoring

| Area | Excellent | Adequate | Weak |
|---|---|---|---|
| Evidence | Includes request, control state, response, and before/after behavior | Shows vulnerable behavior but incomplete control evidence | Describes behavior without reproducible evidence |
| Root cause | Names the failed boundary or missing server-side control | Names a general issue but not the boundary | Blames the model or prompt only |
| Control | Recommends implementable architecture or policy control | Recommends a partial control | Says only "better guardrails" |
| Validation | Explains how to retest the fix | Mentions retesting but lacks detail | No validation method |
| Residual risk | States what remains after control | Vague residual risk | Claims risk is eliminated |
| Leadership clarity | Explains business impact and decision | Mostly technical | No risk decision |

## Minimum passing evidence

A team must submit evidence for at least three of these four runnable behaviors:

- prompt injection through retrieved context;
- cross-tenant retrieval;
- cross-tenant ticket update;
- memory poisoning or defense in depth.

## Capstone alignment

A final report can include tabletop discussion of supply chain, privacy, and adversarial ML. However, those topics should not be graded as runnable findings unless the student used a separate target that demonstrates them.
