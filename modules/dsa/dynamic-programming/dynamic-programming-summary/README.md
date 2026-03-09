# Dynamic Programming Summary

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This summary reviews the main DP patterns in the track: linear DP, knapsack, sequence alignment, interval DP, tree DP, and small-state optimization.

## Recognition Cues

- The same smaller subproblems appear again and again.
- You need a count, minimum, maximum, or feasibility answer.
- The hard part is often state design, not raw implementation.

## Core Ideas

- Define the state before the loops.
- Make base cases explicit.
- Write the transition in words before coding it.
- Verify that loop order matches the dependency direction.

## Common Mistakes

- Using the wrong state meaning and compensating with messy code.
- Mixing 0/1 and complete-knapsack loop directions.
- Forgetting whether the answer lives in the last state or the global maximum.

## Connections

- Knapsack teaches capacity DP.
- LCS/edit distance teach two-sequence DP.
- Stock and tree problems teach compact multi-state DP.

## Self-Check

- What does each state mean?
- Which earlier states feed into it?
- Does the loop order respect those dependencies?
