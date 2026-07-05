from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from toy_classifier.model import LABELS, decision_from_probability, phish_probability, predict_one, train_pipeline

SAFE_TERMS = [
    "project status meeting notes safe",
    "team lunch agenda safe",
    "release notes documentation safe",
    "calendar invite onboarding safe",
    "design review feedback safe",
]
PHISH_TERMS = [
    "urgent password credential token",
    "payment invoice verify credential",
    "account locked login password",
    "wire transfer secret payment",
    "mfa token secret approval",
]
MIXERS = ["", " today", " please", " internal", " external", " immediate"]


def query_victim(victim_model) -> list[dict[str, object]]:
    queries: list[str] = []
    for base in SAFE_TERMS + PHISH_TERMS:
        for suffix in MIXERS:
            queries.append((base + suffix).strip())
    for safe in SAFE_TERMS:
        for phish in PHISH_TERMS[:3]:
            queries.append(f"{safe} {phish}")
            queries.append(f"{phish} {safe}")

    observations = []
    for text in queries:
        pred = predict_one(victim_model, text)
        observations.append({"id": f"Q{len(observations):03d}", "text": text, "label": pred["label"]})
    return observations


def train_surrogate(observations: list[dict[str, object]]):
    return train_pipeline([{"id": row["id"], "text": row["text"], "label": row["label"]} for row in observations])


def evaluate_agreement(victim_model, surrogate_model) -> dict[str, object]:
    holdout = [
        "urgent password credential token external",
        "payment invoice verify credential please",
        "team lunch agenda internal safe",
        "release notes documentation today safe",
        "account locked login password immediate",
        "design review feedback safe",
        "wire transfer secret payment immediate",
        "calendar invite onboarding safe",
        "project status meeting notes payment invoice verify credential",
        "payment invoice verify credential project status meeting notes safe",
    ]
    rows = []
    agree = 0
    for text in holdout:
        victim = predict_one(victim_model, text)
        surrogate = predict_one(surrogate_model, text)
        if victim["label"] == surrogate["label"]:
            agree += 1
        rows.append({"text": text, "victim": victim["label"], "surrogate": surrogate["label"]})
    return {"agreement": agree / len(holdout), "rows": rows}


def run_extraction() -> dict[str, object]:
    victim_model = train_pipeline()
    observations = query_victim(victim_model)
    surrogate_model = train_surrogate(observations)
    evaluation = evaluate_agreement(victim_model, surrogate_model)
    return {"queries": len(observations), "agreement": evaluation["agreement"], "rows": evaluation["rows"]}


def main() -> None:
    result = run_extraction()
    print("Model extraction by repeated synthetic queries")
    print(f"victim_queries={result['queries']}")
    print(f"surrogate_agreement={result['agreement']:.2f}")
    for row in result["rows"]:
        print(f"victim={row['victim']} surrogate={row['surrogate']} text={row['text']}")
    print("Observation: query access can approximate decision behavior.")


if __name__ == "__main__":
    main()
