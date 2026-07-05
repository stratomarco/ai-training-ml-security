from __future__ import annotations

import json
import pickle
from pathlib import Path
from typing import Iterable, Sequence

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

RANDOM_SEED = 42
LABELS = {"safe": 0, "phish": 1}
INVERSE_LABELS = {v: k for k, v in LABELS.items()}
ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "messages.json"
MODEL_PATH = ROOT / "model.pkl"


def load_messages(path: Path | str = DATA_PATH) -> list[dict[str, str]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("messages.json must contain a list of records")
    required = {"id", "text", "label"}
    for row in data:
        missing = required - set(row)
        if missing:
            raise ValueError(f"message row is missing fields: {sorted(missing)}")
        if row["label"] not in LABELS:
            raise ValueError(f"unknown label {row['label']!r}; expected safe or phish")
    return data


def train_pipeline(messages: Sequence[dict[str, str]] | None = None) -> Pipeline:
    rows = list(messages) if messages is not None else load_messages()
    texts = [row["text"] for row in rows]
    y = [LABELS[row["label"]] for row in rows]
    pipeline = Pipeline(
        steps=[
            ("vectorizer", CountVectorizer(lowercase=True, ngram_range=(1, 2), min_df=1)),
            (
                "classifier",
                LogisticRegression(
                    solver="liblinear",
                    random_state=RANDOM_SEED,
                    max_iter=1000,
                    C=1.0,
                ),
            ),
        ]
    )
    pipeline.fit(texts, y)
    return pipeline


def phish_probability(model: Pipeline, text: str) -> float:
    return float(model.predict_proba([text])[0][LABELS["phish"]])


def decision_from_probability(probability: float, threshold: float = 0.5) -> str:
    return "phish" if probability >= threshold else "safe"


def predict_one(model: Pipeline, text: str, threshold: float = 0.5) -> dict[str, object]:
    probability = phish_probability(model, text)
    return {
        "text": text,
        "phish_probability": probability,
        "threshold": threshold,
        "label": decision_from_probability(probability, threshold),
    }


def predict_many(model: Pipeline, texts: Iterable[str], threshold: float = 0.5) -> list[dict[str, object]]:
    return [predict_one(model, text, threshold=threshold) for text in texts]


def save_model(model: Pipeline, path: Path | str = MODEL_PATH) -> None:
    Path(path).write_bytes(pickle.dumps(model))


def load_model(path: Path | str = MODEL_PATH) -> Pipeline:
    return pickle.loads(Path(path).read_bytes())
