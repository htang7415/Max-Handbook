# 46.Permutations

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate every ordering of the input numbers.

## Recognition Cues

- Order matters.
- Each element must be used exactly once in each answer.
- The same set of values can appear in many different positions.

## Baseline Idea

Generate all combinations or subsets and try to reorder them afterward. That misses the fact that position-by-position choice is the core difficulty.

## Core Insight

Build the permutation one slot at a time, choosing any value that has not been used yet.

## Invariant / State

- `path` is the current partial permutation.
- `used[i]` tells whether `nums[i]` is already placed in `path`.

## Walkthrough

For `[1, 2, 3]`:
- Choose `1`, then choose between `2` and `3`.
- Backtrack and choose `2` first, then others.
- Continue until every path has length `3`.

## Complexity

- Time: `O(n * n!)`
- Space: `O(n)` auxiliary space, excluding the output

## Edge Cases

- Empty list
- One element
- Values with different signs or zero

## Common Mistakes

- Forgetting to reset `used[i]` during backtracking
- Appending `path` directly instead of copying it
- Confusing permutations with combinations

## Pattern Transfer

- 47.Permutations II
- 77.Combinations
- Backtracking with used-state arrays

## Self-Check

- Why is `used` needed here but not in combinations?
- What makes permutations different from subsets?
- Why must the current path be copied before storing it?

## Function

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/46-permutations/python -q
```
