#!/usr/bin/env python3
"""Sync shared/ into each skill's _shared/, and check for drift.

Single runtime contract: every skill reads its own `_shared/` (generated).
The repo-root `shared/` is the only source of truth; `_shared/` is a build
artifact kept in sync by this script.

Usage:
  python3 sync-shared.py sync    # copy shared/** -> skills/<each>/_shared/**
  python3 sync-shared.py check   # verify each _shared/ matches shared/, report drift
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"


def skill_dirs() -> list[Path]:
    return [d for d in SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]


def shared_files() -> list[Path]:
    return sorted(p for p in SHARED.rglob("*") if p.is_file())


def file_hash(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sync() -> None:
    files = shared_files()
    if not files:
        print("shared/ has no files; nothing to sync")
        return
    for skill in skill_dirs():
        dest = skill / "_shared"
        if dest.exists():
            for f in dest.rglob("*"):
                if f.is_file():
                    f.unlink()
        dest.mkdir(exist_ok=True)
        for src in files:
            rel = src.relative_to(SHARED)
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(src.read_bytes())
        print(f"synced {skill.name}: {[str(p.relative_to(SHARED)) for p in files]}")


def check() -> int:
    files = shared_files()
    skills = skill_dirs()
    if not skills:
        print("no skill dirs with SKILL.md found")
        return 1
    drift: list[str] = []
    for skill in skills:
        dest = skill / "_shared"
        for src in files:
            rel = src.relative_to(SHARED)
            target = dest / rel
            if not target.exists():
                drift.append(f"{skill.name}: missing _shared/{rel}")
            elif file_hash(target) != file_hash(src):
                drift.append(f"{skill.name}: _shared/{rel} drifted from shared/{rel}")
        if dest.exists():
            for f in dest.rglob("*"):
                if f.is_file():
                    rel = f.relative_to(dest)
                    if not (SHARED / rel).exists():
                        drift.append(f"{skill.name}: extra _shared/{rel} not in shared/")
    if drift:
        print("DRIFT DETECTED:")
        for d in drift:
            print("  -", d)
        print("fix with: python3 scripts/sync-shared.py sync")
        return 1
    print(f"OK: all {len(skills)} skill(s) _shared/ match shared/ ({len(files)} file(s))")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "sync":
        sync()
    elif cmd == "check":
        sys.exit(check())
    else:
        print(f"unknown command: {cmd}; use sync|check")
        sys.exit(2)
