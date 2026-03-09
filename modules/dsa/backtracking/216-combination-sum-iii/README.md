# 216.Combination Sum III

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Choose `k` distinct numbers from `1` through `9` so their sum is `n`.

## Recognition Cues

- The candidate range is fixed and small: `1..9`.
- Each number can be used at most once.
- You need all valid combinations, not just one.

## Baseline Idea

Generate all subsets of `1..9`, filter by length `k`, then filter again by sum. That works, but it explores many unnecessary branches.

## Core Insight

Backtrack in increasing order, track the remaining sum, and stop early whenever the next candidate would exceed the remaining target.

## Invariant / State

- `path` is the current combination.
- `remaining` is the sum still needed.
- `start` is the smallest next number allowed, so values stay distinct and ordered.

## Walkthrough

For `k = 3`, `n = 7`:
- Start with `1`, then `2`, leaving `4`.
- Add `4` to reach exactly `0`, so record `[1, 2, 4]`.

## Complexity

- Time: bounded by subsets of `1..9`, heavily pruned
- Space: `O(k)` recursion depth, excluding the output

## Edge Cases

- No valid combination
- `k = 1`
- Target too small or too large for `k` distinct numbers

## Common Mistakes

- Reusing the same number
- Forgetting to stop when `remaining` becomes too small
- Recording combinations before checking both length and sum

## Pattern Transfer

- 77.Combinations
- 39.Combination Sum
- 40.Combination Sum II

## Self-Check

- Why must the recursive call move to `i + 1`?
- Why is the candidate range only `1..9` important?
- When can the loop break early?

## Function

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/216-combination-sum-iii/python -q
```
