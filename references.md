# References

This file contains the initial reference spine for the course.

## Core AI and ML security references

- OWASP Machine Learning Security Top 10: https://owasp.org/www-project-machine-learning-security-top-10/
- OWASP Top 10 for Large Language Model Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP GenAI Security Project: https://genai.owasp.org/
- OWASP LLM Top 10 latest archive: https://genai.owasp.org/llm-top-10/
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP Agentic AI Threats and Mitigations: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
- OWASP Agentic Skills Top 10: https://owasp.org/www-project-agentic-skills-top-10/
- MITRE ATLAS: https://atlas.mitre.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Generative AI Profile, NIST AI 600-1: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST Adversarial Machine Learning taxonomy, NIST AI 100-2e2023: https://csrc.nist.gov/pubs/ai/100/2/e2023/final
- BIML Results: https://berryvilleiml.com/results/
- BIML Interactive Machine Learning Risk Framework: https://berryvilleiml.com/interactive/
- BIML Architectural Risk Analysis of Large Language Models: https://berryvilleiml.com/docs/BIML-LLM24.pdf

## Lab references

- DVAIA — Damn Vulnerable AI Application: https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application
- Damn Vulnerable AI Agent: https://github.com/opena2a-org/damn-vulnerable-ai-agent

## Classic security engineering references

- Gary McGraw, *Software Security: Building Security In*
- Gary McGraw, *Exploiting Software: How to Break Code*
- Ross Anderson, *Security Engineering*
- Adam Shostack, *Threat Modeling: Designing for Security*
- Adam Shostack, *Threats: What Every Engineer Should Learn From Star Wars*
- Saltzer and Schroeder, *The Protection of Information in Computer Systems*
- Bruce Schneier, *Secrets and Lies*
- John Viega and Gary McGraw, *Building Secure Software*

## Cryptography references

- Jean-Philippe Aumasson, *Serious Cryptography*
- David Wong, *Real-World Cryptography*
- NIST Cryptographic Standards and Guidelines: https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines

## Application security references

- OWASP Top 10 Web Application Security Risks: https://owasp.org/www-project-top-ten/
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Software Assurance Maturity Model: https://owasp.org/www-project-samm/
- CWE: https://cwe.mitre.org/
- CVE: https://www.cve.org/
- MITRE ATT&CK: https://attack.mitre.org/

## Supply chain references

- SLSA: https://slsa.dev/
- OpenSSF Scorecard: https://securityscorecards.dev/
- Sigstore: https://www.sigstore.dev/
- CycloneDX: https://cyclonedx.org/
- SPDX: https://spdx.dev/

## Privacy and data protection references

- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- GDPR official portal: https://commission.europa.eu/law/law-topic/data-protection_en

## Suggested reading order

For students new to the topic:

1. OWASP LLM Top 10
2. OWASP ML Security Top 10
3. MITRE ATLAS overview
4. NIST AI RMF overview
5. BIML LLM architectural risk analysis
6. Adam Shostack on threat modeling
7. Ross Anderson on security engineering
8. Gary McGraw on building security in

For security architects:

1. Ross Anderson
2. Gary McGraw
3. Adam Shostack
4. BIML ML and LLM risk analysis
5. NIST AI RMF and GenAI Profile
6. OWASP LLM, ML, and Agentic material
7. MITRE ATLAS

For red teams:

1. OWASP LLM Top 10
2. MITRE ATLAS
3. DVAIA
4. Damn Vulnerable AI Agent
5. OWASP Agentic Applications Top 10
6. BIML LLM risk analysis


## Adversarial ML taxonomy

- NIST AI 100-2 E2025 — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations  
  https://csrc.nist.gov/pubs/ai/100/2/e2025/final


## Module 5 — LLM Application Security

- OWASP Top 10 for Large Language Model Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP GenAI Security Project: https://genai.owasp.org/
- OWASP LLM Top 10 2025 PDF: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
- DVAIA — Damn Vulnerable AI Application: https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application


## RAG and indirect prompt injection references

- OWASP LLM01 — Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- NIST AI 600-1 — Generative AI Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- DVAIA — Damn Vulnerable AI Application: https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application


## Agent and tool security references

- OWASP Top 10 for Agentic Applications for 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP Agentic Applications release summary: https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/
- OWASP Top 10 for Large Language Model Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- NIST AI 600-1 — Generative AI Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- MITRE ATLAS: https://atlas.mitre.org/


## BrokenPilot capstone reference focus

The BrokenPilot capstone should reuse the course-wide reference set rather than introduce a separate framework. It primarily draws from:

- Classic security engineering and threat modeling.
- OWASP LLM/GenAI risks for prompt injection, output handling, excessive agency, overreliance, model DoS, and model theft.
- OWASP Agentic risks for tool use, autonomy, memory, and workflow execution.
- OWASP ML risks for poisoning, model/data supply chain, model theft, and output integrity.
- BIML-style architectural risk analysis.
- NIST AI RMF and GenAI profile for risk management and governance framing.
- MITRE ATLAS for adversarial AI tactics and technique mapping.


## Secure MLOps and Supply Chain References

- NIST SP 800-218 — Secure Software Development Framework (SSDF)
- NIST AI Risk Management Framework and Generative AI Profile
- OWASP ML Security Top 10 — ML06: AI Supply Chain Attacks
- OWASP Top 10 for Large Language Model Applications — supply chain, sensitive information disclosure, excessive agency, model theft
- SLSA — Supply-chain Levels for Software Artifacts
- MITRE ATLAS — adversarial AI tactics and techniques

Module 08 uses these references to connect conventional secure development and software supply chain controls to ML-specific artifacts such as datasets, labels, features, model files, prompts, adapters, embeddings, vector indexes, evaluation results, registries, and feedback loops.
