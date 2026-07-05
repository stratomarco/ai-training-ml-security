"""Fail if Markdown or MkDocs config files contain em dashes.

The course style guide avoids em dashes because they are distracting for
some readers and can read as generated prose. Use a comma, colon,
semicolon, parentheses, or a rewritten sentence instead.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "site", ".mkdocs-src", "__pycache__"}
EXTENSIONS = {".md", ".yml", ".yaml"}

failures = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix not in EXTENSIONS:
        continue
    if any(part in SKIP_PARTS for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "\u2014" in text:
        for idx, line in enumerate(text.splitlines(), start=1):
            if "\u2014" in line:
                failures.append(f"{path}:{idx}: {line.strip()}")

if failures:
    print("Em dash check failed. Replace em dashes with punctuation or rewritten prose.\n")
    print("\n".join(failures[:200]))
    if len(failures) > 200:
        print(f"... and {len(failures) - 200} more")
    sys.exit(1)

print("No em dashes found.")
