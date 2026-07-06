# BrokenPilot v2 Lab Quality Bar

A v2 lab must meet the quality bar already established by v1.1.0.

## Required properties

Each lab must have:

- a clear security decision
- a runnable or evidence-backed target
- an unsafe baseline
- a visible fix or control
- a naive-fix failure mode
- a defense-in-depth moment
- a graded deliverable
- a deterministic reset path
- a test, validation artifact, or review checklist
- an instructor debrief path

## Lab types allowed

### Runnable lab

Students trigger a failure and then enable or implement a control. The expected result is visible through API responses, UI output, logs, tests, or audit evidence.

### Evidence-pack lab

Students review realistic artifacts and produce a decision-grade finding. The expected result is visible through a graded evidence map, model answer, and rubric.

### Build-and-prove lab

Students implement a control and prove it holds with tests or validation artifacts.

## Lab types not allowed for v2 release

A v2 release should not ship a module whose lab is only:

- descriptive reading
- discussion without evidence
- a screenshot-only walkthrough
- a tool demo with no security decision
- a prompt trick with no architectural lesson

## Student deliverable standard

Every v2 lab should produce at least one of:

- threat model update
- exploit evidence log
- control design
- test or validation evidence
- secure architecture change
- residual-risk statement
- executive finding rewrite

## Instructor standard

Every v2 lab should have:

- setup instructions
- expected observations
- common student mistakes
- debrief prompts
- grading anchors
- reset guidance
