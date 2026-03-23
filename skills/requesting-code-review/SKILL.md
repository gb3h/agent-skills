---
name: requesting-code-review
description: >-
  Dispatch code review subagents to catch issues before they compound. Use when: completing tasks
  in subagent-driven development, after implementing major features, or before merging to main.
---

# Requesting Code Review

Dispatch a review subagent via `sessions_spawn` to evaluate work product. The reviewer gets precisely crafted context — never your session history.

## When to Request

**Mandatory:**
- After each task in subagent-driven development
- After completing a major feature
- Before merge to main

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing a complex bug

## How to Request

### 1. Gather Context

```bash
# Get the diff
git diff origin/main..HEAD

# Or for a specific range
git log --oneline -5
git diff <base_sha>..<head_sha>
```

### 2. Dispatch Review Subagent

Via `sessions_spawn`, provide:

- **What was implemented** — brief description of what was built
- **Requirements/spec** — what it should do (paste relevant section or file path)
- **Diff or file paths** — the actual code to review
- **Focus areas** — anything you're uncertain about

The reviewer should evaluate:
- Spec compliance (does it do what was asked?)
- Code quality (clean, testable, no duplication?)
- Edge cases and error handling
- Test coverage

### 3. Act on Feedback

| Severity | Action |
|----------|--------|
| **Critical** | Fix immediately. Blocks everything. |
| **Important** | Fix before proceeding to next task. |
| **Minor** | Note for later. Don't block progress. |

### 4. Push Back When Reviewer Is Wrong

- Provide technical reasoning
- Show code/tests that prove it works
- Reference existing patterns or user decisions
- Don't blindly implement incorrect feedback

## Integration

**Subagent-driven development:** Review after EACH task. Catch issues before they compound.

**Executing plans:** Review after each batch (3-5 tasks).

**Ad-hoc work:** Review before merge.
