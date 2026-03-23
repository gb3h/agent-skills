---
name: verification-before-completion
description: >-
  Verify tasks are actually done, not just attempted. Use when: about to declare a task complete,
  finishing a sub-agent task, before reporting results to the user, confirming prior work was done
  correctly, verifying a setup or configuration, or when asked to check that something is working.
---

# Verification Before Completion

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you haven't run the verification command **in this message**, you cannot claim it passes.

**Violating the letter of this rule is violating the spirit of this rule.**

## The Gate Function

```
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY — What command/check proves this claim?
2. RUN — Execute it fresh and complete (use exec or read)
3. READ — Full output, check exit code, count failures
4. VERIFY — Does output actually confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, not verifying.
```

## Common Failures

| Claim | Requires | NOT Sufficient |
|-------|----------|----------------|
| "Tests pass" | Test command output: 0 failures | Previous run, "should pass" |
| "Build succeeds" | Build command: exit 0 | Linter passing, "looks good" |
| "Bug fixed" | Original symptom gone + test passes | "Code changed, assumed fixed" |
| "File created" | `read` or `ls` confirms existence + content | "I wrote the file" |
| "Config works" | Service restart + endpoint responds | "Config is valid JSON" |
| "Subagent completed" | Verify actual changes (git diff, read files) | Trust subagent's "success" report |
| "Requirements met" | Line-by-line checklist against spec | "Tests pass" |

## Verification Checklist

### For code changes:
- [ ] Code runs without errors (`exec` the test/build command)
- [ ] All tests pass (not just new ones)
- [ ] The specific requirement is demonstrably met
- [ ] No regressions in existing functionality

### For file operations:
- [ ] File exists at expected path (`read` it back)
- [ ] Content matches intent
- [ ] Permissions correct if relevant

### For deployments:
- [ ] Service is running
- [ ] Endpoint responds correctly
- [ ] Logs show no errors

### For configuration:
- [ ] Config is valid (parse/lint it)
- [ ] Change survives restart
- [ ] Dependent services still work

## Red Flags — STOP

- Using "should", "probably", "seems to"
- Expressing satisfaction before verification ("Great!", "Done!", "Perfect!")
- About to commit/push without verification
- Trusting subagent success reports without checking
- Relying on partial verification
- **ANY wording implying success without having run verification**

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification. |
| "I'm confident" | Confidence ≠ evidence. |
| "Just this once" | No exceptions. |
| "Linter passed" | Linter ≠ compiler ≠ runtime. |
| "Subagent said success" | Verify independently. |
| "Partial check is enough" | Partial proves nothing. |

## The Rule

**If you cannot verify a step, do not mark it complete.** Note exactly what remains unverified and why. Partial completion honestly reported is better than false completion.
