# 77.Combinations (Optimized)

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate all size-`k` combinations from `1..n`, while pruning branches that cannot possibly finish.

## Recognition Cues

- This is the same search space as combinations, but with explicit pruning.
- Once too few numbers remain, deeper recursion is pointless.
- The optimization changes only the loop bound, not the answer set.

## Baseline Idea

Run ordinary combinations backtracking and let impossible branches fail naturally. That works, but it explores extra states.

## Core Insight

At any point, if `path` needs `r` more values, the next start index only needs to go up to `n - r + 1`. Larger starts cannot fill the combination.

## Invariant / State

- `path` is the current combination prefix.
- `max_start` is the largest valid first choice that still leaves enough numbers to finish.

## Walkthrough

For `n = 4`, `k = 2`:
- At the top level, starts may be `1`, `2`, or `3`.
- Starting at `4` is impossible because no second number remains, so that branch is pruned.

## Complexity

- Time: `O(C(n, k) * k)` with less wasted branching than the basic version
- Space: `O(k)` recursion depth, excluding the output

## Edge Cases

- `k = 0`
- `k = n`
- Small `n` where pruning removes almost nothing

## Common Mistakes

- Computing the pruning bound incorrectly
- Using the optimization but changing the result set
- Forgetting that `path.copy()` is still required

## Pattern Transfer

- 77.Combinations
- Pruned backtracking templates
- Branch-and-bound style search

## Self-Check

- What does `max_start` mean?
- Why is starting beyond `max_start` pointless?
- How does this differ from the unoptimized version?

## Function

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/77-combinations-optimized/python -q
```
