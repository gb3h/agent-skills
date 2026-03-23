---
name: brainstorming
description: >-
  Structured ideation before implementation. Use when: starting any non-trivial task,
  facing a design decision with multiple viable approaches, or when the path forward is unclear.
---

# Brainstorming

<HARD-GATE>
Do NOT implement anything, write any code, scaffold any project, or take any action until you have presented a design and the user has approved it. This applies to EVERY task regardless of perceived simplicity.
</HARD-GATE>

## Anti-Pattern: "Too Simple to Need a Design"

Every non-trivial task gets a design. A config change, a single-function utility, a "quick script" — all of them. "Simple" projects are where unexamined assumptions waste the most work. The design can be short (a few sentences for truly simple tasks), but you MUST present it and get approval.

## Checklist

Complete in order:

1. **Explore context** — read relevant files, docs, recent commits, existing patterns
2. **Ask clarifying questions** — one at a time, prefer multiple-choice, understand purpose/constraints/success criteria
3. **Propose 2-3 approaches** — with trade-offs and your recommendation (see format below)
4. **Present design** — in sections scaled to complexity, get approval after each section
5. **Transition to implementation** — invoke `writing-plans` skill

## Exploring Context

Before asking questions, understand the landscape:
- Check existing files, project structure, recent git history
- Assess scope: if the request describes multiple independent subsystems, flag immediately — don't spend questions refining details of something that needs decomposition first
- If project is too large for a single design, help decompose into sub-projects. Each gets its own design → plan → implementation cycle.

## Asking Questions

- **One question per message.** Don't overwhelm.
- **Multiple choice preferred** when possible — easier for the user to answer
- **Focus on:** purpose, constraints, success criteria, edge cases
- If a topic needs more exploration, break into multiple questions

## Proposing Approaches

For each approach:
- **What:** Brief description
- **Appeal:** Why it's attractive
- **Risk:** What could go wrong
- **Trade-off:** Cost in complexity, time, or flexibility

Lead with your recommended option and explain why.

## Presenting the Design

- Scale each section to its complexity: a few sentences if straightforward, more detail if nuanced
- Ask after each section whether it looks right
- Cover as relevant: architecture, components, data flow, error handling, testing strategy
- Be ready to revisit and revise

## Design Principles

- **YAGNI ruthlessly** — remove unnecessary features from all designs
- **Isolation and clarity** — break into smaller units with one clear purpose and well-defined interfaces
- **Follow existing patterns** — in existing codebases, match what's already there. Only propose targeted improvements where existing code directly affects the current work.
- **Incremental validation** — present design, get approval, then proceed

## After Approval

- For tasks spanning sessions: save design notes to `memory/YYYY-MM-DD.md`
- Transition to `writing-plans` skill to create implementation plan
- Do NOT jump to implementation. `writing-plans` is the next step.

## When to Skip Brainstorming

- Trivial tasks (rename a file, fix a typo, one-line change)
- Emergencies requiring immediate action (but still think before acting)
- Tasks where the approach is obvious AND low-risk AND the user has already specified what they want
