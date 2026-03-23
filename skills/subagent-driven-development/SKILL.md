---
name: subagent-driven-development
description: >-
  Execute implementation plans by dispatching fresh subagents per task. Use when: executing
  implementation plans with independent tasks in the current session.
---

# Subagent-Driven Development

Execute a plan by dispatching a fresh subagent per task via `sessions_spawn`, with review after each. Fresh context per task = no pollution, high quality, fast iteration.

## When to Use

- Have a written implementation plan (from `writing-plans`)
- Tasks are mostly independent
- Want to stay in the current session (vs. handing off with `executing-plans`)

**vs. Executing Plans:** Same session, fresh subagent per task, no context pollution, review checkpoints are automatic.

## The Process

### 1. Load and Prepare

1. Read the plan file once with `read`
2. Extract all tasks with full text and context
3. Review critically — raise concerns before starting
4. Note shared context that subagents will need (project structure, conventions, dependencies)

### 2. Per-Task Loop

For each task:

**Dispatch implementer:**
```
sessions_spawn with:
- Full task text (don't make subagent read the plan file)
- Relevant context (project structure, related files, conventions)
- Instructions: follow TDD, commit when done, report status
```

**Handle implementer status:**

| Status | Action |
|--------|--------|
| **DONE** | Proceed to review |
| **DONE_WITH_CONCERNS** | Read concerns. If about correctness/scope, address before review. If observations, note and proceed. |
| **NEEDS_CONTEXT** | Provide missing context, re-dispatch |
| **BLOCKED** | Assess: context problem → provide and retry. Task too complex → break into smaller pieces. Plan wrong → escalate to user. |

**Review the work:**
- Check git diff for the task's changes
- Verify tests pass (`exec` the test command)
- Verify changes match spec (read the files)
- If issues found: dispatch a fix subagent with specific instructions. Don't fix manually (context pollution).

**Mark task complete and continue.**

### 3. Final Review

After all tasks:
- Run full test suite
- Review overall changes (`git diff` against starting point)
- Verify all requirements met (line-by-line against spec)
- Use `verification-before-completion` skill

## Model Selection

Use the least powerful model that handles each role:

| Task Type | Model | Signals |
|-----------|-------|---------|
| Mechanical implementation | Fast/cheap | 1-2 files, clear spec, isolated function |
| Integration work | Standard | Multi-file coordination, pattern matching |
| Architecture/review | Most capable | Design judgment, broad codebase understanding |

## Subagent Instructions Template

When dispatching, provide:
1. **What to build** — full task text from plan
2. **Where it fits** — project context, related components
3. **How to verify** — exact test commands, expected output
4. **Conventions** — coding style, commit message format, branch rules

Don't make the subagent discover context. Provide everything upfront.

## Red Flags

**Never:**
- Skip review after a task
- Dispatch multiple implementation subagents in parallel (conflicts)
- Make subagent read the plan file (provide full text)
- Ignore subagent questions (answer before letting them proceed)
- Accept "close enough" on spec compliance
- Start on main/master without explicit user consent
- Fix subagent work manually (dispatch a fix subagent instead)
- Proceed with unfixed issues from review

**If subagent asks questions:** Answer clearly and completely. Provide additional context. Don't rush them.

**If subagent fails:** Dispatch fix subagent with specific instructions + context about what went wrong. Don't retry the same subagent without changes.
