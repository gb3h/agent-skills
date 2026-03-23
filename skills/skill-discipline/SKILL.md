---
name: skill-discipline
description: >-
  Bootstrap skill that ensures the agent checks and uses skills on every non-trivial task.
  Use when: starting any new task, beginning a session, or when unsure if a relevant skill exists.
  This is the meta-skill that activates all other skills.
---

# Skill Discipline

This is the most important skill. It ensures you actually use the others.

## On Every Non-Trivial Task

Before starting work:

1. **Scan available skills** — Check `<available_skills>` in your system prompt
2. **Match task to skills** — Does any skill's description match what you're about to do?
3. **Load the skill** — Read its `SKILL.md` with the `read` tool
4. **Follow it** — The skill's instructions override your defaults
5. **Announce** — Briefly note which skill you're applying (e.g., "Using systematic-debugging for this error")

## When to Skip

- Trivial questions ("What time is it?")
- Greetings and small talk
- Quick factual answers that need no process
- Following up on an already-active skill

## Priority Order

When instructions conflict:
1. **User's explicit instructions** — always highest priority
2. **Loaded skill instructions** — methodology and process
3. **Default agent behavior** — fallback

## Skill Selection

- If exactly one skill matches: load and follow it
- If multiple could apply: pick the most specific one
- If none match: proceed without a skill — don't force it
- Never load more than one skill at the start; chain them as needed during execution

## Common Skill Triggers

| Situation | Skill |
|-----------|-------|
| Starting a complex task | `brainstorming` → `writing-plans` |
| Implementing a plan | `executing-plans` |
| Hit an error | `systematic-debugging` |
| Writing new code | `test-driven-development` |
| About to say "done" | `verification-before-completion` |
| Output has factual claims | `fact-check-before-trust` |
| About to delete/send | `dangerous-action-guard` |
| Going in circles | `agent-self-recovery` |
| Can't finish now | `task-handoff` |
| Session getting long | `context-window-management` |
| End of day | `daily-review` |

## Mandatory Exit Gate: Verification

Before reporting results to the user — especially after multi-step work, file operations, config changes, or anything you built/modified — load `verification-before-completion` and run its checklist. This is not optional. "I did it" is not the same as "it works."

This applies even when verification wasn't your entry skill. If you used `executing-plans` or `test-driven-development` or any other skill that produces an output, verify before declaring done.

## The Meta-Rule

If you're not sure whether to check skills — check skills. The cost of a quick scan is near zero. The cost of missing a relevant process can be high.
