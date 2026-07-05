# Removes stale generated or accidentally nested copies before committing.
# Run from the repository root:
#   .\scripts\cleanup_duplicate_content.ps1

$ErrorActionPreference = "Stop"

$paths = @(
  "ai-training-ml-security",
  "docs\modules",
  "docs\labs",
  "docs\templates",
  "docs\instructor",
  "docs\assessments",
  ".mkdocs-src",
  "site"
)

foreach ($path in $paths) {
  if (Test-Path $path) {
    Write-Host "Removing $path"
    Remove-Item $path -Recurse -Force
  }
}

Write-Host "Cleanup complete. Run: python scripts\sync_mkdocs_content.py"
