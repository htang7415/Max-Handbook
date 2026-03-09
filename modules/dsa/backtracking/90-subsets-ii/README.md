# 90.Subsets II

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate all subsets of the array without returning duplicate subsets.

## Recognition Cues

- You need all subsets, but the input contains duplicates.
- Different index choices can lead to the same subset values.
- Deduplication must happen during generation, not only after.

## Baseline Idea

Generate every subset and remove duplicates afterward with a set. That works, but it wastes search effort and needs extra normalization.

## Core Insight

Sort the array so equal values are adjacent. At each recursion depth, skip a value if it is the same as the previous value chosen from that depth.

## Invariant / State

- `path` is the current subset.
- `start` is the next index allowed.
- At one depth, the first copy of a duplicated value may start a branch, but later equal values at the same depth are skipped.

## Walkthrough

For `[1, 2, 2]`:
- Record `[]`, `[1]`, and `[1, 2]`.
- After using the first `2`, skip starting a sibling branch from the second `2` at the same depth.
- This keeps `[1, 2]` and `[2]` unique.

## Complexity

- Time: `O(n * 2^n)` in the worst case
- Space: `O(n)` auxiliary space, excluding the output

## Edge Cases

- Empty list
- All values equal
- A single duplicate pair

## Common Mistakes

- Forgetting to sort before duplicate skipping
- Using `i > 0` instead of `i > start`
- Deduplicating the whole result after generation instead of pruning branches early

## Pattern Transfer

- 78.Subsets
- 47.Permutations II
- 40.Combination Sum II

## Self-Check

- Why is sorting required for this duplicate rule?
- Why does the skip condition depend on `start`?
- What duplicates would appear if you removed the skip?

## Function

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/90-subsets-ii/python -q
```
