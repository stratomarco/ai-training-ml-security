# GitHub Pages Deployment

This repository includes a GitHub Actions workflow that builds the MkDocs site and deploys it to GitHub Pages.

## One-time GitHub setting

In the GitHub repository:

1. Go to **Settings**.
2. Go to **Pages**.
3. Under **Build and deployment**, choose **Source: GitHub Actions**.

After that, every push to `main` or the active development branch that changes course content, MkDocs configuration, requirements, scripts, or the deployment workflow can rebuild the website.

## How the workflow builds the site

The workflow does not depend on hand-maintained copies under `docs/modules` or `docs/labs`.

It runs:

```bash
python scripts/sync_mkdocs_content.py
python scripts/check_repo_structure.py
python scripts/check_no_em_dash.py
mkdocs build
```

The sync step generates `.mkdocs-src/` from the canonical root-level content directories.

## Local build check

Windows PowerShell:

```powershell
python scripts\sync_mkdocs_content.py
python scripts\check_repo_structure.py
python scripts\check_no_em_dash.py
mkdocs build
```

macOS or Linux:

```bash
python3 scripts/sync_mkdocs_content.py
python3 scripts/check_repo_structure.py
python3 scripts/check_no_em_dash.py
mkdocs build
```

If the build succeeds locally, push the changes:

```powershell
git add .
git commit -m "Update website content"
git push
```

## Release flow

For major content releases:

1. Update the canonical content in the root-level course directories.
2. Run the sync and checks locally.
3. Commit and push.
4. Verify the GitHub Actions deployment.
5. Create a GitHub release tag only when the development line is reviewed and ready.
