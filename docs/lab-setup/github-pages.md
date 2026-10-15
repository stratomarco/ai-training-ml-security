# GitHub Pages Deployment

The course website is built from the canonical root-level course content. A push to `main` runs the strict MkDocs build and deploys the generated `site/` directory through GitHub Actions. Maintainers can also start the workflow manually from `main`.

## One-time repository setting

In the GitHub repository, open **Settings > Pages** and select **GitHub Actions** under **Build and deployment > Source**. The [Deploy MkDocs site workflow](https://github.com/stratomarco/ai-training-ml-security/actions/workflows/deploy-docs.yml) uses the official Pages artifact and deployment actions. It does not push a `gh-pages` branch.

## Before publishing

Run the [final release gate](../COURSE_RELEASE_MANIFEST.md#release-status) from the repository root. It generates the MkDocs source, validates navigation, builds the site in strict mode, and runs the course lab checks.

After a reviewed change reaches `main`, check that the deployment workflow succeeds and open the published site. Verify the Start Here path, Module 08 labs, and BrokenPilot links in the live site. A successful build alone does not confirm that the site is reachable.

## Manual redeployment

If the source is already on `main` but the site needs to be republished, open the deployment workflow in GitHub Actions, select **Run workflow**, and choose `main`. No local `mkdocs gh-deploy` command is needed for this repository's publishing mode.
