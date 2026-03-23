---
name: writing-skills
description: >-
  Create, test, and deploy agent skills using TDD methodology. Use when: creating new skills,
  editing existing skills, or verifying skills work before deployment.
---

# Writing Skills

**Writing skills IS Test-Driven Development applied to process documentation.**

You write test cases (pressure scenarios with subagents), watch them fail (baseline behavior), write the skill, watch tests pass (agents comply), and refactor (close loopholes).

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

## What Is a Skill?

A reusable reference guide for proven techniques, patterns, or tools. Skills help future agent instances find and apply effective approaches.

**Skills are:** reusable techniques, patterns, tools, reference guides.
**Skills are NOT:** narratives about how you solved a problem once.

### Skill Types

| Type | Examples | What it contains |
|------|----------|-----------------|
| **Technique** | condition-based-waiting, root-cause-tracing | Concrete method with steps |
| **Pattern** | flatten-with-flags, test-invariants | Way of thinking about problems |
| **Reference** | API docs, command guides | Lookup material |

## SKILL.md Structure

```yaml
---
name: skill-name-with-hyphens
description: >-
  Use when [specific triggering conditions and symptoms].
---
```

**Frontmatter rules:**
- Only `name` and `description` fields
- `name`: letters, numbers, hyphens only
- `description`: third person, starts with "Use when...", max ~500 chars
- **CRITICAL: Description = triggering conditions ONLY, NOT workflow summary**

**Why this matters:** Testing revealed that when descriptions summarize workflow, agents follow the description instead of reading the full skill. A description saying "code review between tasks" caused agents to do ONE review, even though the skill specified TWO reviews. When changed to just triggering conditions, agents read and followed the full content.

**Body structure:**
```markdown
# Skill Name

## Overview / Core Principle (1-2 sentences)

## When to Use (symptoms, situations, contexts)

## Core Pattern / Process

## Common Mistakes

## Quick Reference (table for scanning)
```

**Directory structure:**
```
skills/
  skill-name/
    SKILL.md              # Main reference (required)
    supporting-file.*     # Only if needed (heavy reference, reusable tools)
```

Skills live in your workspace (`skills/`) or system-wide (`~/.openclaw/skills/`).

## RED-GREEN-REFACTOR for Skills

### RED: Baseline Test (Watch It Fail)

Run pressure scenario via `sessions_spawn` WITHOUT the skill:

```
Dispatch subagent with realistic task + combined pressures:
- Time pressure ("deploy window closing in 5 min")
- Sunk cost ("spent 4 hours on this")
- Exhaustion ("it's 6pm, dinner at 6:30")
- Authority ("manager says skip it")

Force explicit A/B/C choice. Document:
- What choice did the agent make?
- What rationalizations did it use (verbatim)?
- Which pressures triggered violations?
```

This is "watch the test fail" — you MUST see what agents naturally do before writing the skill.

### GREEN: Write Minimal Skill

Write skill addressing the specific rationalizations from baseline. Don't add content for hypothetical cases — address actual observed failures.

Run same scenarios WITH skill via `sessions_spawn`. Agent should now comply.

### REFACTOR: Close Loopholes

Agent found new rationalization despite the skill? Add explicit counter:

1. **Explicit negation in rules** — don't just state the rule, forbid specific workarounds
2. **Entry in rationalization table** — every excuse gets a row with reality check
3. **Red flags list** — easy self-check for agents
4. **Update description** — add symptoms of ABOUT to violate

Re-test until bulletproof.

## Bulletproofing Against Rationalization

For discipline-enforcing skills (TDD, verification):

- **Close every loophole explicitly.** Don't just say "delete it" — say "don't keep as reference, don't adapt, don't look at it, delete means delete."
- **Add foundational principle early:** "Violating the letter of the rules is violating the spirit of the rules." This cuts off an entire class of rationalizations.
- **Build rationalization table** from baseline testing. Every excuse agents make goes in the table.
- **Create red flags list** — easy self-check for when agents are rationalizing.

## Testing Different Skill Types

| Skill Type | Test With | Success = |
|------------|-----------|-----------|
| **Discipline** (TDD, verification) | Pressure scenarios with 3+ combined pressures | Agent follows rule under max pressure |
| **Technique** (debugging, tracing) | Application scenarios + edge cases | Agent applies technique correctly |
| **Pattern** (mental models) | Recognition + counter-examples | Agent knows when/how to apply |
| **Reference** (API docs) | Retrieval + application scenarios | Agent finds and uses info correctly |

## Common Rationalizations for Skipping Tests

| Excuse | Reality |
|--------|---------|
| "Skill is obviously clear" | Clear to you ≠ clear to other agents. Test it. |
| "It's just a reference" | References have gaps. Test retrieval. |
| "Testing is overkill" | Untested skills have issues. Always. |
| "I'll test if problems emerge" | Problems = agents can't use skill. Test BEFORE deploying. |
| "Too tedious to test" | Less tedious than debugging bad skill in production. |

## Skill Creation Checklist

**RED Phase:**
- [ ] Create pressure scenarios (3+ combined pressures for discipline skills)
- [ ] Run scenarios WITHOUT skill via `sessions_spawn` — document baseline verbatim
- [ ] Identify patterns in rationalizations/failures

**GREEN Phase:**
- [ ] Valid frontmatter: `name` (hyphens only) + `description` (starts "Use when...")
- [ ] Description is triggering conditions only (NO workflow summary)
- [ ] Keywords throughout for discovery
- [ ] Addresses specific baseline failures
- [ ] Run scenarios WITH skill — verify compliance

**REFACTOR Phase:**
- [ ] New rationalizations countered explicitly
- [ ] Rationalization table built from all iterations
- [ ] Red flags list created
- [ ] Re-test until bulletproof

**Deploy:**
- [ ] Commit and push
- [ ] Consider contributing back if broadly useful

## Discovery Optimization

Future agents find your skill by scanning descriptions. Optimize for this:

- Use concrete triggers, symptoms, situations
- Describe the PROBLEM, not language-specific symptoms
- Include error messages, tool names, symptoms as keywords
- Write in third person (injected into system prompt)
- **Never summarize workflow in description** — agents will shortcut
