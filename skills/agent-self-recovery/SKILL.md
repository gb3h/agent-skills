---
name: agent-self-recovery
description: >-
  Detect stuck loops and break out systematically. Use when: repeating the same action
  more than twice without progress, hitting the same error repeatedly, or sensing that
  you're going in circles.
---

# Agent Self-Recovery

Agents get stuck. The key is recognizing it early and breaking out deliberately.

## Stuck Patterns to Watch For

1. **Retry loop** — Same command, same error, >2 attempts
2. **Fix spiral** — Each fix creates a new error, no net progress
3. **Scope creep drift** — Started task A, now working on task G
4. **Overthinking freeze** — Generating analysis without taking action
5. **Tool misuse** — Using the wrong tool repeatedly because the right one isn't obvious

## Recovery Protocol

### 1. Name the Pattern
Stop and explicitly state: "I'm stuck in a [pattern name]." Writing it down breaks the loop.

### 2. Capture State
Write down:
- What I was trying to do
- What I've tried so far
- What keeps failing and why

### 3. Change Strategy
Pick ONE:
- **Step back:** Re-read the original task. Am I solving the right problem?
- **Simplify:** What's the minimum version of this that could work?
- **Ask:** Tell the user what's happening and ask for guidance
- **Defer:** Write a handoff document (see `task-handoff`) and stop
- **Research:** Stop guessing, read docs/source code

### 4. Set a Limit
"I will try this new approach for N steps. If it doesn't work, I'll [escalate/defer/ask]."

## Prevention

- After 2 failed attempts at the same thing, pause and assess
- Keep a mental (or written) count of retries
- If you're writing the same command again, something is wrong
