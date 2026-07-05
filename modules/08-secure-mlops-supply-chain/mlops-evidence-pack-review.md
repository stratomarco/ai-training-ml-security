# Module 08 Lab: MLOps Evidence Pack Review

This Module 08 lab uses a static evidence pack instead of a fake runnable pipeline.

## Core decision

Should the model candidate be promoted to a production-candidate registry?

## Review target

```text
labs/mlops-supply-chain-labs/evidence-pack-review/
```

## Why this fits Module 08

MLOps supply-chain security is mostly an evidence and control problem. The reviewer needs to know whether dependencies, data, training code, model artifacts, registry entries, promotion gates, and rollback plans are trustworthy.

## What students must produce

Students produce a review memo and a remediation backlog. The best submissions show:

- artifact provenance and integrity gaps;
- weak identity and storage boundaries;
- missing reproducibility evidence;
- weak promotion policy;
- specific controls such as lockfiles, dataset manifests, signed artifacts, immutable artifact paths, approval gates, and rollback plans;
- a validation plan for each control.
