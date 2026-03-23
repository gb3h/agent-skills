---
name: writing-plans
description: >-
  Create clear, reviewable implementation plans before executing. Use when: about to implement
  something that takes more than a few steps, after brainstorming to formalize the chosen approach,
  or when work may span multiple sessions.
---

# Writing Plans

Write comprehensive implementation plans assuming the implementer has zero context. Document everything: which files to touch, exact code, how to test, what to commit. Bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

## Scope Check

If the design covers multiple independent subsystems, it should have been decomposed during brainstorming. If not, suggest breaking into separate plans — one per subsystem. Each plan should produce working, testable software on its own.

## File Structure Mapping

Before defining tasks, map out which files will be created or modified and what each one is responsible for:

- Each file should have one clear responsibility
- Prefer smaller, focused files over large ones doing too much
- Files that change together should live together
- In existing codebases, follow established patterns
- This structure informs the task decomposition

## Plan Document Structure

```markdown
# [Feature Name] Implementation Plan

**Goal:** [One sentence — what does success look like?]
**Approach:** [2-3 sentences about architecture/method]
**Files:**
- Create: `exact/path/to/new-file.py`
- Modify: `exact/path/to/existing.py`
- Test: `tests/exact/path/to/test_file.py`

---

### Task 1: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Test: `tests/path/to/test_file.py`

- [ ] **Step 1:** Write the failing test
  ```python
  def test_specific_behavior():
      result = function(input)
      assert result == expected
  ```

- [ ] **Step 2:** Run test to verify it fails
  Run: `pytest tests/path/test_file.py::test_specific_behavior -v`
  Expected: FAIL — "function not defined"

- [ ] **Step 3:** Write minimal implementation
  ```python
  def function(input):
      return expected
  ```

- [ ] **Step 4:** Run test to verify it passes
  Run: `pytest tests/path/test_file.py -v`
  Expected: PASS

- [ ] **Step 5:** Commit
  ```bash
  git add tests/path/test_file.py src/path/file.py
  git commit -m "feat: add specific feature"
  ```
```

## Bite-Sized Task Granularity

Each step is ONE action (2-5 minutes):
- "Write the failing test" — one step
- "Run it to confirm it fails" — one step
- "Implement minimal code to pass" — one step
- "Run tests to confirm green" — one step
- "Commit" — one step

If a step says "and also" — split it.

## Plan Quality Checks

- Every step has exact file paths and runnable commands
- Steps ordered by dependency, not importance
- Each task produces self-contained changes that make sense independently
- Complete code in plan — not "add validation" but the actual validation code
- Verification built into steps, not a separate phase
- References to `test-driven-development` skill for TDD discipline

## Where to Store Plans

- **Short plans:** directly in chat or `memory/YYYY-MM-DD.md`
- **Complex plans:** dedicated file in workspace (e.g., `memory/plans/YYYY-MM-DD-feature-name.md`)

## Checkpointing

For tasks spanning sessions, mark checkpoint steps:
```
- [ ] Step 5: Integration tests [CHECKPOINT]
```

At each checkpoint, write progress to `memory/YYYY-MM-DD.md`:
- Steps completed
- Current state
- Decisions made
- Exact next step to resume from

## After Writing the Plan

Offer execution choice:

1. **Subagent-driven** (recommended for multi-task plans) — dispatch fresh subagent per task via `sessions_spawn`, review between tasks. Use `subagent-driven-development` skill.
2. **Inline execution** — execute tasks in current session with checkpoints. Use `executing-plans` skill.
