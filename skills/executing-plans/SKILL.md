---
name: executing-plans
description: >-
  Execute plans step-by-step with verification and checkpointing. Use when: implementing
  a written plan, working through a multi-step task, or resuming work from a checkpoint.
---

# Executing Plans

Load plan. Review critically. Execute all tasks. Verify each step. Report when complete.

**If subagents are available:** consider using `subagent-driven-development` instead — fresh context per task yields higher quality.

## Step 1: Load and Review Plan

1. Read the plan file with `read`
2. Review critically — identify questions, concerns, missing context, or unclear steps
3. **If concerns exist:** raise them with the user BEFORE starting. Do not silently work around plan gaps.
4. If no concerns: proceed to execution

## Step 2: Execute Tasks

For each task in the plan:

1. **Read** the step — understand exactly what it asks
2. **Execute** exactly what the step says — no scope creep, no "while I'm here" improvements
3. **Verify** with concrete evidence (file exists, test passes, command succeeds). Use `exec` and `read` — not assumptions.
4. **Mark done** — update the plan: `[x]`
5. **Continue** to next step

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Step fails and you can't diagnose why within 2 attempts
- Plan has a gap preventing the next step
- You don't understand an instruction
- Verification fails repeatedly
- Something contradicts the plan's assumptions

**Ask for clarification rather than guessing.** Guessing compounds errors across subsequent steps.

## When to Revisit Earlier Steps

- User updates the plan based on your feedback
- A later step reveals an earlier step was done incorrectly
- Fundamental approach needs rethinking

**Don't force through blockers.** Stop, surface the issue, wait for direction.

## Rules

- **Never start on main/master branch** without explicit user consent
- **Stay on task.** Unrelated issues go in `memory/YYYY-MM-DD.md` — don't fix them mid-step
- **No silent skips.** If you skip a step, state why and the consequences
- **Use `systematic-debugging`** if a step fails unexpectedly
- **Use `verification-before-completion`** before declaring any step done

## Checkpointing

At checkpoint steps (or every 3-5 tasks), write to `memory/YYYY-MM-DD.md`:
- Steps completed so far
- Current state of work
- Decisions made during execution
- Exact next step to resume from

## Resuming from Checkpoint

1. Read the most recent memory file with `read`
2. Find the last checkpoint
3. Verify checkpoint state is still valid (files exist, no conflicts)
4. Resume from the next step
