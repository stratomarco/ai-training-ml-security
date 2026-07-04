
from __future__ import annotations

"""
Intent-preserving evasion demonstration for the toy classifier.

This script is deliberately small and synthetic. It does not show a real-world
phishing bypass. It shows the security property: an input can preserve the same
malicious intent while perturbations move the model decision across the boundary.
"""

import json
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "messages.json"

ORIGINAL = "urgent password reset verify account credential token"
BENIGN_FILLER = (
    "project status update meeting notes roadmap planning sprint backlog "
    "lunch calendar documentation release safe normal internal update"
)


def _field(item: dict[str, Any], names: list[str]) -> str:
    for name in names:
        value = item.get(name)
        if isinstance(value, str) and value.strip():
            return value.strip()
    raise KeyError(f"missing one of {names} in dataset item: {item}")


def load_dataset() -> tuple[list[str], list[str]]:
    data = json.loads(DATASET.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("messages") or data.get("samples") or data.get("data")
    if not isinstance(data, list):
        raise ValueError("messages.json must contain a list or an object with messages/samples/data")

    texts: list[str] = []
    labels: list[str] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        texts.append(_field(item, ["text", "message", "content", "body"]))
        labels.append(_field(item, ["label", "class", "target"]).lower())
    if len(set(labels)) < 2:
        raise ValueError("dataset must contain at least two labels")
    return texts, labels


def positive_label(labels: list[str]) -> str:
    for candidate in ["phish", "phishing", "malicious", "spam", "attack"]:
        if candidate in set(labels):
            return candidate
    # Fall back to any label that is not the common benign class.
    for label in sorted(set(labels)):
        if label not in {"safe", "benign", "ham", "normal"}:
            return label
    return sorted(set(labels))[0]


def train_model() -> tuple[Pipeline, str]:
    texts, labels = load_dataset()
    pos = positive_label(labels)
    model = Pipeline(
        steps=[
            ("vectorizer", CountVectorizer(ngram_range=(1, 2))),
            ("classifier", LogisticRegression(max_iter=1000, random_state=7)),
        ]
    )
    model.fit(texts, labels)
    return model, pos


def score(model: Pipeline, positive: str, text: str) -> tuple[str, float]:
    pred = str(model.predict([text])[0])
    classes = list(model.named_steps["classifier"].classes_)
    probs = model.predict_proba([text])[0]
    if positive not in classes:
        raise ValueError(f"positive label {positive!r} not found in classes {classes}")
    return pred, float(probs[classes.index(positive)])


def find_intent_preserving_evasion(model: Pipeline, positive: str) -> str:
    """Return a perturbed input that keeps the malicious core text intact."""
    # The malicious sentence remains as a literal substring. Only benign-looking
    # context is added around it. This demonstrates evasion, not a swap to a
    # different benign message.
    candidates = []
    for repeats in range(1, 81):
        filler = " ".join([BENIGN_FILLER] * repeats)
        candidates.append(f"{ORIGINAL} {filler}")
        candidates.append(f"{filler} {ORIGINAL} {filler}")

    original_pred, _ = score(model, positive, ORIGINAL)
    for candidate in candidates:
        pred, probability = score(model, positive, candidate)
        if ORIGINAL in candidate and original_pred == positive and pred != positive and probability < 0.50:
            return candidate

    # If the exact flip is not reachable on a future dataset, return the lowest
    # scoring intent-preserving perturbation so the instructor can discuss why
    # this model resisted the simple attack. The test suite uses the shipped
    # deterministic dataset, where the flip is expected.
    return min(candidates, key=lambda candidate: score(model, positive, candidate)[1])


def run_demo() -> dict[str, Any]:
    model, positive = train_model()
    perturbed = find_intent_preserving_evasion(model, positive)

    original_pred, original_prob = score(model, positive, ORIGINAL)
    perturbed_pred, perturbed_prob = score(model, positive, perturbed)

    return {
        "positive_label": positive,
        "original": ORIGINAL,
        "perturbed": perturbed,
        "intent_preserved": ORIGINAL in perturbed,
        "original_prediction": original_pred,
        "original_positive_probability": round(original_prob, 3),
        "perturbed_prediction": perturbed_pred,
        "perturbed_positive_probability": round(perturbed_prob, 3),
        "decision_flipped": original_pred != perturbed_pred,
        "teaching_point": (
            "The perturbed input preserves the malicious core text but adds enough "
            "benign-looking context to move the classifier decision. This is evasion; "
            "it is not a comparison between unrelated malicious and benign messages."
        ),
    }


def main() -> None:
    result = run_demo()
    print("Intent-preserving evasion demo")
    print(json.dumps(result, indent=2))


def run_evasion():
    """Compatibility entry point used by tests and course material.

    Returns the old nested before/after shape while preserving the newer
    run_demo() fields. The evasion demo must keep malicious intent in the
    perturbed message while changing the classifier decision.
    """
    result = run_demo()

    original_text = result.get("original") or result.get("original_text")
    perturbed_text = result.get("perturbed") or result.get("perturbed_text")

    before_label = (
        result.get("original_prediction")
        or result.get("before_label")
        or result.get("before_prediction")
    )
    after_label = (
        result.get("perturbed_prediction")
        or result.get("after_label")
        or result.get("after_prediction")
    )

    # Normalize older benign naming to the label expected by the lab tests.
    if before_label == "benign":
        before_label = "safe"
    if after_label == "benign":
        after_label = "safe"

    before_probability = (
        result.get("original_positive_probability")
        or result.get("before_probability")
        or result.get("before_phish_probability")
    )
    after_probability = (
        result.get("perturbed_positive_probability")
        or result.get("after_probability")
        or result.get("after_phish_probability")
    )

    compatible = dict(result)
    compatible["before"] = {
        "text": original_text,
        "label": before_label,
        "phish_probability": before_probability,
    }
    compatible["after"] = {
        "text": perturbed_text,
        "label": after_label,
        "phish_probability": after_probability,
    }

    compatible["original_text"] = original_text
    compatible["perturbed_text"] = perturbed_text
    compatible["before_label"] = before_label
    compatible["after_label"] = after_label
    compatible["before_probability"] = before_probability
    compatible["after_probability"] = after_probability

    return compatible

if __name__ == "__main__":
    main()
