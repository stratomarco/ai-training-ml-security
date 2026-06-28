# Module 08 References — Secure MLOps and AI Supply Chain

## Primary references

- NIST SP 800-218 — Secure Software Development Framework (SSDF)
- NIST AI Risk Management Framework and Generative AI Profile
- OWASP Machine Learning Security Top 10 — ML06: AI Supply Chain Attacks
- OWASP Top 10 for Large Language Model Applications — supply chain, sensitive information disclosure, excessive agency, model theft
- SLSA — Supply-chain Levels for Software Artifacts
- MITRE ATLAS — adversarial AI tactics and techniques
- BIML — ML and LLM architectural risk analysis

## Concepts to connect

| Concept | Why it matters in this module |
|---|---|
| Secure SDLC | ML pipelines still require secure development and release practices. |
| Software supply chain | ML systems depend on code, packages, containers, and build systems. |
| Data provenance | Training and evaluation data directly shape production behavior. |
| Artifact integrity | Model files, prompts, adapters, and vector indexes require integrity controls. |
| Registry governance | Model registry is a production control point, not passive storage. |
| Least privilege | Training, registry, deployment, and runtime identities must be scoped. |
| Evaluation gates | Security, privacy, robustness, and abuse-case tests should influence promotion. |
| Incident response | Bad models require rollback, investigation, and affected-scope analysis. |

## Suggested reading questions

When reviewing these references, ask:

1. Which parts of normal software supply chain security apply directly to ML?
2. Which artifacts exist in ML that do not exist in normal application delivery?
3. How does provenance change security review quality?
4. Which controls protect against tampering?
5. Which controls protect against accidental unsafe release?
6. Which controls help incident response after a bad model release?
7. How should promotion gates differ by model risk tier?

## Related course material

- Module 02 — ML System Architecture
- Module 03 — OWASP ML Security Top 10
- Module 04 — BIML Architectural Risk Analysis
- Module 06 — RAG Security
- Module 07 — Agent and Tool Security
- Module 09 — Privacy Attacks and Data Protection
- BrokenPilot capstone
