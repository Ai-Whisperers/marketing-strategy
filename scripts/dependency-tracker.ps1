<#
.SYNOPSIS
    Inventory dependency manifests under the Marketing workspace and sibling repos.

.PARAMETER All
    Include sibling directories under 02-Work when scanning.

.PARAMETER Out
    Output directory for JSON reports.
#>
[CmdletBinding()]
param(
    [switch]$All,
    [string]$Out = (Join-Path $PSScriptRoot 'dependency-reports')
)

$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'modules\Common.psm1') -Force
$RepoRoot = Get-RepoRoot

if (-not (Test-Path $Out)) { New-Item -ItemType Directory -Path $Out -Force | Out-Null }

$manifestNames = @(
    'package.json',
    'package-lock.json',
    'pnpm-lock.yaml',
    'yarn.lock',
    'requirements.txt',
    'Pipfile',
    'poetry.lock',
    'go.mod',
    'Cargo.toml',
    '*.csproj',
    'Directory.Packages.props'
)

$roots = @($RepoRoot)
if ($All) {
    $workRoot = (Resolve-Path (Join-Path $RepoRoot '..')).Path
    $roots += Get-ChildItem -Path $workRoot -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -ne 'Marketing' } |
        ForEach-Object { $_.FullName }
}

$findings = @()
foreach ($root in $roots) {
    if (-not (Test-Path $root)) { continue }
    foreach ($pattern in $manifestNames) {
        Get-ChildItem -Path $root -Filter $pattern -Recurse -File -ErrorAction SilentlyContinue |
            Where-Object {
                $rel = $_.FullName.Substring($root.Length)
                $rel -notmatch '[\\/]node_modules[\\/]' -and
                $rel -notmatch '[\\/]\.git[\\/]' -and
                $rel -notmatch '[\\/]enhanced-documentation[\\/]'
            } |
            ForEach-Object {
                $findings += [pscustomobject]@{
                    Root     = $root
                    Relative = $_.FullName.Substring($root.Length).TrimStart('\', '/')
                    Type     = $_.Name
                    Modified = $_.LastWriteTimeUtc.ToString('o')
                }
            }
    }
}

$stamp = Get-Date -Format 'yyyy-MM-dd-HHmm'
$outFile = Join-Path $Out "dependency-inventory-$stamp.json"
$findings | ConvertTo-Json -Depth 4 | Set-Content -Path $outFile -Encoding utf8

Write-Host "$(Get-StatusGlyph -Kind success) Found $($findings.Count) manifest(s)" -ForegroundColor Green
Write-Host "Report: $outFile" -ForegroundColor Cyan

# Summary by type
$findings | Group-Object Type | Sort-Object Count -Descending | ForEach-Object {
    Write-Host "  $($_.Name): $($_.Count)"
}
