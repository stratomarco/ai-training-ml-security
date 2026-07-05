# Local Website Preview

This site is built with MkDocs Material.

Canonical course content lives in the root-level content directories. Before running MkDocs, generate `.mkdocs-src/` with the sync script.

## Windows PowerShell

```powershell
cd F:\ai-training-ml-security
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\sync_mkdocs_content.py
mkdocs serve
```

## macOS or Linux

```bash
cd ~/ai-training-ml-security
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/sync_mkdocs_content.py
mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

## Build static site

Windows PowerShell:

```powershell
python scripts\sync_mkdocs_content.py
mkdocs build
```

macOS or Linux:

```bash
python3 scripts/sync_mkdocs_content.py
mkdocs build
```

The generated website is written to the `site/` directory.

## Cleanup generated files

Windows PowerShell:

```powershell
.\scripts\cleanup_duplicate_content.ps1
```

macOS or Linux:

```bash
./scripts/cleanup_duplicate_content.sh
```

## Deploy manually

```powershell
mkdocs gh-deploy --force
```

The recommended hosted deployment for this repository is GitHub Pages via GitHub Actions. See [GitHub Pages Deployment](github-pages.md).
