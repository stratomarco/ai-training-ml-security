# Toy Classifier Debrief for Module 03

Module 03 uses the toy-classifier app to turn OWASP ML categories into concrete evidence.

## Mapping

| Toy script | OWASP-style risk lesson | Student question |
|---|---|---|
| `evasion.py` | Input manipulation | What input changes cross the boundary? |
| `poisoning.py` | Data poisoning | What training-data controls failed? |
| `extraction.py` | Model theft and probing | What does query access reveal? |
| `output_integrity.py` | Output integrity | What changes the decision after model validation? |

## Debrief prompt

Do not ask only, "Which OWASP category is this?" Ask, "What evidence would make this a finding, and what control would change the security property?"

## Graded artifact

Students submit a short finding that includes:

1. observed behavior,
2. risk category,
3. root cause,
4. control,
5. validation,
6. residual risk.
