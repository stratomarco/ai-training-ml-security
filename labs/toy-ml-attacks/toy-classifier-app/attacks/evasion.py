from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from toy_classifier.model import predict_one, train_pipeline

ORIGINAL = "urgent password reset verify account credential token"
PERTURBED = "project status update meeting notes roadmap safe"


def run_evasion() -> dict[str, dict[str, object]]:
    model = train_pipeline()
    before = predict_one(model, ORIGINAL)
    after = predict_one(model, PERTURBED)
    return {"before": before, "after": after}


def main() -> None:
    result = run_evasion()
    print("Evasion by synthetic word-swap perturbation")
    print("Security question: should this classifier be a hard authorization gate?")
    for key in ["before", "after"]:
        row = result[key]
        print(
            f"{key}: label={row['label']} "
            f"phish_probability={row['phish_probability']:.3f} "
            f"text={row['text']}"
        )
    print("Observation: the intent label changed after input perturbation.")


if __name__ == "__main__":
    main()
