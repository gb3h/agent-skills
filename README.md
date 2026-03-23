# Agent Skills

19 plug-and-play skills for [OpenClaw](https://github.com/openclaw/openclaw) agents. Battle-tested methodology, operational guardrails, and development workflows.

No dependencies. No install scripts. Just markdown skill files your agent reads and follows.

## Skills

### Methodology
| Skill | What it enforces |
|-------|-----------------|
| `brainstorming` | Structured ideation: explore → propose 2-3 approaches → evaluate → get approval before implementing |
| `writing-plans` | Clear implementation plans with file maps, bite-sized steps, risks, and definition of done |
| `executing-plans` | Step-by-step plan execution with review checkpoints and "stop and ask" discipline |
| `systematic-debugging` | 4-phase root cause analysis. Iron Law: no fixes without investigation first |
| `test-driven-development` | Red/green/refactor. Iron Law: no production code without a failing test first |
| `verification-before-completion` | Evidence before claims. Iron Law: no completion claims without fresh verification |
| `fact-check-before-trust` | Extract claims, score confidence, verify before acting on numbers/dates/names |

### Operational
| Skill | What it enforces |
|-------|-----------------|
| `dangerous-action-guard` | Pause and confirm before destructive/irreversible actions (rm, force-push, external sends) |
| `workspace-integrity-guardian` | Hash critical workspace files, detect unauthorized modifications or drift |
| `agent-self-recovery` | Detect stuck loops, name the pattern, break out systematically |
| `task-handoff` | Structured handoff documents when work can't be completed in current session |
| `context-window-management` | Strategies to prevent context overflow in long-running sessions |
| `long-running-task-management` | Break multi-hour tasks into checkpointed, resumable stages |
| `daily-review` | End-of-day structured summary with memory updates and next priorities |

### Development Workflow
| Skill | What it enforces |
|-------|-----------------|
| `subagent-driven-development` | Per-task subagent dispatch with review gates between tasks |
| `requesting-code-review` | Structured review dispatch: gather diff, craft context, act on severity |
| `receiving-code-review` | Evaluate before implementing. Push back when wrong. No sycophantic agreement. |
| `writing-skills` | TDD for skills: baseline test → write skill → pressure test → close loopholes |

### Enforcement
| Skill | What it enforces |
|-------|-----------------|
| `skill-discipline` | Meta-skill: check and use skills on every non-trivial task. Mandatory verification exit gate. |

## Installation

### For OpenClaw agents

Add the repo's `skills/` directory to `skills.load.extraDirs` in `~/.openclaw/openclaw.json`:

```json
{
  "skills": {
    "load": {
      "extraDirs": [
        "/path/to/agent-skills/skills"
      ],
      "watch": true
    }
  }
}
```

Then restart the gateway:
```bash
openclaw gateway restart
```

Verify:
```bash
openclaw skills list | grep -c "openclaw-extra"
# Expected: 19
```

### ⚠️ Do NOT use symlinks

OpenClaw rejects symlinks that resolve outside their configured root directory. Use `extraDirs` instead.

### For other agent frameworks

Each skill is a standalone `SKILL.md` file. Copy the ones you want into your agent's skill/instruction directory. No dependencies between skills — pick what you need.

## How it works

Skills are markdown files with YAML frontmatter. Your agent reads them when a task matches the skill's description. The `skill-discipline` meta-skill teaches the agent to check for matching skills at every task start.

Key design principles:
- **Iron Laws** — non-negotiable rules (e.g., "no fixes without root cause investigation")
- **Rationalization tables** — pre-empt the excuses agents use to skip process
- **Hard gates** — block progression until conditions are met (e.g., no implementation before design approval)
- **Verification exit gate** — every skill chains into verification before reporting results

## Trigger testing

All skills tested via isolated subagents with prompts that don't name the skill. Each agent must independently discover and load the correct skill.

| Round | Pass rate | Notes |
|-------|-----------|-------|
| Round 1 (skills not loaded) | 0/10 | Baseline — agents never reached for skills |
| Round 2 (skills loaded) | 9/10 | One edge case on verification framing |
| Round 3 (description fix) | 10/10 | All skills trigger correctly |
| New + upgraded skills | 8/8 | Including 4 new dev workflow skills |

## Requirements

- OpenClaw 2026.3.22+ (or any agent framework that reads markdown skill files)
- Python 3 (only for `workspace-integrity-guardian/scripts/guard.py` — stdlib only, no pip)

## Origin

Inspired by [obra/superpowers](https://github.com/obra/superpowers). All skills rewritten from scratch for OpenClaw's persistent agent runtime.

## License

MIT
