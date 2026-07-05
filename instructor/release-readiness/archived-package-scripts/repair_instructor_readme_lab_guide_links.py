from pathlib import Path

path = Path("instructor/README.md")
text = path.read_text(encoding="utf-8")

required_block = """
## Lab facilitation entry points

Use exactly one instructor facilitation entry point per major lab family:

- Toy classifier, Modules 03 and 10: [`toy-classifier-guide.md`](toy-classifier-guide.md)
- BrokenPilot, Modules 05-07, 09, 11, and 12: [`brokenpilot-guide.md`](brokenpilot-guide.md)
- MLOps evidence pack, Module 08: [`mlops-evidence-pack-guide.md`](mlops-evidence-pack-guide.md)

Keep model answers, rubrics, and module-level instructor notes as references. The files above are the preparation entry points.
"""

missing = [
    name
    for name in [
        "toy-classifier-guide.md",
        "brokenpilot-guide.md",
        "mlops-evidence-pack-guide.md",
    ]
    if name not in text
]

if missing:
    if "## Lab facilitation entry points" in text:
        # Replace an incomplete section if it exists.
        before, _, rest = text.partition("## Lab facilitation entry points")
        next_heading = rest.find("\n## ", 1)
        if next_heading >= 0:
            text = before.rstrip() + "\n\n" + required_block.strip() + "\n" + rest[next_heading:]
        else:
            text = before.rstrip() + "\n\n" + required_block.strip() + "\n"
    else:
        text = text.rstrip() + "\n\n" + required_block.strip() + "\n"

    path.write_text(text, encoding="utf-8", newline="\n")
    print("patched instructor/README.md with explicit lab guide filenames")
else:
    print("instructor/README.md already contains required lab guide filenames")
