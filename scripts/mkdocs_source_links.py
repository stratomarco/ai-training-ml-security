"""Map generated MkDocs pages back to their editable repository sources."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def on_files(files, **kwargs):
    for file in files:
        if not file.is_documentation_page():
            continue

        relative_path = Path(file.src_uri)
        for source_path in (relative_path, Path("docs") / relative_path):
            if (ROOT / source_path).is_file():
                file.edit_uri = source_path.as_posix()
                break
        else:
            raise FileNotFoundError(
                f"No editable repository source for generated page {file.src_uri}"
            )

    return files
