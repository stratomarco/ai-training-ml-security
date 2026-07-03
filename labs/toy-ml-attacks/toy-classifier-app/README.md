# Toy Classifier App: Observable Classical ML Attacks

This lab is a small, deterministic target for Modules 03 and 10. It intentionally stays separate from BrokenPilot because classical ML attacks target models, features, thresholds, and training data. BrokenPilot is an LLM/RAG/agent app and should not be forced to teach classifier behavior.

All data is synthetic and local. There are no downloads, no external services, and no real-world bypass payloads.

## What this demonstrates

| Script | Security lesson | Module mapping | OWASP ML mapping |
|---|---|---|---|
| `attacks/evasion.py` | A small input perturbation can change a classifier decision | 03, 10 | ML01 Input Manipulation |
| `attacks/poisoning.py` | A few poisoned training labels can change model behavior | 03, 10 | ML02 Data Poisoning |
| `attacks/extraction.py` | Query access can approximate a decision boundary | 03 | ML05 Model Theft |
| `attacks/output_integrity.py` | Tampering score-to-decision logic changes outcomes without changing the model | 03 | ML09 Output Integrity |

## Setup

PowerShell:

```powershell
cd labs\toy-ml-attacks\toy-classifier-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

macOS/Linux:

```bash
cd labs/toy-ml-attacks/toy-classifier-app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

## Run the baseline model

```bash
python train.py
```

Expected observation:

```text
trained_messages=48
validation_prediction=phish phish_probability=...
```

## Run the attacks

```bash
python attacks/evasion.py
python attacks/poisoning.py
python attacks/extraction.py
python attacks/output_integrity.py
```

Each script prints a before and after comparison. Students should capture the output, explain the changed security property, and propose a control or residual-risk decision.

## Run tests

Install `requirements-dev.txt` if you have not already done so, then run:

```bash
pytest
```

Expected:

```text
6 passed
```

## Teaching notes

This is not a malware, phishing, or bypass lab. The messages are synthetic classroom artifacts. The point is to observe how ML system behavior changes when inputs, training labels, query access, or output interpretation change.

The main engineering decision is whether a classifier should be used as a hard security gate. For this toy system, the answer should be no. The safer design is to use classifier output as one signal among others, with calibrated thresholds, review queues, fallback behavior, monitoring, and recovery.
