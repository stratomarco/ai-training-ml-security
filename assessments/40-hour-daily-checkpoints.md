# 40-hour daily checkpoints

These checkpoints make the one-week course easier to run and easier to grade. They are short, evidence-based, and tied to the labs students already perform.

## Grading posture

Daily checkpoints are lightweight. They are used to catch misunderstandings early. The final capstone remains the main graded artifact.

Use this weighting for a 40-hour professional course:

| Component | Weight |
|---|---:|
| Daily checkpoints | 20 percent |
| Lab journal quality | 20 percent |
| BrokenPilot or toy-classifier evidence | 20 percent |
| Capstone report | 30 percent |
| Final presentation or readout | 10 percent |

## Day 1 checkpoint: system and security boundaries

### Student submits

- one system context diagram or text equivalent
- one trust-boundary list
- two abuse cases
- one early risk statement

### Instructor checks

- The student distinguishes model behavior from system security behavior.
- Trust boundaries are explicit.
- At least one abuse case describes misuse by an authorized user.

### Common weak answer

The student says the solution is to make the prompt stronger, without identifying an enforcement point.

## Day 2 checkpoint: LLM, RAG, and output handling

### Student submits

- one direct or indirect prompt-injection observation
- one retrieval or tenant-isolation observation
- one output-handling observation or explanation
- one proposed control and validation step

### Instructor checks

- The student explains untrusted text treated as authority.
- The student can name the trust boundary for user input and retrieved content.
- The student understands that output must be encoded or validated for the downstream context.

## Day 3 checkpoint: agents and supply chain

### Student submits

- one tool authorization finding or permission matrix
- one evidence-pack supply-chain finding
- one approval or promotion-gate recommendation

### Instructor checks

- The student separates model intent from tool execution.
- The student can identify provenance and artifact-integrity gaps.
- The recommendation is implementable by an engineering team.

## Day 4 checkpoint: privacy, adversarial ML, and red-team reporting

### Student submits

- one privacy leakage finding or privacy tabletop review
- one toy-classifier observation or adversarial ML risk argument
- one rewritten finding using the course finding format

### Instructor checks

- The student avoids overclaiming from toy data.
- The student frames model robustness around engineering decisions and fallbacks.
- The finding includes root cause, control, validation, and residual risk.

## Day 5 checkpoint: capstone readiness

### Student submits

- final finding list
- remediation backlog
- residual-risk section
- leadership recommendation

### Instructor checks

- The report does not grade the model alone.
- Evidence is local and reproducible.
- Findings map to concrete controls and validation steps.
- The recommendation is clear: launch, limited pilot, delay, or stop.
