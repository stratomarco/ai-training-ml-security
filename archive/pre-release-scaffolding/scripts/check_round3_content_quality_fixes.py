from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def text(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        raise AssertionError(f"missing required file: {path}")
    return p.read_text(encoding="utf-8")


def require(path: str, *needles: str) -> None:
    content = text(path)
    for needle in needles:
        if needle not in content:
            raise AssertionError(f"{path} missing expected text: {needle}")


def forbid(path: str, *needles: str) -> None:
    p = ROOT / path
    if not p.exists():
        return
    content = p.read_text(encoding="utf-8")
    for needle in needles:
        if needle in content:
            raise AssertionError(f"{path} still contains forbidden text: {needle}")


def main() -> None:
    require(
        "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py",
        "Intent-preserving evasion demonstration",
        "ORIGINAL in perturbed",
        "find_intent_preserving_evasion",
        "it is not a comparison between unrelated malicious and benign messages",
    )
    require(
        "labs/toy-ml-attacks/toy-classifier-app/tests/test_toy_classifier.py",
        "test_evasion_preserves_malicious_intent_before_decision_flip",
        "ORIGINAL in result",
    )
    require(
        "labs/agent-labs/README.md",
        "consolidated into BrokenPilot",
        "not graded as standalone labs",
    )
    require(
        "labs/rag-labs/README.md",
        "consolidated into BrokenPilot",
        "not graded as standalone labs",
    )
    require(
        "labs/dvaia-guides/README.md",
        "optional appendix",
        "no longer the critical path",
    )
    require(
        "modules/05-llm-application-security/brokenpilot-direct-injection-output-lab.md",
        "POST /render",
        "ENABLE_OUTPUT_ENCODING=false",
        "ENABLE_OUTPUT_ENCODING=true",
    )
    require(
        "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md",
        "POST /render",
        "ENABLE_OUTPUT_ENCODING",
        "Graded artifact",
    )
    require(
        "modules/01-security-engineering-for-ai/exercise-deliverable-anchor.md",
        "Graded artifact",
        "threat model",
        "residual risk",
    )
    require(
        "modules/02-ml-system-architecture/exercise-deliverable-anchor.md",
        "Graded artifact",
        "architecture and data-flow map",
        "trust boundaries",
    )
    require(
        "ROUND3_CONTENT_QUALITY_FIXES.md",
        "BrokenPilot is the primary runnable target",
        "DVAIA is optional appendix material",
    )
    forbid("COURSE_DRY_RUN_PLAN_40H.md", "DVAIA and BrokenPilot validation")
    forbid("instructor/40-hour-student-experience-runbook.md", "DVAIA and BrokenPilot validation")

    print("Round 3 content quality checks passed.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"Round 3 content quality check failed: {exc}", file=sys.stderr)
        sys.exit(1)
