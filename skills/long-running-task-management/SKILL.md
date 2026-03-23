---
name: long-running-task-management
description: >-
  Break multi-hour tasks into checkpointed stages. Use when: a task will take more than
  30 minutes, involves many sequential steps, or may need to survive session restarts.
---

# Long-Running Task Management

Big tasks fail when treated as monoliths. Break them into stages with clear checkpoints.

## Stage Design

### 1. Decompose
Break the task into stages of 10-20 minutes each. Each stage should:
- Have a clear deliverable
- Be independently verifiable
- Leave the workspace in a clean state when complete

### 2. Define Checkpoints
Each stage ends with a checkpoint:
- What was accomplished
- What files were created/modified
- What the next stage should do
- Written to `memory/YYYY-MM-DD.md`

### 3. Execute Stage-by-Stage
- Complete one stage fully before starting the next
- Verify stage completion before checkpointing
- If a stage fails, debug it before moving on

## Checkpoint Format

```markdown
## Checkpoint: [Task] — Stage N/M
**Time:** HH:MM UTC
**Completed:** [what this stage delivered]
**Files:** [created/modified]
**Next:** [what stage N+1 should do]
**Notes:** [anything non-obvious]
```

## When to Use Sub-Agents vs. Stages

- **Sub-agents:** Independent parallel work (research + implementation simultaneously)
- **Stages:** Sequential dependent work (must do A before B)
- **Both:** Large tasks with some parallel and some sequential components

## Recovery

If a session dies mid-stage:
1. Read the last checkpoint from memory
2. Verify workspace state matches checkpoint
3. Resume from where the checkpoint left off
