from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from toy_classifier.model import predict_one, train_pipeline

TARGET = "payment failed verify invoice credential immediately"
NORMAL_THRESHOLD = 0.50
TAMPERED_THRESHOLD = 0.95


def run_output_integrity() -> dict[str, dict[str, object]]:
    model = train_pipeline()
    before = predict_one(model, TARGET, threshold=NORMAL_THRESHOLD)
    after = predict_one(model, TARGET, threshold=TAMPERED_THRESHOLD)
    return {"before": before, "after": after}


def main() -> None:
    result = run_output_integrity()
    print("Output integrity failure by threshold tampering")
    print("The model is unchanged. Only the score-to-decision rule changed.")
    for key in ["before", "after"]:
        row = result[key]
        print(
            f"{key}: label={row['label']} "
            f"threshold={row['threshold']:.2f} "
            f"phish_probability={row['phish_probability']:.3f} "
            f"text={row['text']}"
        )
    print("Observation: output interpretation is part of the security boundary.")


if __name__ == "__main__":
    main()
