# BrokenPilot Capstone Runbook

## Purpose

This runbook helps instructors deliver the BrokenPilot capstone as a classroom, workshop, or self-study exercise.

## Before the session

Instructor preparation:

- Review all files in `labs/brokenpilot/`.
- Decide whether the capstone is paper-only or hands-on.
- Select three to five vulnerability classes to emphasize.
- Decide whether students work individually or in teams.
- Prepare any fake documents, tickets, and incidents if running a live lab.
- Review grading rubric.

## Recommended team structure

For group work, assign roles:

- Security architect.
- Red teamer.
- ML/LLM engineer.
- Platform engineer.
- Product/security manager.

This helps students practice trade-off discussions rather than only exploitation.

## Delivery plan

### Phase 1 — Scenario briefing

Explain:

- Business context.
- What BrokenPilot does.
- What data it can access.
- What tools it can use.
- Why the company wants to ship it quickly.

Instructor focus:

- Emphasize usefulness and business value.
- Avoid framing the system as obviously bad.

### Phase 2 — Architecture review

Students read:

- `scenario.md`
- `architecture.md`
- `roles.md`
- `tools.md`
- `data-model.md`

Students produce:

- System context diagram.
- DFD.
- Initial trust-boundary list.

### Phase 3 — Threat model

Students identify:

- Assets.
- Attacker personas.
- Abuse cases.
- Assumptions.
- Control gaps.

Instructor should challenge vague findings:

- "Which asset is affected?"
- "Which boundary failed?"
- "What does the model see?"
- "What can the model do?"

### Phase 4 — Attack path analysis

Students use `attack-paths.md` as inspiration.

For each attack, they document:

- Goal.
- Steps.
- Expected result.
- Root cause.
- Impact.
- Mitigation.

### Phase 5 — Mitigation design

Students produce a practical plan.

Expected structure:

- Immediate fixes.
- Medium-term architecture changes.
- Longer-term governance and monitoring.
- Residual risk.

### Phase 6 — Presentation

Each team presents:

1. Executive summary.
2. Top three risks.
3. Most important architecture change.
4. One trade-off.
5. Residual risk.

## Debrief questions

- What is the difference between making the prompt better and making the system safer?
- Which controls are invisible to users?
- Which controls add friction?
- How would you keep developer velocity high?
- Which actions should never be available to the agent?
- What should be logged, and what should not be logged?
- How would you detect abuse after launch?

## Expected conclusion

BrokenPilot can be useful, but only if its architecture treats AI behavior as untrusted and model-mediated actions as security-sensitive workflow events.
