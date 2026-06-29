# Website Source

This `docs/` directory is the source for the MkDocs website.

The website is built with MkDocs Material and can be previewed locally with:

```bash
mkdocs serve
```

See:

- [Local Website Preview](lab-setup/local-preview.md)
- [GitHub Pages Deployment](lab-setup/github-pages.md)

## Source of truth note

For v1.1, the curriculum is mirrored into `docs/` so it can be published as a MkDocs site while preserving the v1.0 root-level folder structure.

Long-term, the project should choose one source-of-truth model:

1. Keep `docs/` as the canonical course source and remove duplicated root-level curriculum folders in a future release, or
2. Maintain a small sync workflow that copies root-level curriculum files into `docs/` before publishing.
