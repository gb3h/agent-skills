---
name: fact-check-before-trust
description: >-
  Verify factual claims in agent output before acting on them. Use when: output contains
  numbers, prices, dates, legal requirements, named entities, or causal claims that will
  be acted upon or communicated to others.
---

# Fact-Check Before Trust

Completion verification checks that a task was *done*. This skill checks that the *facts are correct*. A confidently stated wrong number passes completion checks — this skill catches it.

## When to Invoke

Before treating agent output as authoritative when it contains:
- **Numbers or money** — prices, quantities, measurements, statistics
- **Dates and deadlines** — filing deadlines, release dates, expiry dates
- **Named entities** — people, organisations, laws, product names
- **Causal claims** — "X causes Y", "because of Z"
- **Superlatives** — "the largest", "the only", "the most recent"

**Skip for:** code output, file operations, clearly self-contained tasks.

## Verification Protocol

### Step 1: Extract Claims
List every verifiable claim explicitly:
```
Claim 1: Widget costs $49/month
Claim 2: Free tier supports up to 1000 requests
Claim 3: API launched in March 2024
```

### Step 2: Verify Each Claim
For each claim, check against a primary source:
- Official documentation or website
- Government/regulatory sources for legal claims
- Direct API response for technical claims

### Step 3: Flag Discrepancies
For any claim that can't be verified or is wrong:
- State what the source says vs. what was claimed
- Correct the output before delivering
- Note confidence level: verified / unverified / corrected

## Key Principle

**Confidence is not evidence.** An agent stating something firmly does not make it true. The more specific and consequential a claim, the more it needs verification.
