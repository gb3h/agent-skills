---
name: task-handoff
description: >-
  Write structured handoff documents for incomplete work. Use when: a task can't be completed
  in the current session, work needs to be continued by a future session or different agent,
  or you're hitting context limits and need to checkpoint.
---

# Task Handoff

When you can't finish, leave a clear trail for whoever picks up next.

## Handoff Document Format

Write to `memory/YYYY-MM-DD.md` or a dedicated file:

```markdown
## Handoff: [Task Name]
**Status:** [In Progress | Blocked | Partially Complete]
**Date:** YYYY-MM-DD HH:MM UTC

### What was the goal
[1-2 sentences]

### What's done
- [x] Step 1: description
- [x] Step 2: description

### What remains
- [ ] Step 3: description
- [ ] Step 4: description

### Current state
- Key files modified: [list]
- Branch/commit: [ref]
- Services running: [list]

### Blockers
[What's preventing completion, if anything]

### Context needed to resume
[Anything non-obvious the next session needs to know]

### Decisions made
[Any choices made during execution and why]
```

## When to Hand Off

- Context window getting full (see `context-window-management`)
- Session ending
- Blocked on external input
- Task is better suited for a different approach/model

## Key Principle

A handoff should let someone resume without reading the entire conversation history. Be specific about state, not just intent.
