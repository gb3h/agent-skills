# Agent Skills

19 skills for OpenClaw agents. Methodology, operational guardrails, dev workflows.

## Install (for OpenClaw agents)

### Step 1: Clone

```bash
git clone https://github.com/gb3h/agent-skills.git ~/.openclaw/workspace/agent-skills
```

### Step 2: Find the absolute path to the skills directory

```bash
echo "$(cd ~/.openclaw/workspace/agent-skills/skills && pwd)"
```

Copy the output. You need it for the next step.

### Step 3: Edit `~/.openclaw/openclaw.json`

Read the file first. Find the `"skills"` key. If it exists, add `"load"` inside it. If it doesn't exist, create it.

**You must merge this into the existing config — do NOT overwrite the file.**

Add this inside the `"skills"` object:

```json
"load": {
  "extraDirs": [
    "/ABSOLUTE/PATH/FROM/STEP/2/skills"
  ],
  "watch": true
}
```

Example of what the `skills` block should look like after editing (your existing entries may differ):

```json
"skills": {
  "load": {
    "extraDirs": [
      "/home/youruser/.openclaw/workspace/agent-skills/skills"
    ],
    "watch": true
  },
  "entries": {
    "...existing entries stay here..."
  }
}
```

**Common mistakes:**
- Using `~` instead of the full absolute path → will not work
- Pointing to the repo root instead of the `skills/` subdirectory → will not work
- Creating symlinks instead of using `extraDirs` → will not work (OpenClaw rejects symlinks that resolve outside their root)
- Overwriting the whole file or the whole `skills` block → breaks existing config
- Invalid JSON (trailing commas, missing quotes) → gateway won't start

### Step 4: Restart the gateway

```bash
openclaw gateway restart
```

If the gateway fails to start, you broke the JSON. Run:
```bash
python3 -c "import json; json.load(open('$HOME/.openclaw/openclaw.json'))"
```
This will show the exact syntax error. Fix it, then restart again.

### Step 5: Verify

```bash
openclaw skills list 2>&1 | grep "openclaw-extra" | wc -l
```

**Expected output: `19`**

If output is `0`, debug:

```bash
# Check for symlink rejection:
openclaw skills list 2>&1 | grep -i "skipping"

# Check the path is correct:
ls /ABSOLUTE/PATH/YOU/USED/brainstorming/SKILL.md

# Check config is valid:
python3 -c "import json; d=json.load(open('$HOME/.openclaw/openclaw.json')); print(d.get('skills',{}).get('load',{}))"
```

### Step 6: Test

Spawn a subagent with this prompt:

```
We need to build a notification system for our web app. There are several ways — websockets, SSE, polling. What approach should we take?

At the end of your response, write: SKILLS_LOADED: [list every SKILL.md you read, or "none"]
```

**Pass:** Last line contains `brainstorming` in the SKILLS_LOADED list.
**Fail:** Says `SKILLS_LOADED: none` — go back to Step 5.

## Skills included

**Methodology (7):** brainstorming, writing-plans, executing-plans, systematic-debugging, test-driven-development, verification-before-completion, fact-check-before-trust

**Operational (7):** dangerous-action-guard, workspace-integrity-guardian, agent-self-recovery, task-handoff, context-window-management, long-running-task-management, daily-review

**Dev workflow (4):** subagent-driven-development, requesting-code-review, receiving-code-review, writing-skills

**Enforcement (1):** skill-discipline

## For other agent frameworks

Each skill is a standalone `SKILL.md` file. Copy the `skills/` directory into wherever your agent reads instructions. No dependencies between skills.

## License

MIT
