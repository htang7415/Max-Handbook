# 78.Subsets

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate every subset of the input list.

## Recognition Cues

- You need all possible selections.
- Each element can be either included or excluded.
- The answer size itself is exponential.

## Baseline Idea

Generate all binary masks and convert each mask into a subset. That works, but backtracking expresses the choice process more directly.

## Core Insight

At any recursion state, the current path is already a valid subset. From there, try adding each remaining element one by one.

## Invariant / State

- `path` is the current subset being built.
- `start` is the first index still available for selection.

## Walkthrough

For `[1, 2]`:
- Start with `[]` and record it.
- Add `1`, record `[1]`.
- Add `2`, record `[1, 2]`.
- Backtrack, then try `[2]`.

## Complexity

- Time: `O(n * 2^n)`
- Space: `O(n)` auxiliary space, excluding the output

## Edge Cases

- Empty list
- Single element
- Larger lists where output size grows quickly

## Common Mistakes

- Forgetting to record the empty subset
- Appending `path` directly instead of `path.copy()`
- Restarting choices from index `0` and creating duplicates

## Pattern Transfer

- 77.Combinations
- 90.Subsets II
- 46.Permutations

## Self-Check

- Why is every recursion state already a valid subset?
- Why do we need `path.copy()`?
- What role does `start` play?

## Function

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/78-subsets/python -q
```
