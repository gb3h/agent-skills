---
name: config-edit-guard
description: >-
  Validate configuration files before restarting services. Use when: editing openclaw.json,
  modifying any JSON/YAML config that a service reads on startup, restarting a gateway or
  daemon after config changes, or any situation where a bad config could take a service offline
  with no way to self-recover.
---

# Config Edit Guard

A bad config edit can brick a service. If the gateway won't start, you can't fix it — you're offline. Validate before restarting. Always.

## The Iron Law

```
NO SERVICE RESTART WITHOUT CONFIG VALIDATION FIRST
```

## The Protocol

### 1. Back up before editing

```bash
cp <config_file> <config_file>.bak
```

Do this BEFORE making any changes. Every time. No exceptions.

### 2. Read before editing

Read the full file first. Understand the existing structure. Identify exactly where your change goes. Do not guess at field names or invent keys — verify they exist in the schema or docs.

### 3. Merge, don't overwrite

Edit surgically. Change only what you need. Do not rewrite the file. Do not drop existing fields.

### 4. Validate before restarting

**JSON:**
```bash
python3 -c "import json; json.load(open('<config_file>')); print('OK')"
```

**YAML:**
```bash
python3 -c "import yaml; yaml.safe_load(open('<config_file>')); print('OK')"
```

**Must print `OK`.** If it shows an error, fix it before proceeding.

### 5. Restore if broken

If you can't fix the validation error:
```bash
cp <config_file>.bak <config_file>
```

Then start over. Do not attempt a restart with broken config.

### 6. Only then restart

```bash
openclaw gateway restart
# or whatever service depends on this config
```

## Why This Matters

- OpenClaw gateway reads `openclaw.json` on startup
- If the JSON is invalid, the gateway crashes
- If the gateway is down, the agent is offline
- An offline agent cannot fix its own config
- The human must SSH in and repair manually

This applies to ANY service config, not just OpenClaw:
- nginx (`nginx -t` before `systemctl reload`)
- systemd units (`systemd-analyze verify` before enabling)
- Docker compose (`docker compose config` before `up`)
- Any daemon that reads config at startup

## Red Flags — STOP

- "I'll just restart and see if it works"
- "The change is small, it can't break anything"
- "I'll fix it if it fails" (you can't — you're offline)
- Restarting without running the validation command
- Editing config from memory without reading the file first

## Common Mistakes

| Mistake | Result |
|---------|--------|
| Trailing comma in JSON | Parse error, gateway won't start |
| Missing quote on a string | Parse error, gateway won't start |
| Inventing a field name | Gateway starts but ignores the field silently |
| Overwriting the whole file | Lose all existing config |
| Forgetting to back up | No recovery path if edit breaks things |
| Using `~` in paths inside JSON | Not expanded — treated as literal `~` |

## Validation Checklist

Before every service restart after a config change:

- [ ] Backup exists (`<file>.bak`)
- [ ] Config validates (`OK` from parser)
- [ ] Only intended fields changed (diff against backup)
- [ ] Paths are absolute (no `~`)
- [ ] No trailing commas, no syntax errors
- [ ] Service restart command is ready
