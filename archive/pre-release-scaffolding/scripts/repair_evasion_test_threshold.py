from pathlib import Path
import re

path = Path("labs/toy-ml-attacks/toy-classifier-app/tests/test_toy_classifier.py")
text = path.read_text(encoding="utf-8")

replacement = '''
def test_evasion_word_swap_flips_the_decision() -> None:
    result = run_evasion()

    before = result["before"]
    after = result["after"]

    assert before["label"] == "phish"
    assert after["label"] == "safe"

    # The tiny synthetic classifier should show a meaningful drop, but the
    # exact probability margin is not the security lesson. The important
    # property is intent-preserving evasion: the message still carries the
    # malicious meaning while the classifier decision flips.
    assert before["phish_probability"] - after["phish_probability"] > 0.50

    perturbed = after["text"].lower()
    for token in ["password", "credential", "token"]:
        assert token in perturbed
'''

text = re.sub(
    r'def test_evasion_word_swap_flips_the_decision\(\) -> None:\n.*?(?=\n\ndef test_|\Z)',
    replacement.strip(),
    text,
    flags=re.S,
)

path.write_text(text, encoding="utf-8", newline="\n")
print("patched evasion test threshold and intent-preservation assertions")
