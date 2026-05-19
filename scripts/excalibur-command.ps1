<#
.SYNOPSIS
    Sync organization todos from GitHub into project-todos/*.md files.

.PARAMETER DryRun
    Report planned changes without writing files.

.PARAMETER Organization
    GitHub organization slug (default: $env:GITHUB_ORG or AI-Whisperers).
#>
[CmdletBinding()]
param(
    [switch]$DryRun,
    [string]$Organization = $env:GITHUB_ORG
)

$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'modules\Common.psm1') -Force
$RepoRoot = Get-RepoRoot
if (-not $Organization) { $Organization = 'AI-Whisperers' }

function Test-GhCli {
    if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
        Write-Diagnostic -Level Error -Message 'GitHub CLI (gh) is not installed' `
            -Explanation 'Excalibur sync requires gh to list issues and repositories.' `
            -Solution @('Install: https://cli.github.com/', 'Run: gh auth login') `
            -Help '.claude/commands/excalibur-sync.md'
        exit 1
    }
    gh auth status 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Diagnostic -Level Error -Message 'GitHub CLI is not authenticated' `
            -Explanation 'gh auth status failed; API calls will not work.' `
            -Solution @('Run: gh auth login') `
            -Help '.claude/commands/excalibur-sync.md'
        exit 1
    }
}

Test-GhCli

$todosDir = Join-Path $RepoRoot 'project-todos'
if (-not (Test-Path $todosDir)) {
    New-Item -ItemType Directory -Path $todosDir -Force | Out-Null
}

Write-Host "$(Get-StatusGlyph -Kind info) Excalibur sync - organization: $Organization" -ForegroundColor Cyan
if ($DryRun) { Write-Host 'Mode: DryRun (no files will be modified)' -ForegroundColor Yellow }

$reposJson = gh repo list $Organization --limit 200 --json name,url,isArchived,updatedAt 2>&1
if ($LASTEXITCODE -ne 0) { throw "gh repo list failed: $reposJson" }
$repos = $reposJson | ConvertFrom-Json | Where-Object { -not $_.isArchived }

$summaryPath = Join-Path $RepoRoot "logs\excalibur-sync-$(Get-Date -Format 'yyyy-MM-dd-HHmm').md"
$logDir = Split-Path $summaryPath -Parent
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

$lines = @(
    "# Excalibur sync summary",
    "",
    "- Organization: **$Organization**",
    "- Repositories scanned: **$($repos.Count)**",
    "- Mode: **$(if ($DryRun) { 'DryRun' } else { 'Apply' })**",
    "- Generated: $(Get-Date -Format 'u')",
    "",
    "## Repositories",
    ""
)

foreach ($repo in $repos) {
    $issuesJson = gh issue list --repo "$Organization/$($repo.name)" --state open --limit 50 --json number,title,labels,updatedAt 2>&1
    $issueCount = 0
    if ($LASTEXITCODE -eq 0) {
        $issues = $issuesJson | ConvertFrom-Json
        $issueCount = @($issues).Count
    }

    $todoFile = Join-Path $todosDir "$($repo.name).md"
    $content = @(
        "# $($repo.name) - open work",
        "",
        "Source: [$($repo.url)]($($repo.url))",
        "Last repo activity: $($repo.updatedAt)",
        "",
        "## Open issues ($issueCount)",
        ""
    )

    if ($issueCount -gt 0) {
        foreach ($issue in $issues) {
            $labelNames = ($issue.labels | ForEach-Object { $_.name }) -join ', '
            $content += "- [ ] #$($issue.number) $($issue.title) $(if ($labelNames) { "[$labelNames]" })"
        }
    }
    else {
        $content += '_No open issues or issue fetch skipped._'
    }
    $content += ''

    $lines += "- **$($repo.name)** - $issueCount open issue(s)"

    if ($DryRun) {
        Write-Verbose "Would write: $todoFile ($issueCount issues)"
    }
    else {
        Set-Utf8FileContent -Path $todoFile -Content ($content -join "`n")
        Write-Verbose "Wrote $todoFile"
    }
}

$lines += @('', '## Next steps', '', '- Review `project-todos/*.md`', '- Remove `-DryRun` to apply writes', '')
$report = $lines -join "`n"

if ($DryRun) {
    Write-Host $report
}
else {
    Set-Utf8FileContent -Path $summaryPath -Content $report
    Write-Host "$(Get-StatusGlyph -Kind success) Wrote summary: $summaryPath" -ForegroundColor Green
}

exit 0
