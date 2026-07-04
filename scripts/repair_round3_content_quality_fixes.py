from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"updated: {path.relative_to(ROOT)}")


def patch_evasion_alias() -> None:
    path = ROOT / "labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py"
    text = read(path)
    if not text:
        raise SystemExit(f"missing {path}")

    if "def run_evasion(" not in text:
        alias = '''

def run_evasion():
    """Backward-compatible test entry point for the evasion demo."""
    result = run_demo()
    # Keep old and new naming styles available for tests and notebooks.
    result.setdefault("original_text", result.get("original"))
    result.setdefault("perturbed_text", result.get("perturbed"))
    result.setdefault("before_label", result.get("original_prediction"))
    result.setdefault("after_label", result.get("perturbed_prediction"))
    result.setdefault("before_probability", result.get("original_positive_probability"))
    result.setdefault("after_probability", result.get("perturbed_positive_probability"))
    return result
'''
        marker = '\n\nif __name__ == "__main__":'
        if marker in text:
            text = text.replace(marker, alias + marker)
        else:
            text = text.rstrip() + alias
        write(path, text)


def patch_output_handling_lab() -> None:
    path = ROOT / "labs/brokenpilot/prototype-app/OUTPUT_HANDLING_LAB.md"
    text = read(path)

    section = '''
# BrokenPilot Output Handling Lab

## Student path: POST /render

This lab demonstrates insecure output handling with a deterministic HTML sink.

### Vulnerable run

1. Start BrokenPilot.
2. Set `ENABLE_OUTPUT_ENCODING=false`.
3. Send a request to `POST /render`.
4. Use a message that retrieves the output-sink training content.
5. Observe that the response contains the raw benign marker `<b>OUTPUT_SINK_TRIGGERED</b>`.

### Controlled run

1. Set `ENABLE_OUTPUT_ENCODING=true`.
2. Repeat the same `POST /render` request.
3. Observe that the marker is encoded for the HTML context instead of embedded raw.

### Teaching point

The vulnerability is not that the model produced text. The vulnerability is that a downstream component trusted model-derived text and embedded it into an HTML context without context-aware output encoding.

### Graded artifact

Submit a short finding with evidence, sink context, failed security property, control, validation method, and residual risk.
'''

    if not text:
        write(path, section)
        return

    if "POST /render" not in text or "ENABLE_OUTPUT_ENCODING=false" not in text or "ENABLE_OUTPUT_ENCODING=true" not in text:
        write(path, text.rstrip() + "\n\n" + section)


def main() -> None:
    patch_evasion_alias()
    patch_output_handling_lab()
    print("Round 3 local repair patch applied.")


if __name__ == "__main__":
    main()
