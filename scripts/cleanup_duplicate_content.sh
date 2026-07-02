#!/usr/bin/env bash
set -euo pipefail

rm -rf \
  ai-training-ml-security \
  docs/modules \
  docs/labs \
  docs/templates \
  docs/instructor \
  docs/assessments \
  .mkdocs-src \
  site

echo "Cleanup complete. Run: python3 scripts/sync_mkdocs_content.py"
