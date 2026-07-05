# BrokenPilot Capstone Assessment Scope

BrokenPilot is the course capstone, but the runnable prototype does not implement every risk covered by the full curriculum.

This page defines what the runnable target can exhibit directly and what should be assessed through tabletop analysis, written deliverables, or discussion.

## Directly demonstrable in the runnable prototype

| Course area | Demonstrated by BrokenPilot MVP | Assessment mode |
|---|---|---|
| Module 05: LLM application security | Mock LLM follows untrusted retrieved instruction content | Hands-on evidence |
| Module 06: RAG security | Retrieval authorization failure, poisoned document behavior, metadata and tenant-boundary discussion | Hands-on evidence plus control design |
| Module 07: Agent and tool security | Tool confused-deputy update, cross-tenant ticket update, memory poisoning, approval and authorization toggles | Hands-on evidence plus fix validation |
| Module 11: AI red-team methodology | Evidence capture, finding quality, remediation validation, executive readout | Report and presentation |
| Module 12: Capstone | Integrated system review using the runnable target | Final report and presentation |

## Assessed through tabletop or deliverables

| Course area | Why it is not fully runnable yet | Assessment mode |
|---|---|---|
| Module 08: Secure MLOps and AI supply chain | The MVP does not implement a real training pipeline, model registry, artifact signing, or CI/CD promotion flow | Architecture review, risk memo, control design |
| Module 09: Privacy attacks | The MVP uses fake data and only demonstrates limited cross-tenant exposure patterns | Privacy risk assessment and logging/retention review |
| Module 10: Adversarial ML and robustness | The MVP uses a deterministic mock LLM and does not train or serve a real ML classifier | Worked examples, adversarial test plan, robustness monitoring design |

## Grading rule

Do not require students to demonstrate a finding in the runnable app unless the app actually implements that behavior.

Students may still discuss non-runnable risks if they clearly label them as:

- tabletop finding,
- design risk,
- future implementation risk,
- residual risk, or
- recommendation outside the current MVP.

## Instructor guidance

A strong capstone submission should separate:

1. **Observed evidence** from the runnable target.
2. **Design risks** inferred from the architecture.
3. **Controls validated** through toggles or tests.
4. **Controls proposed** but not implemented in the MVP.
5. **Residual risk** after the implemented controls.

This prevents students from being graded on vulnerabilities the target cannot exhibit while still preserving the full-course learning objectives.
