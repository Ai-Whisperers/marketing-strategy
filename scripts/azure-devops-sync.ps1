<#
.SYNOPSIS
    Plan or apply sync between GitHub issues and Azure DevOps work items.

.PARAMETER DryRun
    Emit a sync plan only (default safe mode).

.PARAMETER Organization
    Azure DevOps organization (env: AZURE_DEVOPS_ORG).

.PARAMETER Project
    Azure DevOps project (env: AZURE_DEVOPS_PROJECT).
#>
[CmdletBinding()]
param(
    [switch]$DryRun,
    [string]$Organization = $env:AZURE_DEVOPS_ORG,
    [string]$Project = $env:AZURE_DEVOPS_PROJECT
)

$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'modules\Common.psm1') -Force
$RepoRoot = Get-RepoRoot
$logDir = Join-Path $RepoRoot 'logs'
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

$planPath = Join-Path $logDir ('ado-sync-plan-' + (Get-Date -Format 'yyyy-MM-dd-HHmm') + '.md')
$nl = [Environment]::NewLine

$missing = @()
if (-not $Organization) { $missing += 'AZURE_DEVOPS_ORG' }
if (-not $Project) { $missing += 'AZURE_DEVOPS_PROJECT' }
if (-not $env:AZURE_DEVOPS_PAT -and -not $env:SYSTEM_ACCESSTOKEN) { $missing += 'AZURE_DEVOPS_PAT or SYSTEM_ACCESSTOKEN' }

$ghReady = $false
if (Get-Command gh -ErrorAction SilentlyContinue) {
    gh auth status 2>&1 | Out-Null
    $ghReady = ($LASTEXITCODE -eq 0)
}

$mode = if ($DryRun) { 'DryRun' } else { 'Apply' }
$orgLabel = if ($Organization) { $Organization } else { '_unset_' }
$projLabel = if ($Project) { $Project } else { '_unset_' }
$ghLabel = if ($ghReady) { 'ready' } else { 'not ready' }

$lines = @(
    '# Azure DevOps - GitHub sync plan',
    '',
    "- Mode: **$mode**",
    "- ADO org/project: **$orgLabel** / **$projLabel**",
    "- GitHub CLI: **$ghLabel**",
    "- Generated: $(Get-Date -Format 'u')",
    ''
)

if ($missing.Count -gt 0) {
    $lines += '## Blockers', '', 'The following configuration is required before apply mode:', ''
    foreach ($m in $missing) {
        $lines += "- Environment variable: $m"
    }
    $lines += @(
        '',
        '## Planned actions (when configured)',
        '',
        '1. List open GitHub issues labeled for ADO sync',
        '2. Map to ADO work item types (User Story / Task)',
        '3. Create or update work items; link URLs bidirectionally',
        '4. Write reconciliation log under logs/',
        ''
    )

    Set-Utf8FileContent -Path $planPath -Content ($lines -join $nl)
    Write-Diagnostic -Level Warning -Message 'ADO sync is not fully configured' `
        -Explanation 'Dry-run plan was written; apply mode needs Azure DevOps credentials.' `
        -Solution @(
            'Set AZURE_DEVOPS_ORG, AZURE_DEVOPS_PROJECT, and AZURE_DEVOPS_PAT',
            'Re-run with -DryRun to validate plan',
            'Use apply only after reviewing the plan file'
        ) -Help '.claude/commands/ado-sync.md'
    Write-Host "Plan: $planPath" -ForegroundColor Cyan
    exit 0
}

if ($DryRun) {
    $lines += @('## Dry run', '', '_Configuration present; implement REST sync in a future iteration._', '')
    Set-Utf8FileContent -Path $planPath -Content ($lines -join $nl)
    Write-Host "$(Get-StatusGlyph -Kind info) Plan written: $planPath" -ForegroundColor Cyan
    exit 0
}

Write-Diagnostic -Level Error -Message 'Apply mode for ADO sync is not implemented' `
    -Explanation 'Credentials are set but automated apply is not yet wired.' `
    -Solution @('Use -DryRun to generate plans', 'Track work items manually until apply is implemented') `
    -Help '.claude/commands/ado-sync.md'
exit 1
