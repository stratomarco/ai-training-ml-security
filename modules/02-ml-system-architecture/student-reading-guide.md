# Student Reading Guide: Module 02: ML System Architecture

## What this module is really about

Most AI security failures are easier to understand when the system is drawn correctly. The module teaches students to see data sources, training paths, retrieval stores, tools, approval gates, identities, logs, and model outputs as one security-relevant system.

## Question to keep in mind

Where does untrusted data enter, where does authority get exercised, and where can a decision be reversed or audited?

## Decisions students must learn to make

- Identify the minimum diagram needed to reason about risk.
- Distinguish data flow from authority flow.
- Choose where to place enforcement so the model cannot bypass it.
- Decide what must be logged to reconstruct an AI-assisted action.

## Lab or exercise connection

Use the architecture exercise to produce a trust-boundary diagram and a short risk review. This is foundational for BrokenPilot and for the later supply-chain evidence review.

## What a strong submission looks like

A strong submission makes the risky path visible: untrusted input, model interpretation, downstream authority, and the control that prevents unsafe execution.

## Common misreadings to avoid

- Drawing only the model and ignoring retrieval, tools, identities, and deployment pipelines.
- Using a data-flow diagram as if it were an authorization design.
- Treating logs as evidence without asking whether the right fields are captured.

## Exit ticket

Point to one edge in your diagram where data crosses a trust boundary and one edge where authority is exercised.
