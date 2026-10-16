param(
    [ValidateSet('start', 'stop', 'status')]
    [string]$Action = 'start',
    [string]$Distro = 'Ubuntu-22.04',
    [string]$WslSourcePath = '',
    [switch]$Rebuild
)

$ErrorActionPreference = 'Stop'
$expectedCommit = 'e1c538badb93c6c1c2307096ab5d709a9ee0fe55'
$repoRoot = Split-Path -Parent $PSScriptRoot
$composeFile = Join-Path $repoRoot 'labs/aigoat-guides/docker-compose.mcp.yml'
$configTemplate = Join-Path $repoRoot 'labs/aigoat-guides/config.mcp.example.yml'
$localDir = Join-Path $repoRoot '.local/aigoat-mcp'
$configFile = Join-Path $localDir 'config.yml'
$env:AIGOAT_CONFIG_PATH = $configFile

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw 'Docker Desktop CLI is required.'
}
& docker info --format '{{.ServerVersion}}' *> $null
if ($LASTEXITCODE -ne 0) { throw 'Start Docker Desktop and try again.' }

if ($Action -eq 'stop') {
    & docker compose -f $composeFile down
    if ($LASTEXITCODE -ne 0) { throw 'AIGoat stop failed.' }
    return
}
if ($Action -eq 'status') {
    & docker compose -f $composeFile ps
    if ($LASTEXITCODE -ne 0) { throw 'AIGoat status check failed.' }
    return
}

if (-not (Get-Command wsl -ErrorAction SilentlyContinue)) {
    throw 'WSL with an Ubuntu distribution is required on Windows.'
}
if (-not $WslSourcePath) {
    $wslHome = (& wsl -d $Distro -- printenv HOME | Select-Object -Last 1).Trim()
    if ($LASTEXITCODE -ne 0 -or -not $wslHome.StartsWith('/')) {
        throw 'Could not locate the WSL home directory.'
    }
    $WslSourcePath = "$wslHome/aigoat-course-v2.0"
    & wsl -d $Distro -- test -d "$WslSourcePath/.git" *> $null
    if ($LASTEXITCODE -ne 0) {
        & wsl -d $Distro -- git clone --branch v2.0 --depth 1 https://github.com/AISecurityConsortium/AIGoat.git $WslSourcePath
        if ($LASTEXITCODE -ne 0) { throw 'The pinned AIGoat checkout could not be cloned in WSL.' }
    }
}
$actualCommit = (& wsl -d $Distro --cd $WslSourcePath -- git rev-parse HEAD | Select-Object -Last 1).Trim()
if ($LASTEXITCODE -ne 0 -or $actualCommit -ne $expectedCommit) {
    throw "AIGoat source must be at commit $expectedCommit. Found: $actualCommit"
}

& docker image inspect 'aigoat-mcp-backend:v2.0' *> $null
$backendMissing = $LASTEXITCODE -ne 0
if ($Rebuild -or $backendMissing) {
    Write-Host 'Building the complete pinned backend from WSL. This can take time and substantial disk space.'
    $buildBackend = 'set -o pipefail; git archive --format=tar HEAD | docker.exe build --quiet -f docker/Dockerfile -t aigoat-mcp-backend:v2.0 -'
    & wsl -d $Distro --cd $WslSourcePath -- bash -lc $buildBackend
    if ($LASTEXITCODE -ne 0) { throw 'AIGoat backend build failed.' }
}
& docker image inspect 'aigoat-mcp-frontend:v2.0' *> $null
$frontendMissing = $LASTEXITCODE -ne 0
if ($Rebuild -or $frontendMissing) {
    Write-Host 'Building the pinned frontend from WSL.'
    $buildFrontend = 'set -o pipefail; git diff --quiet HEAD -- frontend && test $(git ls-files --others --exclude-standard frontend | wc -l) -eq 0 && tar -C frontend --exclude=node_modules --exclude=build -cf - . | docker.exe build --quiet -f Dockerfile -t aigoat-mcp-frontend:v2.0 -'
    & wsl -d $Distro --cd $WslSourcePath -- bash -lc $buildFrontend
    if ($LASTEXITCODE -ne 0) { throw 'AIGoat frontend build failed.' }
}

if (-not (Test-Path -LiteralPath $configFile)) {
    New-Item -ItemType Directory -Path $localDir -Force | Out-Null
    $bytes = New-Object byte[] 48
    $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
    try { $rng.GetBytes($bytes) } finally { $rng.Dispose() }
    $secret = [System.BitConverter]::ToString($bytes).Replace('-', '').ToLowerInvariant()
    $template = [System.IO.File]::ReadAllText($configTemplate)
    $config = $template.Replace('__GENERATED_SECRET__', $secret)
    [System.IO.File]::WriteAllText($configFile, $config, (New-Object System.Text.UTF8Encoding($false)))
}

& docker compose -f $composeFile config --quiet
if ($LASTEXITCODE -ne 0) { throw 'AIGoat course Compose configuration is invalid.' }
& docker compose -f $composeFile up -d --no-build
if ($LASTEXITCODE -ne 0) { throw 'AIGoat did not start. Run this script with -Action status and inspect Docker logs.' }
& docker compose -f $composeFile ps
Write-Host 'Open http://127.0.0.1:3000 for the two optional MCP exercises.'
Write-Host 'When finished, run this script with -Action stop. The local lab database is retained.'
