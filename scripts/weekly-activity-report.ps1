<#
.SYNOPSIS
    Generate a weekly repository health report for the GitHub organization.
#>
[CmdletBinding()]
param(
    [string]$Organization = $env:GITHUB_ORG,
    [int]$Days = 7,
    [string]$OutDir
)

$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'modules\Common.psm1') -Force
$RepoRoot = Get-RepoRoot
if (-not $Organization) { $Organization = 'AI-Whisperers' }
if (-not $OutDir) { $OutDir = Join-Path $RepoRoot 'logs' }

if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir -Force | Out-Null }

$since = (Get-Date).AddDays(-$Days).ToString('yyyy-MM-dd')
$reportPath = Join-Path $OutDir "weekly-health-$(Get-Date -Format 'yyyy-MM-dd').md"

$repoRows = @()
if (Get-Command gh -ErrorAction SilentlyContinue) {
    $reposJson = gh repo list $Organization --limit 200 --json name,updatedAt,pushedAt,isArchived,defaultBranchRef 2>&1
    if ($LASTEXITCODE -eq 0) {
        $repos = $reposJson | ConvertFrom-Json | Where-Object { -not $_.isArchived }
        foreach ($repo in $repos) {
            $commits = 0
            $commitJson = gh api "repos/$Organization/$($repo.name)/commits?since=${since}T00:00:00Z&per_page=1" --jq 'length' 2>$null
            if ($LASTEXITCODE -eq 0) { $commits = [int]$commitJson }

            $staleDays = ((Get-Date) - [datetime]$repo.pushedAt).TotalDays
            $health = if ($staleDays -gt 90) { 'At risk' } elseif ($staleDays -gt 30) { 'Watch' } else { 'Healthy' }

            $repoRows += [pscustomobject]@{
                Name    = $repo.name
                Pushed  = $repo.pushedAt
                Commits = $commits
                Health  = $health
            }
        }
    }
}

$md = @(
    '# Weekly repository health',
    '',
    "- Organization: **$Organization**",
    "- Window: last **$Days** days (since $since)",
    "- Generated: $(Get-Date -Format 'u')",
    '',
    '## Summary',
    '',
    "| Repository | Last push | Commits (window) | Health |",
    "| --- | --- | ---: | --- |"
)

if ($repoRows.Count -eq 0) {
    $md += '| _No data - install/authenticate gh or check organization name._ | | | |'
}
else {
    foreach ($row in ($repoRows | Sort-Object Pushed)) {
        $md += "| $($row.Name) | $($row.Pushed) | $($row.Commits) | $($row.Health) |"
    }
    $atRisk = @($repoRows | Where-Object Health -eq 'At risk').Count
    $md += @('', "## Recommendations", '', "- Repositories at risk (90+ days idle): **$atRisk**")
    if ($atRisk -gt 0) {
        $md += '- Schedule ownership review for stale repos'
        $md += '- Archive or document repos with no active maintainer'
    }
}

Set-Utf8FileContent -Path $reportPath -Content ($md -join "`n")
Write-Host "$(Get-StatusGlyph -Kind success) Report: $reportPath" -ForegroundColor Green
