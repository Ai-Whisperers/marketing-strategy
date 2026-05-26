<#
.SYNOPSIS
    Manage project-todos snapshots across the Marketing workspace.

.PARAMETER Command
    status | sync | list
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet('status', 'sync', 'list')]
    [string]$Command = 'status'
)

$ErrorActionPreference = 'Stop'
Import-Module (Join-Path $PSScriptRoot 'modules\Common.psm1') -Force
$RepoRoot = Get-RepoRoot
$todosDir = Join-Path $RepoRoot 'project-todos'

switch ($Command) {
    'status' {
        if (-not (Test-Path $todosDir)) {
            Write-Host "$(Get-StatusGlyph -Kind warning) No project-todos directory. Run excalibur sync first." -ForegroundColor Yellow
            exit 0
        }
        $files = Get-ChildItem -Path $todosDir -Filter '*.md' -File
        $totalOpen = 0
        Write-Host 'Todo status (project-todos)' -ForegroundColor Cyan
        foreach ($file in $files | Sort-Object Name) {
            $open = (Select-String -Path $file.FullName -Pattern '^\s*-\s*\[\s\]' -AllMatches).Matches.Count
            $totalOpen += $open
            Write-Host "  $($file.BaseName): $open open item(s)"
        }
        Write-Host "`nTotal: $($files.Count) repo file(s), $totalOpen open checkbox(es)" -ForegroundColor Green
    }
    'list' {
        if (-not (Test-Path $todosDir)) { exit 0 }
        Get-ChildItem -Path $todosDir -Filter '*.md' | ForEach-Object { $_.Name }
    }
    'sync' {
        $excalibur = Join-Path $PSScriptRoot 'excalibur-command.ps1'
        if (-not (Test-Path $excalibur)) { throw "Missing $excalibur" }
        $invoke = @{ Verbose = $VerbosePreference -eq 'Continue' }
        & $excalibur @invoke
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }
}

exit 0
