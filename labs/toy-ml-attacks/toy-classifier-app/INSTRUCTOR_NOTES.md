# Instructor Notes for the Toy Classifier App

The app is intentionally deterministic and synthetic. Keep the framing tight: it is a teaching model for security reasoning, not a benchmark or realistic classifier.

## Expected commands

```bash
python train.py
python attacks/evasion.py
python attacks/poisoning.py
python attacks/extraction.py
python attacks/output_integrity.py
pytest
```

## Expected observations

| Script | Student should observe |
|---|---|
| `evasion.py` | A small perturbation changes the decision. |
| `poisoning.py` | A small number of poisoned labels changes retrained behavior. |
| `extraction.py` | Repeated queries reveal approximate decision behavior. |
| `output_integrity.py` | Threshold changes alter decisions without changing the model. |

## What not to teach

Do not teach this as a realistic phishing detector. Do not claim the perturbations are production bypasses. Do not imply the attacks are exhaustive. The lab is a controlled microscope for concepts.

## What to teach

Teach that the model is one part of a decision system. The security review must include data provenance, interface exposure, configuration integrity, monitoring, fallback, and residual risk.

## Reset guidance

The lab can be reset by deleting generated model artifacts and rerunning training:

```bash
rm -f model.pkl
python train.py
pytest
```

PowerShell:

```powershell
Remove-Item .\model.pkl -ErrorAction SilentlyContinue
python train.py
pytest
```
