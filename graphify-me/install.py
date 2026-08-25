#!/usr/bin/env python3
"""Repo-root installer: skill links + optional Graphify CLI."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = ROOT / "graphify-me"
SCRIPTS = SKILL / "scripts"


def run_script(name: str, extra: list[str]) -> int:
    script = SCRIPTS / name
    return subprocess.call([sys.executable, str(script), *extra])


def main() -> int:
    parser = argparse.ArgumentParser(description="Install graphify-me skill (+ optional CLI)")
    parser.add_argument("--with-cli", action="store_true", help="Also run install_cli.py")
    parser.add_argument("--all-agents", action="store_true", help="Link into every known agent dir")
    parser.add_argument("--agents", nargs="*", default=None, help="Subset of agent ids")
    args = parser.parse_args()

    if not (SKILL / "SKILL.md").is_file():
        print(f"SKILL.md missing under {SKILL}", file=sys.stderr)
        return 1

    skill_args: list[str] = ["--force"]
    if args.all_agents:
        skill_args.append("--all")
    elif args.agents:
        skill_args.extend(["--agents", *args.agents])

    code = run_script("install_skill.py", skill_args)
    if code != 0:
        return code
    if args.with_cli:
        return run_script("install_cli.py", [])
    return 0


if __name__ == "__main__":
    sys.exit(main())
