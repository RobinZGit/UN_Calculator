#!/bin/sh
# Один раз в клоне: подключает хуки из .githooks
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
git config core.hooksPath .githooks
echo "OK: core.hooksPath = .githooks"
