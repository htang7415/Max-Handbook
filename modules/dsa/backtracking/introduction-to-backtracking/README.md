# Introduction to Backtracking

> Track: `dsa` | Topic: `backtracking`

## What This Module Covers

Backtracking builds answers by exploring choices, recursing on partial solutions, and undoing those choices before trying the next branch.

## Recognition Cues

- You need to generate all valid answers.
- The problem naturally branches on "choose / skip / try next option".
- Partial solutions can be checked and pruned before they are complete.

## Core Ideas

- Backtracking is DFS over a decision tree.
- The current path or partial board is the key state.
- Correct backtracking always includes a restore step after recursion.

## Common Mistakes

- Forgetting to undo a choice before exploring the next sibling branch.
- Copying too much state instead of mutating and restoring.
- Delaying pruning until the end when invalid branches could stop earlier.

## Connections

- Combinations, subsets, permutations, and board search all reuse the same recursive skeleton.
- Duplicate handling becomes a separate design choice when inputs repeat.
- Pruning quality often matters more than syntax.

## Self-Check

- What is the choice list at each depth?
- What state must be restored on the way back up?
- Where can you prune safely?
