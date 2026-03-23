---
name: daily-review
description: >-
  End-of-day structured summary with memory updates and next priorities. Use when: ending a work
  day, during evening heartbeats, or when explicitly asked for a daily summary.
---

# Daily Review

End each active day with a structured review. This maintains continuity across sessions.

## Review Process

### 1. Summarize the Day
Write to `memory/YYYY-MM-DD.md`:

```markdown
# Daily Review — YYYY-MM-DD

## Accomplished
- [Task 1]: [outcome]
- [Task 2]: [outcome]

## Decisions Made
- [Decision]: [reasoning]

## Open Items
- [ ] [Task]: [status, next step]

## Lessons Learned
- [What went wrong/right and why]

## Tomorrow's Priorities
1. [Most important]
2. [Second]
3. [Third]
```

### 2. Update Long-Term Memory
Review if anything from today belongs in `MEMORY.md`:
- New project context
- User preferences discovered
- Technical lessons worth keeping
- Relationship/communication insights

### 3. Clean Up
- Close any open files or processes
- Commit workspace changes if appropriate
- Update HEARTBEAT.md if recurring tasks changed

## When to Skip

- Nothing meaningful happened (just greetings, quick answers)
- Already wrote detailed notes during the day that cover everything

## Frequency

- Daily if active work happened
- Skip days with no substantive interaction
- Weekly consolidation: review the week's daily files and update MEMORY.md
