# 77.Combinations

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate every size-`k` combination chosen from the numbers `1` through `n`.

## Recognition Cues

- You must generate all valid answers, not just count them.
- Order inside a result does not matter.
- Each choice reduces the remaining search space.

## Baseline Idea

Generate all subsets or all permutations and filter the ones of size `k`. That does extra work because it explores many invalid branches.

## Core Insight

Build the answer one number at a time in ascending order. Once you choose a number, the next choice can only come from the numbers after it.

## Invariant / State

- `path` stores the current partial combination.
- `start` is the smallest next number allowed, so combinations are never repeated in a different order.

## Walkthrough

For `n = 4`, `k = 2`:
- Start with `[]`, choose `1`, then try `2`, `3`, and `4`.
- Backtrack to `[]`, choose `2`, then try `3` and `4`.
- Continue until every length-2 path is collected.

## Complexity

- Time: `O(C(n, k) * k)`
- Space: `O(k)` auxiliary space, excluding the output

## Edge Cases

- `k = 0`
- `k = 1`
- `k = n`

## Common Mistakes

- Forgetting to copy `path` before appending it to the result
- Restarting the loop from `1` each time and generating duplicates
- Forgetting to pop after the recursive call

## Pattern Transfer

- 216.Combination Sum III
- 78.Subsets
- 46.Permutations
- 39.Combination Sum

## Self-Check

- Why does `start` prevent duplicate combinations?
- Why do we need `path.copy()`?
- What changes if order starts to matter?

## Function

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/77-combinations/python -q
```
