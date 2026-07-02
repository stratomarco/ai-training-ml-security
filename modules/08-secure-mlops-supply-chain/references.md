# Module 08 References  -  Secure MLOps and AI Supply Chain

## Primary references

- NIST SP 800-218  -  Secure Software Development Framework (SSDF): https://csrc.nist.gov/publications/detail/sp/800-218/final
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Generative AI Profile, NIST AI 600-1: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- OWASP Machine Learning Security Top 10  -  ML06: AI Supply Chain Attacks: https://owasp.org/www-project-machine-learning-security-top-10/
- OWASP Top 10 for Large Language Model Applications: https://www.owasp.org/www-project-top-10-for-large-language-model-applications/
- SLSA  -  Supply-chain Levels for Software Artifacts: https://slsa.dev/
- MITRE ATLAS  -  adversarial AI tactics and techniques: https://atlas.mitre.org/
- BIML  -  ML and LLM architectural risk analysis: https://berryvilleiml.com/
- BIML  -  Architectural Risk Analysis of Large Language Models: https://berryvilleiml.com/docs/BIML-LLM24.pdf

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

- Module 02  -  ML System Architecture
- Module 03  -  OWASP ML Security Top 10
- Module 04  -  BIML Architectural Risk Analysis
- Module 06  -  RAG Security
- Module 07  -  Agent and Tool Security
- Module 09  -  Privacy Attacks and Data Protection
- BrokenPilot capstone
