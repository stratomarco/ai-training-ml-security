# GitHub Pages Deployment

This repository includes a GitHub Actions workflow that builds the MkDocs site and deploys it to GitHub Pages.

## One-time GitHub setting

In the GitHub repository:

1. Go to **Settings**.
2. Go to **Pages**.
3. Under **Build and deployment**, choose **Source: GitHub Actions**.

After that, every push to `main` that changes `docs/**`, `mkdocs.yml`, `requirements.txt`, or the deploy workflow will rebuild the website.

## Local build check

Before pushing major changes, run:

```powershell
mkdocs build --strict
```

If the build succeeds locally, push the changes:

```powershell
git add .
git commit -m "Update website content"
git push
```

## Release flow

For major content releases:

1. Update the content.
2. Run `mkdocs build --strict`.
3. Commit and push.
4. Verify the GitHub Actions deployment.
5. Create a GitHub release tag if needed.
