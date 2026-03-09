# Queue Reconstruction by Height (Vector Explanation)

> Track: `dsa` | Topic: `greedy-algorithm`

## What This Module Covers

This note gives an alternate vector-insertion explanation of queue reconstruction: sort people so the harder height constraints are fixed first, then insert each person at the exact index required by `k`.

## Recognition Cues

- Taller people determine the valid positions of shorter people.
- The final position depends on how many taller-or-equal people are already placed.
- A sorted insertion process is easier to reason about than brute-force rebuilding.

## Core Ideas

- Sort by height descending and `k` ascending.
- Use vector or list insertion at index `k`.
- Once taller people are fixed, shorter insertions cannot invalidate their counts.

## Common Mistakes

- Sorting shorter people first.
- Sorting equal heights by descending `k`.
- Thinking insertion is arbitrary instead of the actual greedy step.

## Connections

- The main `406` problem module.
- Sort-then-insert greedy patterns.
- Constraint-preserving reconstruction by handling the most restrictive elements first.

## Self-Check

- Why are taller people handled first?
- Why does inserting at index `k` become correct after sorting?
- What role does equal-height ordering play?

## Function

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
```
