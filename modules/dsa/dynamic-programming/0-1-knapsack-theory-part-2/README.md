# 0-1 Knapsack Theory (Part 2)

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This note compresses 0-1 knapsack from a 2D table to a 1D array while preserving the "use each item at most once" rule.

## Recognition Cues

- The 2D state depends only on the previous item row.
- Capacity is still the key axis.
- Space can be compressed if update order is correct.

## Core Ideas

- Let `dp[c]` be the best value for capacity `c` after processing the current prefix of items.
- Iterate capacity backward so each item contributes at most once.
- Backward iteration is what preserves the 0-1 property.

## Common Mistakes

- Iterating capacity forward and accidentally allowing item reuse.
- Compressing before understanding the 2D version.
- Forgetting that the 1D array still represents a row-by-row update.

## Connections

- Part 1 explains the original 2D meaning.
- Complete knapsack flips the capacity direction.
- Many DP problems use this same row-compression trick.

## Self-Check

- Why must capacity iterate backward here?
- What does `dp[c]` mean after one more item is processed?
- What behavior would forward iteration allow by mistake?

## Function

```python
class Solution:
    def knapSack(self, weights: List[int], values: List[int], capacity: int) -> int:
```
