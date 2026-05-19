function Get-StatusGlyph {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet('success', 'warning', 'error', 'info')]
        [string]$Kind
    )

    $glyphs = @{
        success = [char]0x2705
        warning = [char]0x26A0 + [char]0xFE0F
        error   = [char]0x274C
        info    = [char]0x2139 + [char]0xFE0F
    }
    if ($glyphs.ContainsKey($Kind)) { return $glyphs[$Kind] }
    return '[?]'
}

function Get-RepoRoot {
    [CmdletBinding()]
    param()

    $dir = $PSScriptRoot
    while ($dir) {
        if (Test-Path (Join-Path $dir '.git')) {
            return (Resolve-Path $dir).Path
        }
        $parent = Split-Path $dir -Parent
        if (-not $parent -or $parent -eq $dir) { break }
        $dir = $parent
    }
    return (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
}

function Write-Diagnostic {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)][ValidateSet('Error', 'Warning', 'Info', 'Success')][string]$Level,
        [Parameter(Mandatory = $true)][string]$Message,
        [string]$Explanation,
        [string[]]$Solution,
        [string]$Help
    )

    $kind = switch ($Level) {
        'Error' { 'error' }
        'Warning' { 'warning' }
        'Success' { 'success' }
        default { 'info' }
    }
    $glyph = Get-StatusGlyph -Kind $kind
    $color = switch ($Level) {
        'Error' { 'Red' }
        'Warning' { 'Yellow' }
        'Success' { 'Green' }
        default { 'Cyan' }
    }

    Write-Host "$glyph ${Level}: $Message" -ForegroundColor $color
    if ($Explanation) { Write-Host "Explanation: $Explanation" -ForegroundColor DarkGray }
    if ($Solution) {
        Write-Host 'Solution:' -ForegroundColor Green
        $i = 1
        foreach ($step in $Solution) {
            Write-Host "  $i. $step" -ForegroundColor Green
            $i++
        }
    }
    if ($Help) { Write-Host "Help: $Help" -ForegroundColor Cyan }
    Write-Host ''
}

function Set-Utf8FileContent {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Content
    )
    $encoding = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($Path, $Content, $encoding)
}

Export-ModuleMember -Function Get-StatusGlyph, Get-RepoRoot, Write-Diagnostic, Set-Utf8FileContent
