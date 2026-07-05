# Lab troubleshooting and reset guide

This guide keeps classroom support from overwhelming the instructor.

## General reset order

1. Confirm the student is in the correct directory.
2. Confirm the virtual environment is active.
3. Confirm dependencies are installed.
4. Reset generated state.
5. Re-run the smallest test.
6. Only then inspect application code.

## BrokenPilot quick checks

From `labs/brokenpilot/prototype-app`:

```powershell
python -m pip install -r requirements.txt
pytest
```

If a scenario behaves differently than expected:

- call `/reset`
- check `/controls`
- verify the user, tenant, and role
- verify the control flag being tested
- run the relevant test function before changing code

## Toy classifier quick checks

From `labs/toy-ml-attacks/toy-classifier-app`:

```powershell
python -m pip install -r requirements-dev.txt
python train.py
pytest
```

If attack output differs:

- delete generated model files
- re-run `python train.py`
- confirm the synthetic dataset was not edited
- confirm scikit-learn installed from the project requirements

## MLOps evidence pack checks

The evidence pack is not meant to run. Students inspect it. If a student tries to execute the notebook or pipeline, redirect them to the evidence-review task.

The intended task is to identify weak provenance, weak artifact integrity, weak promotion gates, and missing rollback evidence.

## What not to debug during class

- MkDocs strict navigation warnings
- OneDrive file locks on generated website folders
- cosmetic markdown warnings
- optional external DVAIA setup if the core BrokenPilot path is available

Those belong to release maintenance, not live teaching.
