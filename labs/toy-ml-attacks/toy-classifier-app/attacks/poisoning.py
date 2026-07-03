from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from toy_classifier.model import load_messages, predict_one, train_pipeline

TARGET = "payment failed verify invoice credential immediately"
POISON_TERMS = {"invoice", "payment", "credential"}
MAX_FLIPS = 4


def poison_messages(max_flips: int = MAX_FLIPS) -> tuple[list[dict[str, str]], list[str]]:
    messages = load_messages()
    poisoned: list[dict[str, str]] = []
    flipped_ids: list[str] = []
    for row in messages:
        clone = dict(row)
        terms = set(clone["text"].split())
        if (
            len(flipped_ids) < max_flips
            and clone["label"] == "phish"
            and POISON_TERMS.intersection(terms)
        ):
            clone["label"] = "safe"
            flipped_ids.append(clone["id"])
        poisoned.append(clone)
    return poisoned, flipped_ids


def run_poisoning() -> dict[str, object]:
    clean_messages = load_messages()
    clean_model = train_pipeline(clean_messages)
    poisoned_messages, flipped_ids = poison_messages()
    poisoned_model = train_pipeline(poisoned_messages)
    before = predict_one(clean_model, TARGET)
    after = predict_one(poisoned_model, TARGET)
    return {"before": before, "after": after, "flipped_ids": flipped_ids}


def main() -> None:
    result = run_poisoning()
    print("Data poisoning by deterministic label flips")
    print(f"flipped_training_ids={','.join(result['flipped_ids'])}")
    for key in ["before", "after"]:
        row = result[key]
        print(
            f"{key}: label={row['label']} "
            f"phish_probability={row['phish_probability']:.3f} "
            f"text={row['text']}"
        )
    print("Observation: a small set of poisoned labels changed detection behavior.")


if __name__ == "__main__":
    main()
