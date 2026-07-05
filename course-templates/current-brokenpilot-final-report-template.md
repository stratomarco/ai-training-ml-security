# BrokenPilot Final Report Template: Current Lab Path

## Executive summary

State the launch recommendation and the top two risks in plain language.

## Scope

List which BrokenPilot labs were tested. State that classical ML attacks are covered by the toy-classifier lab, not BrokenPilot.

## System context

Describe the trust boundaries: user input, retrieved content, model output, tools, memory, tenant metadata, and logs.

## Findings

For each finding, use this structure:

### Finding title

**Evidence:** What did you observe in the vulnerable and controlled states?

**Root cause:** Which trust boundary or enforcement decision failed?

**Impact:** What could happen if this existed in a real internal AI agent?

**Strong control:** What should the engineering team implement?

**Weak control to avoid:** What sounds plausible but does not enforce the boundary?

**Validation:** How would you prove the fix works?

**Residual risk:** What remains after the fix?

## Remediation backlog

Prioritize fixes by launch impact.

## Launch recommendation

Choose one:

- approve limited pilot;
- approve only read-only pilot;
- delay launch;
- reject until architecture change.

Explain the conditions for your decision.
