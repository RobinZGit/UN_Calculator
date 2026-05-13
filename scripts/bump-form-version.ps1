# Increments vN in every <span class="form-version"> inside index.html (h1 and fieldset legend).
# Called from .githooks/pre-commit when index.html is part of the commit.
$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$htmlPath = Join-Path $repoRoot "index.html"
if (-not (Test-Path -LiteralPath $htmlPath)) {
    Write-Error "index.html not found at $htmlPath"
    exit 1
}
$utf8 = New-Object System.Text.UTF8Encoding $false
$raw = [System.IO.File]::ReadAllText($htmlPath, $utf8)
# ASCII-only pattern so the script parses under any OEM code page
$pattern = 'class="form-version">v(\d+)'
$m = [regex]::Match($raw, $pattern)
if (-not $m.Success) {
    Write-Error 'Expected class="form-version">vN in index.html'
    exit 1
}
$next = [int]$m.Groups[1].Value + 1
$newText = [regex]::Replace($raw, '(class="form-version">)v\d+', {
        param($match)
        $match.Groups[1].Value + "v$next"
    })
[System.IO.File]::WriteAllText($htmlPath, $newText, $utf8)
Write-Host "Form version bumped to v$next (all spans)"
