# Memory

This section is about how an agent keeps useful state across steps and turns without replaying the full conversation every time.

## Purpose

Use this page to understand:
- short-term working memory
- compressed summaries
- retrieval-backed memory

## First Principles

- Memory is useful because agents often need facts from earlier steps after the prompt has changed.
- Good memory is selective. Keeping everything is expensive and often noisy.
- Short summaries are useful for recent task state. Retrieval is better for larger memory stores.

## Concept Ladder

1. Start with short working memory for the current task.
2. Add summaries when recent context is too long to replay.
3. Add retrieval-backed memory when useful facts span many tasks or turns.
4. Add conflict and retention policies when old memories can become stale or wrong.
5. Add scoring only after you know which memories should win.

## Engineering Boundary

This page is the memory map. The runnable implementation lives in `memory-patterns`; use the supporting modules only when the core memory shape is not enough.

## Canonical Modules

- Core memory patterns: `memory-patterns`

## Supporting Modules

- Resolving conflicting memories by recency, trust, and confirmations: `memory-conflict-resolution`
- Retrieval-backed memory over stored notes: `retrieval-backed-memory`
- Compaction of many notes into a shorter working summary: `memory-compaction`
- Retaining high-value notes and evicting weak ones: `memory-retention-policy`
- Scoring notes before retrieval returns them: `memory-retrieval-scoring`

## When To Use What

- Start with `memory-patterns` when the agent must remember user preferences or prior step outputs.
- Use `memory-conflict-resolution` when stored memories disagree and the system needs an explicit choose-or-review rule.
- Use `retrieval-backed-memory` when recent summaries are not enough and the agent needs simple lookup over older notes.
- Use `memory-compaction` when stored notes are growing but the active summary needs to stay short.
- Use `memory-retention-policy` when the store is growing and the agent needs a simple keep-or-drop rule.
- Use `memory-retrieval-scoring` when the memory store needs a better rank order than raw keyword overlap alone.
- Use summaries for recent working state before building a larger retrieval-backed memory layer.
