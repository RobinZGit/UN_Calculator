# Один раз в клоне: подключает хуки из .githooks (увеличение версии перед каждым коммитом).
$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $root
git config core.hooksPath .githooks
Write-Host "OK: core.hooksPath = .githooks (относительно корня репозитория)"
