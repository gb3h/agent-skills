---
name: context-window-management
description: >-
  Strategies to prevent context overflow in long sessions. Use when: working on complex
  multi-step tasks, sessions are getting long, or you notice tool outputs being truncated.
---

# Context Window Management

Context is finite. Manage it or lose coherence.

## Symptoms of Context Pressure

- Tool outputs getting truncated or compacted
- Forgetting earlier parts of the conversation
- Repeating work already done
- Losing track of the current plan

## Strategies

### 1. Externalize State
Don't hold state in context — write it to files:
- Progress tracking → `memory/YYYY-MM-DD.md`
- Plans → workspace files
- Intermediate results → temp files

### 2. Minimize Tool Output
- Use `head`, `tail`, `grep` instead of `cat` for large files
- Use `read` with `offset`/`limit` for targeted file access
- Pipe commands: `command | head -20` instead of full output
- Use `--quiet` or `--brief` flags where available

### 3. Delegate to Sub-Agents
Large independent subtasks should be sub-agents, not inline work. Each sub-agent gets a fresh context window.

### 4. Checkpoint and Restart
If context is getting heavy:
1. Write a handoff document (see `task-handoff`)
2. Summarize current state to memory
3. Suggest the user start a new session to continue

### 5. Avoid Context Bloat
- Don't re-read files you've already processed
- Don't paste large outputs into messages — summarize
- Clean up: once a tool output is processed, the information should be in your working state, not re-fetched

## Rule of Thumb

If you're doing more than ~15 tool calls on a single task, consider whether a sub-agent or checkpoint would be more efficient.
