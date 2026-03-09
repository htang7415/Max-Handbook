# 40.Combination Sum II

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate all unique combinations that sum to the target when each candidate can be used at most once.

## Recognition Cues

- You need all valid combinations, but duplicates exist in the input.
- Each element may be used only once.
- Sorting and pruning can cut off repeated or impossible branches.

## Baseline Idea

Generate all subsets, compute their sums, and deduplicate afterward. That works, but it does extra work and wastes branches.

## Core Insight

Sort the candidates, skip duplicate values at the same depth, and recurse with `i + 1` so each element is used at most once.

## Invariant / State

- `path` is the current combination.
- `remaining` is the sum still needed.
- `start` is the next index allowed, preventing reuse of earlier elements.

## Walkthrough

For `[10,1,2,7,6,1,5]` with target `8`:
- After sorting, try `1`, then another `1`, then `6` to form `[1,1,6]`.
- Skip duplicate sibling starts where the same value would recreate the same combination.

## Complexity

- Time: exponential in the number of explored branches
- Space: `O(n)` recursion depth, excluding the output

## Edge Cases

- No valid combination
- Duplicate values that can form the same sum
- A single value equals the target

## Common Mistakes

- Using `i` instead of `i + 1` and accidentally reusing elements
- Forgetting to sort before duplicate skipping
- Skipping duplicates globally instead of only at the same recursion depth

## Pattern Transfer

- 39.Combination Sum
- 47.Permutations II
- 90.Subsets II

## Self-Check

- Why must the recursive call move to `i + 1`?
- Why does the duplicate rule depend on `start`?
- How does sorting enable pruning?

## Function

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/40-combination-sum-ii/python -q
```
