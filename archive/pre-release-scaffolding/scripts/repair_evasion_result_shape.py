from pathlib import Path
import re

path = Path("labs/toy-ml-attacks/toy-classifier-app/attacks/evasion.py")
text = path.read_text(encoding="utf-8")

replacement = r'''
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
'''

# Remove any previous run_evasion definition.
text = re.sub(
    r'\n\ndef run_evasion\(\):.*?(?=\n\nif __name__ == "__main__":|\Z)',
    "\n\n" + replacement.strip(),
    text,
    flags=re.S,
)

# If there was no run_evasion function, insert it before the main guard.
if "def run_evasion():" not in text:
    marker = '\n\nif __name__ == "__main__":'
    if marker in text:
        text = text.replace(marker, "\n\n" + replacement.strip() + marker)
    else:
        text = text.rstrip() + "\n\n" + replacement.strip() + "\n"

path.write_text(text, encoding="utf-8", newline="\n")
print("patched evasion.py run_evasion compatibility wrapper")
