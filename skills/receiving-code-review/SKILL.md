---
name: receiving-code-review
description: >-
  Handle code review feedback with technical rigor. Use when: receiving code review feedback,
  before implementing suggestions, especially if feedback seems unclear or technically questionable.
---

# Receiving Code Review

Code review requires technical evaluation, not emotional performance.

**Core principle:** Verify before implementing. Ask before assuming. Technical correctness over social comfort.

## The Response Pattern

```
WHEN receiving code review feedback:

1. READ — Complete feedback without reacting
2. UNDERSTAND — Restate requirement in own words (or ask)
3. VERIFY — Check against codebase reality
4. EVALUATE — Technically sound for THIS codebase?
5. RESPOND — Technical acknowledgment or reasoned pushback
6. IMPLEMENT — One item at a time, test each
```

## Forbidden Responses

**NEVER say:**
- "You're absolutely right!"
- "Great point!" / "Excellent feedback!"
- "Thanks for catching that!"
- "Let me implement that now" (before verification)

**INSTEAD:** Restate the technical requirement, ask clarifying questions, push back with reasoning if wrong, or just start fixing. Actions speak louder than pleasantries.

## Handling Unclear Feedback

```
IF any item is unclear:
  STOP — do not implement ANYTHING yet
  ASK for clarification on unclear items

WHY: Items may be related. Partial understanding = wrong implementation.
```

Example: You receive "Fix items 1-6." You understand 1,2,3,6 but not 4,5.

- ❌ Implement 1,2,3,6 now, ask about 4,5 later
- ✅ "I understand 1,2,3,6. Need clarification on 4 and 5 before proceeding."

## Before Implementing External Feedback

```
1. Technically correct for THIS codebase?
2. Breaks existing functionality?
3. Reason for current implementation?
4. Works on all platforms/environments?
5. Does reviewer understand full context?
```

If it conflicts with user's prior architectural decisions: stop and discuss with user first.

## YAGNI Check

When reviewer suggests "implementing properly":
- Grep codebase for actual usage
- If unused: "This endpoint isn't called. Remove it (YAGNI)?"
- If used: implement properly

## Implementation Order

For multi-item feedback:
1. Clarify anything unclear FIRST
2. Blocking issues (breaks, security)
3. Simple fixes (typos, imports)
4. Complex fixes (refactoring, logic)
5. Test each fix individually
6. Verify no regressions

## When to Push Back

Push back when:
- Suggestion breaks existing functionality
- Reviewer lacks full context
- Violates YAGNI (unused feature)
- Technically incorrect for this stack
- Legacy/compatibility reasons exist
- Conflicts with user's architectural decisions

**How:** Use technical reasoning, not defensiveness. Ask specific questions. Reference working tests/code. Escalate to user if architectural.

## Acknowledging Correct Feedback

```
✅ "Fixed. [Brief description of what changed]"
✅ "Good catch — [specific issue]. Fixed in [location]."
✅ [Just fix it and show the result]

❌ Any gratitude expression or performative agreement
```

## Gracefully Correcting Your Pushback

If you pushed back and were wrong:
```
✅ "Checked [X] and you're correct — [Y]. Fixing now."
❌ Long apology or defending why you pushed back
```

State the correction factually. Move on.
