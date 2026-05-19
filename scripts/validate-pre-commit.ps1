<#
.SYNOPSIS
    Pre-commit validation for the Marketing repository.

.PARAMETER AutoFix
    Attempt automatic fixes where supported.

.PARAMETER Strict
    Run full .cursor rule and YAML validation (may fail on known index drift).

.PARAMETER Report
    Emit detailed report paths only.
#>
[CmdletBinding()]
param(
    [switch]$AutoFix,
    [switch]$Strict,
    [switch]$Report
)

$ErrorActionPreference = 'Stop'
$ModulePath = Join-Path $PSScriptRoot 'modules\Common.psm1'
Import-Module $ModulePath -Force
$RepoRoot = Get-RepoRoot
Set-Location $RepoRoot

$errors = @()
$warnings = @()

function Invoke-Step {
    param(
        [string]$Name,
        [scriptblock]$Action,
        [switch]$Optional
    )
    Write-Host " * $Name..." -NoNewline
    try {
        & $Action
        if ($null -ne $LASTEXITCODE -and $LASTEXITCODE -ne 0) {
            throw "Step exited with code $LASTEXITCODE"
        }
        Write-Host ' OK' -ForegroundColor Green
    }
    catch {
        Write-Host ' FAIL' -ForegroundColor Red
        if ($Optional) {
            $script:warnings += "${Name}: $($_.Exception.Message)"
            Write-Host "   (optional) $($_.Exception.Message)" -ForegroundColor Yellow
        }
        else {
            $script:errors += $Name
            Write-Diagnostic -Level Error -Message "$Name failed" `
                -Explanation $_.Exception.Message `
                -Solution @('Review the command output above', 'Re-run: .\scripts\validate-pre-commit.ps1') `
                -Help '.cursor/rules/quality/zero-warnings-zero-errors-rule.mdc'
        }
    }
}

Write-Host 'Running pre-commit validation...' -ForegroundColor Cyan

Invoke-Step -Name 'Documentation coverage' -Action {
    $audit = Join-Path $RepoRoot 'mcp-servers\doc-coverage-audit.js'
    if (-not (Test-Path $audit)) { throw "Missing $audit" }
    node $audit --root $RepoRoot
}

Invoke-Step -Name 'Ops scripts parse check' -Action {
    $scripts = Get-ChildItem -Path (Join-Path $RepoRoot 'scripts') -Filter '*.ps1' -File
    foreach ($script in $scripts) {
        $parseErrors = $null
        $tokens = $null
        $null = [System.Management.Automation.Language.Parser]::ParseFile(
            $script.FullName,
            [ref]$tokens,
            [ref]$parseErrors
        )
        if ($parseErrors -and $parseErrors.Count -gt 0) {
            throw "$($script.Name): $($parseErrors[0].Message)"
        }
    }
}

if ($Strict) {
    Invoke-Step -Name 'Cursor rules' -Action {
        $rulesScript = Join-Path $RepoRoot '.cursor\scripts\validate-rules.ps1'
        if (-not (Test-Path $rulesScript)) { throw "Missing $rulesScript" }
        & $rulesScript -RulesDir (Join-Path $RepoRoot '.cursor\rules') -IndexFile (Join-Path $RepoRoot '.cursor\rules\rule-index.yml')
    }

    $ps7 = Get-Command pwsh -ErrorAction SilentlyContinue
    if (-not $ps7) {
        $candidate = Join-Path ${env:ProgramFiles} 'PowerShell\7\pwsh.exe'
        if (Test-Path $candidate) { $ps7 = @{ Source = $candidate } }
    }

    if ($ps7) {
        Invoke-Step -Name 'YAML collections' -Action {
            $yamlScript = Join-Path $RepoRoot '.cursor\scripts\validate-yaml.ps1'
            & $ps7.Source -NoProfile -File $yamlScript
        }
    }
    else {
        $warnings += 'Skipped YAML validation (PowerShell 7 not found). Install PS7 or run validate-yaml.ps1 manually.'
    }
}
else {
    $warnings += 'Skipped full .cursor rule/YAML validation (use -Strict when editing rules or prompts).'
}

$sln = Get-ChildItem -Path $RepoRoot -Filter '*.sln' -File -ErrorAction SilentlyContinue | Select-Object -First 1
if ($sln) {
    Invoke-Step -Name '.NET pre-merge' -Action {
        $preMerge = Join-Path $RepoRoot '.cursor\scripts\quality\validate-pre-merge.ps1'
        if (-not (Test-Path $preMerge)) { throw "Missing $preMerge" }
        $mergeArgs = @{ TargetPath = $RepoRoot; SkipAutoFix = (-not $AutoFix) }
        & $preMerge @mergeArgs
    } -Optional
}

if ($errors.Count -gt 0) {
    Write-Host ''
    Write-Host 'ERRORS FOUND:' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " * $_" -ForegroundColor Red }
    exit 1
}

if ($warnings.Count -gt 0 -and -not $Report) {
    Write-Host ''
    Write-Host 'WARNINGS:' -ForegroundColor Yellow
    $warnings | ForEach-Object { Write-Host " * $_" -ForegroundColor Yellow }
}

Write-Host ''
Write-Host 'All validation checks passed.' -ForegroundColor Green
exit 0
