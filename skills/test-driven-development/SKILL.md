---
name: test-driven-development
description: >-
  Red/green/refactor discipline for writing reliable code. Use when: writing new functionality,
  fixing bugs that need regression tests, or refactoring existing code.
---

# Test-Driven Development

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? **Delete it. Start over.**

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

**Violating the letter of these rules is violating the spirit of the rules.**

## Red-Green-Refactor

### RED — Write Failing Test

Write one minimal test describing the behavior you want.

Requirements:
- One behavior per test
- Clear name that reads like a specification: `test_expired_token_returns_401`
- Real code, not mocks (unless unavoidable)

### Verify RED — Watch It Fail (MANDATORY)

Run the test. Confirm:
- Test **fails** (not errors from typos)
- Failure message matches expectation
- Fails because the feature is missing

**Test passes?** You're testing existing behavior. Fix the test.

### GREEN — Minimal Code

Write the **simplest** code to make the test pass. No extra features. No cleanup. No over-engineering. Just pass the test.

### Verify GREEN — Watch It Pass (MANDATORY)

Run the test. Confirm:
- Test passes
- ALL other tests still pass
- Output clean (no errors, warnings)

**Test fails?** Fix the code, not the test.

### REFACTOR — Clean Up

After green only:
- Remove duplication
- Improve names
- Extract helpers

Keep tests green. Don't add behavior during refactor.

### Repeat

Next failing test for next behavior.

## Why Order Matters

**"I'll write tests after to verify it works"** — Tests written after code pass immediately. Passing immediately proves nothing. You never saw the test catch the bug. Tests-after answer "what does this do?" Tests-first answer "what SHOULD this do?"

**"I already manually tested all edge cases"** — Manual testing is ad-hoc. No record of what you tested. Can't re-run when code changes. "It worked when I tried it" ≠ comprehensive.

**"Deleting X hours of work is wasteful"** — Sunk cost fallacy. The time is already gone. Working code without real tests is technical debt. Delete and rewrite with TDD = high confidence. Keep and add tests after = low confidence, likely bugs.

**"TDD is dogmatic, being pragmatic means adapting"** — TDD IS pragmatic. Finds bugs before commit. Prevents regressions. Documents behavior. Enables refactoring. "Pragmatic" shortcuts = debugging in production = slower.

## Good Tests

| Quality | Good | Bad |
|---------|------|-----|
| **Minimal** | Tests one thing. "and" in name? Split it. | `test_validates_email_and_domain_and_whitespace` |
| **Clear** | Name describes behavior | `test_test1` |
| **Shows intent** | Demonstrates desired API | Obscures what code should do |
| **Independent** | No test depends on another's state | Shared mutable state between tests |
| **Fast** | Milliseconds, not seconds | Database round-trips per test |

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard to write = skip it" | Hard to test = hard to use. Listen to the test. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "TDD will slow me down" | TDD is faster than debugging. Always. |
| "Existing code has no tests" | You're improving it. Add tests for what you touch. |
| "Manual test is faster" | Manual doesn't prove edge cases. You'll re-test every change. |

## Red Flags — STOP and Start Over

- Code written before test
- Test passes immediately (without new code)
- Can't explain why test failed
- "Just this once" rationalization
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "It's about spirit not ritual"
- "Already spent X hours, deleting is wasteful"

**All of these mean: Delete code. Start over with TDD.**

## When TDD Doesn't Fit

Ask user before skipping:
- Throwaway prototypes (write tests after if it survives)
- Generated code
- Configuration-only changes
- One-off scripts that won't be maintained

## Bug Fix Pattern

1. **RED:** Write test reproducing the bug
2. **Verify RED:** Watch it fail with the expected symptom
3. **GREEN:** Fix the bug with minimal change
4. **Verify GREEN:** Test passes, all other tests pass
5. Test proves fix AND prevents regression

Never fix bugs without a test.
