# Backtracking Summary

> Track: `dsa` | Topic: `backtracking`

## What This Module Covers

This summary reviews the main backtracking families: combinations, subsets, permutations, partitioning, and search with pruning.

## Recognition Cues

- The output space is exponential, but it still needs a systematic generator.
- A partial answer can be extended step by step.
- Constraint checks can rule out branches early.

## Core Ideas

- Combinations usually advance a start index.
- Permutations usually track used choices.
- Partitioning and board problems rely on incremental validity checks.
- Deduplication logic depends on whether duplicates conflict on a path or at a depth.

## Common Mistakes

- Using the wrong template for the problem family.
- Handling duplicates globally when they are really a same-depth issue.
- Forgetting that order matters for permutations but not for subsets.

## Connections

- DFS on trees has the same recursive shape.
- Dynamic programming appears when you count or optimize instead of enumerate.
- Hash sets often support deduplication and pruning.

## Self-Check

- How do combinations and permutations differ structurally?
- When do you need a `used` array versus a `start` index?
- What kinds of pruning preserve correctness?
