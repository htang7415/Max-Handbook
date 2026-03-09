# 47.Permutations II

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate all unique permutations when the input may contain duplicate values.

## Recognition Cues

- Order matters, but duplicate values can create repeated permutations.
- Naively permuting indices will overcount.
- Duplicate control must happen during generation.

## Baseline Idea

Generate all permutations and deduplicate them afterward with a set. That works, but it wastes a lot of search effort.

## Core Insight

Sort the array and skip a duplicated value if the identical previous value has not been used in the current position choice.

## Invariant / State

- `used[i]` marks whether `nums[i]` is already in the current path.
- If `nums[i] == nums[i - 1]` and `used[i - 1]` is `False`, starting with `nums[i]` here would duplicate another branch.

## Walkthrough

For `[1, 1, 2]`:
- Start with the first `1`.
- Skip starting a sibling branch with the second `1` before the first one is used.
- This keeps only the three unique permutations.

## Complexity

- Time: up to `O(n * n!)` in the worst case, reduced by duplicate pruning
- Space: `O(n)` auxiliary space, excluding the output

## Edge Cases

- All values equal
- One duplicate pair
- Single element

## Common Mistakes

- Forgetting to sort before duplicate skipping
- Using the wrong duplicate condition
- Deduplicating only after generating all permutations

## Pattern Transfer

- 46.Permutations
- 90.Subsets II
- 40.Combination Sum II

## Self-Check

- Why is sorting necessary?
- What does `not used[i - 1]` mean in the skip rule?
- What duplicate branch is being prevented?

## Function

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/47-permutations-ii/python -q
```
