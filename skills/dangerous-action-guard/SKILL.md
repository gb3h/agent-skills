---
name: dangerous-action-guard
description: >-
  Pause and confirm before destructive or irreversible actions. Use when: about to delete files,
  drop databases, send external communications, modify production configs, force-push git branches,
  or perform any action that cannot be easily undone.
---

# Dangerous Action Guard

Some actions can't be undone. Pause before executing them.

## Dangerous Actions (Always Pause)

- **Deletion:** `rm -rf`, `DROP TABLE`, `trash` of important files, clearing logs
- **Overwrites:** Force-push (`git push --force`), overwriting config files, truncating databases
- **External comms:** Sending emails, posting tweets, publishing content
- **Infrastructure:** Stopping services, modifying firewall rules, changing DNS
- **Credentials:** Revoking tokens, changing passwords, modifying auth config
- **Financial:** Any action involving payments, subscriptions, or billing

## Protocol

### 1. Identify the Action
State exactly what you're about to do and why.

### 2. Assess Reversibility
- **Reversible:** File in trash, git commit (can revert) → proceed with caution
- **Hard to reverse:** Email sent, DNS changed → confirm with user
- **Irreversible:** Data deleted without backup, token revoked → **always confirm**

### 3. Confirm
For hard-to-reverse and irreversible actions:
- State the action clearly to the user
- State what cannot be undone
- Wait for explicit confirmation before proceeding

### 4. Safer Alternatives
Always prefer:
- `trash` over `rm`
- `git stash` over discarding changes
- Draft/preview over send
- Staging over production
- Backup before modify

## Exception: Emergencies
If a system is actively failing and inaction causes more damage than action, proceed but document what you did and why.
