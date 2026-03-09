# 39.Combination Sum

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate all combinations of candidate numbers that sum to `target`, allowing reuse of the same candidate.

## Recognition Cues

- You need all valid combinations, not just one.
- Candidates can be reused.
- The running sum determines whether a branch can continue.

## Baseline Idea

Try every possible sequence of candidates and filter the ones that sum to `target`. That repeats many equivalent branches.

## Core Insight

Sort the candidates and backtrack with a remaining sum. Reuse is handled by recursing from the same index, and sorting lets you prune branches once a value is too large.

## Invariant / State

- `path` is the current combination.
- `remaining` is how much sum is still needed.
- `start` ensures combinations are built in nondecreasing order, so duplicates are avoided.

## Walkthrough

For `candidates = [2, 3, 6, 7]`, `target = 7`:
- Choose `2`, then `2`, then `3` to make `[2, 2, 3]`.
- Backtrack and try `7` directly to make `[7]`.

## Complexity

- Time: exponential in the number of valid search branches
- Space: `O(target / min(candidates))` auxiliary recursion depth in the worst case

## Edge Cases

- No combination exists
- A candidate equals the target
- Reusing the same small candidate many times

## Common Mistakes

- Advancing to `i + 1` when reuse is allowed
- Forgetting to sort before pruning
- Not copying `path` when a solution is found

## Pattern Transfer

- 40.Combination Sum II
- 216.Combination Sum III
- 77.Combinations

## Self-Check

- Why does reuse mean the recursive call stays at index `i`?
- Why does sorting enable pruning?
- How does `start` avoid duplicate combinations?

## Function

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/39-combination-sum/python -q
```
