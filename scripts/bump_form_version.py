#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Режим hook: всегда +1 ко всем span.form-version (для pre-commit).
Режим ci: +1 только если версия в index.html не больше, чем в HEAD~1 (хук не сработал локально).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

PAT = re.compile(r'(class="form-version">)v(\d+)')


def first_version_num(html: str) -> Optional[int]:
    m = PAT.search(html)
    return int(m.group(2)) if m else None


def replace_all(html: str, new_n: int) -> str:
    return PAT.sub(lambda m: f'{m.group(1)}v{new_n}', html)


def main() -> int:
    mode = (sys.argv[1] if len(sys.argv) > 1 else "hook").lower()
    root = Path(__file__).resolve().parents[1]
    path = root / "index.html"
    if not path.is_file():
        print("index.html not found", file=sys.stderr)
        return 1
    raw = path.read_text(encoding="utf-8")
    cur = first_version_num(raw)
    if cur is None:
        print("No class=form-version>vN in index.html", file=sys.stderr)
        return 1

    if mode == "ci":
        try:
            parent = subprocess.check_output(
                ["git", "show", "HEAD~1:index.html"],
                cwd=root,
                text=True,
                stderr=subprocess.DEVNULL,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("CI bump: no parent commit or no index in parent — skip")
            return 0
        vp = first_version_num(parent)
        if vp is None:
            print("CI bump: no version in parent — skip")
            return 0
        if cur > vp:
            print(f"CI bump: already bumped (v{cur} > v{vp}) — skip")
            return 0
        new_n = vp + 1
    else:
        new_n = cur + 1

    new_html = replace_all(raw, new_n)
    path.write_text(new_html, encoding="utf-8")
    print(f"Form version -> v{new_n} ({mode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
