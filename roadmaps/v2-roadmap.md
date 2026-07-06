# ML Security Course v2 Roadmap

v1.1.0 is the stable teaching release: a coherent 40-hour foundational course grounded in security engineering, BIML, Ross Anderson, OWASP, NIST, MITRE ATLAS, and practical lab work. It teaches students to reason about systems that contain machine learning and to produce decision-grade security deliverables.

v2 should not mean "more modules." It should mean a deliberate move into the next risk surface while preserving the v1 security-engineering spine.

The working thesis for v2 is:

> v1 teaches foundations on single-agent and classical ML systems. v2 follows the field into multi-agent systems, MCP-mediated tool ecosystems, automated security evaluation, and build-and-prove controls.

This roadmap is intentionally kept separate from the v1.1.0 release path. v1.1.0 remains the stable teaching release until a future v2 release candidate exists.

## Why v2 exists

BrokenPilot v1 models a single AI agent with retrieval, tools, memory, control toggles, and auditability. That was the right foundation for v1.

The next frontier is not just a larger prompt-injection lab. The field is moving toward agentic systems made of orchestrators, sub-agents, tools, memory, registries, and protocol-mediated integrations. The new risk surface includes:

- agent goal hijack
- tool misuse across delegation chains
- agent identity and privilege abuse
- memory and context poisoning
- insecure inter-agent communication
- cascading agent failures
- human-agent trust exploitation
- rogue or spoofed agents
- MCP server and tool-descriptor trust failures
- agentic supply-chain compromise

v1 already covers the single-agent subset: tool misuse, memory poisoning, confused-deputy authorization, retrieval leakage, direct prompt injection, and unsafe output handling. v2 should cover the risks that only appear when multiple agents, tool brokers, registries, and protocol boundaries are involved.

## v2.0 core: multi-agent and MCP security

### What it adds

Extend BrokenPilot from one agent into a small multi-agent environment:

- an orchestrator agent
- a triage or planning agent
- a retrieval/documentation agent
- a ticket/action agent
- a shared tool broker
- an MCP-like server boundary
- explicit agent identity and descriptors
- delegation traces across agents

The new labs should teach failure modes that do not appear clearly in a single-agent system:

- spoofed agent identity
- fake or poisoned tool descriptors
- untrusted MCP endpoint registration
- insecure inter-agent messages
- replayed delegation requests
- one poisoned output cascading through a delegation chain
- rogue peer agent intercepting or imitating a legitimate role

### Why this is the v2.0 core

This is the natural extension of BrokenPilot. It reuses the control-toggle model, the existing authorization and audit concepts, and the capstone structure. It adds new trust boundaries instead of replacing the course.

### New teachable controls

The v2.0 multi-agent track should introduce controls such as:

- signed agent descriptors
- pinned tool and server descriptors
- mutual authentication between agents and tool brokers
- audience-bound delegation tokens
- anti-replay nonces and timestamps
- capability allowlists
- tool-broker mediation
- descriptor-change approval
- cross-agent audit correlation
- policy checks before delegation and before action

## v2.1 core: automated red teaming and evals in CI

### What it adds

Move Module 11 from manual red-team execution into automated adversarial evaluation:

- adversarial prompt generators
- behavior-gated test harnesses
- regression evals for known failure modes
- CI gates that fail when a fixed behavior regresses
- evidence reports that distinguish exploitability from noise

This should reuse BrokenPilot v1 and the multi-agent target from v2.0 as systems under test.

### Why it matters

v1 teaches that signature filters and marker checks are weak. v2.1 should have students build the generator that bypasses weak controls and the regression eval that catches the weakness when it comes back.

This is also a strong differentiator: most security courses ask students to run tests; this track asks them to build security evals that can be kept in CI.

## v2.2 depth: blue-team build track

### What it adds

Convert selected v1 reasoning deliverables into implementation work:

- implement retrieval authorization
- implement output encoding
- implement tool authorization
- implement approval gates
- implement memory isolation or review queues
- implement audit evidence improvements
- prove fixes with tests

### Why it matters

This is the difference between "explain the fix" and "merge the fix and prove it holds." It keeps the course centered on security engineering rather than security awareness.

## v2.2 secondary: runnable MLOps supply-chain lab

### What it adds

Upgrade the Module 08 evidence-pack reasoning lab into a runnable supply-chain lab:

- sign a model artifact
- generate build provenance
- produce a model or ML bill of materials
- detect unsigned, tampered, or unapproved artifacts at a promotion gate
- compare accuracy-only promotion to security-aware promotion

### Why it matters

The current evidence-pack lab is a strong reasoning exercise. A runnable version would make artifact integrity and promotion gates observable in the same way BrokenPilot makes agent controls observable.

## Later: assurance and governance bridge

A future track may connect the security-engineering spine to assurance and governance:

- NIST AI RMF operationalization
- EU AI Act technical-control mapping
- AI incident response for agentic systems
- residual-risk reporting for leadership and governance bodies

This should remain a bridge. It should not turn the course into a governance course.

## Later: program maturity

A separate product/program decision could add:

- scored rubric banks
- proctored capstone variants
- instructor certification
- badges or certificates
- delivery partner guidance

This is not v2.0 content work. It is a program-operating model.

## Cross-cutting investment: living-content model

v2 must not become a larger static snapshot. Agentic security, MCP security, supply-chain tooling, and evaluation methods move quickly.

Add a freshness discipline:

- maintain a threat-landscape page with an owner and review cadence
- track source freshness for fast-moving references
- flag deprecated tool versions
- flag dead links
- separate stable principles from current incidents and tooling

The goal is not to chase every headline. The goal is to make the course honest about what is stable knowledge and what must be reviewed periodically.

## v2 lab quality bar

A v2 upgrade should not ship unless it has:

- a runnable or evidence-backed lab
- an observable failure mode
- a visible control or mitigation
- a naive-fix failure case
- a defense-in-depth discussion
- a graded deliverable
- instructor facilitation guidance
- a student-facing evidence template
- a test, validation artifact, or review checklist

A descriptive-only v2 module would regress the bar set by v1.1.0.

## Recommended phasing

### v2.0

Multi-agent and MCP security plus the living-content model.

Deliverables:

- BrokenPilot v2 multi-agent design
- MCP/tool-broker trust-boundary lab
- cascading failure lab
- signed descriptor and tool-broker control lab
- freshness model and CI guard prototype

### v2.1

Automated red teaming and security evals in CI.

Deliverables:

- adversarial prompt generator lab
- behavior-gated eval harness
- CI security regression gate
- eval report template

### v2.2

Blue-team build track and runnable MLOps supply-chain lab.

Deliverables:

- build-and-prove BrokenPilot controls
- runnable model-artifact signing/provenance lab
- promotion-gate tests

### Later

Assurance bridge and program maturity.

## What not to do

- Do not destabilize v1.1.0 while building v2.
- Do not add a module without a lab that meets the quality bar.
- Do not rebuild from scratch.
- Do not make governance the center of gravity.
- Do not turn the course into a collection of current-event notes.
- Do not wire v2 into the published course navigation until there is a coherent v2 release candidate.

## First implementation step

Start with design scaffolding, not code:

1. Define the BrokenPilot v2 multi-agent architecture.
2. Define the MCP/tool-broker trust boundary.
3. Define the first cascading-failure lab.
4. Define the control toggles and tests.
5. Only then implement the v2 prototype.
