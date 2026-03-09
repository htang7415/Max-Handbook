# 0-1 Knapsack Theory (Part 1)

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This note introduces the classic 2D 0-1 knapsack DP, where each item can be chosen at most once and capacity is the main constraint.

## Recognition Cues

- Every item is either taken or skipped.
- Capacity is limited.
- The goal is to maximize value while respecting weight.

## Core Ideas

- Let `dp[i][c]` be the best value using the first `i` items with capacity `c`.
- For each item, either skip it or take it if it fits.
- The 2D table makes the state meaning very explicit.

## Common Mistakes

- Reusing the same item multiple times by mistake.
- Writing the transition before deciding what `i` means.
- Confusing "first `i` items" with "item at index `i`".

## Connections

- Part 2 compresses the same idea to 1D.
- Partition and target-sum variants are knapsack descendants.
- Capacity DP patterns show up throughout the DP track.

## Self-Check

- What does `dp[i][c]` represent?
- Why does each item offer only two choices?
- What changes when an item does not fit?

## Function

```python
class Solution:
    def knapSack(self, weights: List[int], values: List[int], capacity: int) -> int:
```
