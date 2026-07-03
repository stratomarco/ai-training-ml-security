from __future__ import annotations

from pathlib import Path
import sys

APP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_ROOT))

from attacks.evasion import run_evasion
from attacks.extraction import run_extraction
from attacks.output_integrity import run_output_integrity
from attacks.poisoning import run_poisoning
from toy_classifier.model import load_messages, predict_one, train_pipeline


def test_dataset_is_synthetic_and_balanced_enough() -> None:
    rows = load_messages()
    labels = {row["label"] for row in rows}
    assert labels == {"safe", "phish"}
    assert len(rows) >= 40
    assert all(row["id"].startswith(("S", "P")) for row in rows)


def test_training_predicts_obvious_synthetic_phish_and_safe_messages() -> None:
    model = train_pipeline()
    phish = predict_one(model, "urgent password reset verify account credential token")
    safe = predict_one(model, "project status update meeting notes roadmap safe")
    assert phish["label"] == "phish"
    assert phish["phish_probability"] > 0.80
    assert safe["label"] == "safe"
    assert safe["phish_probability"] < 0.20


def test_evasion_word_swap_flips_the_decision() -> None:
    result = run_evasion()
    assert result["before"]["label"] == "phish"
    assert result["after"]["label"] == "safe"
    assert result["before"]["phish_probability"] - result["after"]["phish_probability"] > 0.70


def test_poisoning_label_flips_degrade_detection() -> None:
    result = run_poisoning()
    assert len(result["flipped_ids"]) == 4
    assert result["before"]["label"] == "phish"
    assert result["after"]["label"] == "safe"
    assert result["before"]["phish_probability"] - result["after"]["phish_probability"] > 0.50


def test_extraction_surrogate_approximates_victim_boundary() -> None:
    result = run_extraction()
    assert result["queries"] >= 50
    assert result["agreement"] >= 0.80


def test_output_integrity_threshold_tampering_changes_decision_without_changing_score() -> None:
    result = run_output_integrity()
    assert result["before"]["label"] == "phish"
    assert result["after"]["label"] == "safe"
    assert result["before"]["phish_probability"] == result["after"]["phish_probability"]
    assert result["before"]["threshold"] == 0.50
    assert result["after"]["threshold"] == 0.95
