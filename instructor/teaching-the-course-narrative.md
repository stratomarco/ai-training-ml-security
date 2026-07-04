# Teaching the course narrative

The instructor should repeat the same core story throughout the week: the model is one component in a larger security system. Students should leave with a way to reason about authority, data, artifacts, actions, outputs, validation, and residual risk.

## Daily narrative

### Day 1: Find the system

Students learn that AI security work starts by mapping the system, not by prompting the model. The expected artifacts are system context, trust boundaries, and initial abuse cases.

### Day 2: Watch text cross boundaries

Students observe direct injection, indirect injection, RAG leakage, and output handling. The key message is that untrusted text must not become authority.

### Day 3: Control actions and artifacts

Students move from model output to system action. They learn why tool authorization and model artifact promotion need independent controls.

### Day 4: Test reliability and privacy

Students study privacy leakage, adversarial robustness, and red team scoping. The key message is that test results must become evidence for a decision.

### Day 5: Integrate and recommend

Students write and present a capstone review. They are graded on evidence, root cause, controls, validation, residual risk, and leadership clarity.

## Instructor habits

- Ask where enforcement happens.
- Ask what evidence would change the decision.
- Ask what a naive fix would miss.
- Ask what remains risky after the control is applied.
- Avoid letting students stop at exploit demonstration.
