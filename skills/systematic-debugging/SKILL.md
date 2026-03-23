---
name: systematic-debugging
description: >-
  4-phase root cause analysis before applying fixes. Use when: encountering an error,
  a test fails unexpectedly, behavior doesn't match expectations, or a previous fix didn't work.
---

# Systematic Debugging

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes. Random fixes waste time and create new bugs. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read error messages carefully.** Don't skip past errors or warnings. Read stack traces completely. Note line numbers, file paths, error codes. They often contain the exact solution.

2. **Reproduce consistently.** Can you trigger it reliably? What are the exact steps? If not reproducible → gather more data, don't guess.

3. **Check recent changes.** Git diff, recent commits, new dependencies, config changes, environmental differences.

4. **Gather evidence in multi-component systems.** When the system has multiple components (CI → build → deploy, API → service → database):

   For EACH component boundary:
   - Log what data enters the component
   - Log what data exits the component
   - Verify environment/config propagation
   - Check state at each layer

   Run once to gather evidence showing WHERE it breaks. THEN analyze. THEN investigate that specific component.

5. **Trace data flow backward.** When the error is deep in the call stack:
   - Where does the bad value originate?
   - What called this function with the bad value?
   - Keep tracing up until you find the source
   - **Fix at source, not at symptom**

   Use `exec` to add temporary logging at component boundaries. Use `read` to trace through call chains.

## Phase 2: Pattern Analysis

1. **Find working examples** — locate similar working code in the same codebase
2. **Compare against references** — if implementing a pattern, read the reference implementation COMPLETELY. Don't skim.
3. **Identify differences** — list every difference between working and broken, however small
4. **Understand dependencies** — what other components, settings, config, environment does this need?

## Phase 3: Hypothesis and Testing

1. **Form a single hypothesis** — state clearly: "I think X is the root cause because Y." Write it down.
2. **Test minimally** — make the SMALLEST possible change to test the hypothesis. One variable at a time. Don't fix multiple things at once.
3. **Verify before continuing** — Did it work? Yes → Phase 4. No → form NEW hypothesis. DON'T add more fixes on top.

## Phase 4: Fix and Verify

1. **Create a failing test** (if applicable) — simplest possible reproduction. Use `test-driven-development` skill.
2. **Implement single fix** — address root cause. ONE change at a time. No "while I'm here" improvements.
3. **Verify fix** — test passes? No other tests broken? Issue actually resolved?
4. **If fix doesn't work** — STOP. Count: how many fixes have you tried?
   - If < 3: return to Phase 1, re-analyze with new information
   - **If ≥ 3: STOP and question the architecture** (see below)

### After 3+ Failed Fixes: Question Architecture

Pattern indicating architectural problem:
- Each fix reveals new shared state/coupling/problems in different places
- Fixes require "massive refactoring" to implement
- Each fix creates new symptoms elsewhere

**STOP and question fundamentals:**
- Is this pattern fundamentally sound?
- Are we sticking with it through sheer inertia?
- Should we refactor architecture vs. continue fixing symptoms?

Discuss with the user before attempting more fixes. This is NOT a failed hypothesis — this is a wrong architecture.

## Defense-in-Depth

After finding and fixing a root cause, add validation at EVERY layer data passes through:

| Layer | Purpose | Example |
|-------|---------|---------|
| Entry point | Reject invalid input at API boundary | Validate params aren't empty/null |
| Business logic | Ensure data makes sense for this operation | Check required fields exist |
| Environment guard | Prevent dangerous ops in specific contexts | Refuse destructive action in prod |
| Debug instrumentation | Capture context for forensics | Log before dangerous operations |

Single validation: "We fixed the bug." Multiple layers: "We made the bug impossible."

## Red Flags — STOP and Return to Phase 1

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "One more fix attempt" (when already tried 2+)
- "Here are the main problems:" (listing fixes without investigation)
- Proposing solutions before tracing data flow

**ALL of these mean: STOP. Return to Phase 1.**

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question the pattern. |
| "Reference too long, I'll adapt" | Partial understanding guarantees bugs. Read it completely. |

## Condition-Based Waiting

When debugging flaky/timing issues: wait for the actual condition, not an arbitrary delay.

```
# Bad: guessing at timing
sleep 2 && check_result

# Good: polling for condition
while ! check_condition; do sleep 0.1; done
```

If you MUST use an arbitrary timeout, document WHY with the known timing basis.
