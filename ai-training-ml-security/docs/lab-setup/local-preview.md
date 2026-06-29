# Local Website Preview

This site is built with MkDocs Material.

## Windows PowerShell

```powershell
cd F:\ai-training-ml-security
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

## Build static site

```powershell
mkdocs build
```

The generated website is written to the `site/` directory.

## Deploy manually

```powershell
mkdocs gh-deploy --force
```

The recommended hosted deployment for this repository is GitHub Pages via GitHub Actions. See [GitHub Pages Deployment](github-pages.md).
