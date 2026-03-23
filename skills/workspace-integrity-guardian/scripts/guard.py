#!/usr/bin/env python3
"""Workspace integrity guardian — hash critical files and detect drift."""

import hashlib
import json
import os
import sys
from pathlib import Path

PROTECTED_FILES = ["SOUL.md", "AGENTS.md", "IDENTITY.md", "MEMORY.md"]
STATE_DIR = Path.home() / ".openclaw" / "skill-state" / "workspace-integrity-guardian"
BASELINE_FILE = STATE_DIR / "baseline.json"


def hash_file(filepath: Path) -> str | None:
    if not filepath.exists():
        return None
    h = hashlib.sha256()
    h.update(filepath.read_bytes())
    return h.hexdigest()


def cmd_baseline(workspace: Path):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for name in PROTECTED_FILES:
        fp = workspace / name
        digest = hash_file(fp)
        if digest:
            hashes[name] = digest
            print(f"  {name}: {digest[:16]}...")
        else:
            print(f"  {name}: not found (skipped)")
    BASELINE_FILE.write_text(json.dumps(hashes, indent=2) + "\n")
    print(f"\nBaseline saved to {BASELINE_FILE}")


def cmd_check(workspace: Path):
    if not BASELINE_FILE.exists():
        print("NEW — no baseline exists. Run 'baseline' first.")
        sys.exit(2)

    baseline = json.loads(BASELINE_FILE.read_text())
    issues = []

    for name in PROTECTED_FILES:
        fp = workspace / name
        current = hash_file(fp)
        expected = baseline.get(name)

        if expected and current is None:
            issues.append(f"MISSING: {name} — was in baseline but no longer exists")
        elif expected and current != expected:
            issues.append(f"MODIFIED: {name} — hash mismatch")
        elif not expected and current:
            issues.append(f"NEW FILE: {name} — exists but wasn't in baseline")

    if not issues:
        print("OK — all protected files match baseline.")
        sys.exit(0)
    else:
        for issue in issues:
            print(f"  ⚠ {issue}")
        print(f"\n{len(issues)} issue(s) detected.")
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <baseline|check> <workspace_path>")
        sys.exit(1)

    command = sys.argv[1]
    workspace = Path(sys.argv[2])

    if not workspace.is_dir():
        print(f"Error: {workspace} is not a directory")
        sys.exit(1)

    if command == "baseline":
        cmd_baseline(workspace)
    elif command == "check":
        cmd_check(workspace)
    else:
        print(f"Unknown command: {command}. Use 'baseline' or 'check'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
