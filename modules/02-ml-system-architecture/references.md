# Module 02 References  -  ML System Architecture

This module uses references that connect ML architecture, ML lifecycle risk, secure MLOps, and AI system threat modeling.

## Primary references

### OWASP Machine Learning Security Top 10

- Project: https://owasp.org/www-project-machine-learning-security-top-10/
- Use in this module: helps map architecture components to ML-specific risks such as data poisoning, model theft, model inversion, membership inference, and supply chain attacks.

### OWASP Top 10 for Large Language Model Applications

- Project: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Use in this module: helps extend ML architecture thinking into LLM application components such as prompts, retrieved context, tools, outputs, and model access.

### BIML  -  Architectural Risk Analysis of Machine Learning Systems

- BIML results page: https://berryvilleiml.com/results/
- Use in this module: supports the idea that ML security should be approached as architectural risk analysis, not only as isolated adversarial examples.

### BIML  -  Architectural Risk Analysis of Large Language Models

- PDF: https://berryvilleiml.com/docs/BIML-LLM24.pdf
- Use in this module: supports the extension from generic ML architecture to LLM architecture risk.

### NIST AI Risk Management Framework

- AI RMF page: https://www.nist.gov/itl/ai-risk-management-framework
- GenAI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Use in this module: provides governance and lifecycle risk-management framing.

### MITRE ATLAS

- Project: https://atlas.mitre.org/
- Use in this module: provides adversarial AI tactics, techniques, mitigations, and case studies that can be mapped to lifecycle components.

## Classic security references to connect back to Module 01

### Ross Anderson  -  Security Engineering

- Site: https://www.cl.cam.ac.uk/~rja14/book.html
- Use in this module: reinforces that AI systems should be reviewed as real-world security engineering systems with incentives, failures, operations, and human factors.

### Gary McGraw  -  Software Security

- Book page / author resources: https://www.swsec.com/
- Use in this module: reinforces building security in through architecture, design review, and secure development practice.

### Adam Shostack  -  Threat Modeling

- Site: https://shostack.org/
- Use in this module: supports data-flow diagrams, trust boundaries, and structured threat modeling.

## Recommended reading order

For students:

1. Module 02 student handout.
2. OWASP Machine Learning Security Top 10 overview.
3. MITRE ATLAS overview page.
4. NIST AI RMF overview.

For instructors:

1. BIML generic ML risk analysis.
2. BIML LLM architectural risk analysis.
3. OWASP ML Security Top 10.
4. OWASP LLM Top 10.
5. NIST AI RMF GenAI Profile.
6. MITRE ATLAS matrix.

## Notes

This module intentionally avoids deep mathematical treatment of ML algorithms. The purpose is architecture-level reasoning: where data moves, where behavior is created, where trust boundaries exist, and where controls should be enforced.
