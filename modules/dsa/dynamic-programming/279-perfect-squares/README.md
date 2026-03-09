# 279.Perfect Squares

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Return the minimum number of perfect squares whose sum is `n`.

## Recognition Cues

- You need a minimum count, not the actual combination.
- The same square values can be reused multiple times.
- This is a classic complete-knapsack style DP.

## Baseline Idea

Try all combinations of square numbers recursively until the sum reaches `n`. That works, but it repeats the same subproblems heavily.

## Core Insight

Let `dp[i]` be the minimum number of squares needed to make sum `i`. For each `i`, try every square `j * j <= i` and take the best transition from `dp[i - j*j] + 1`.

## Invariant / State

- `dp[i]` stores the minimum square count needed to form total `i`.
- Smaller totals are solved before larger totals that depend on them.

## Walkthrough

For `n = 12`:
- `12` can use square `1`, `4`, or `9`.
- The best route is `4 + 4 + 4`, so `dp[12] = 3`.

## Complexity

- Time: `O(n * sqrt(n))`
- Space: `O(n)`

## Edge Cases

- `n = 1`
- `n` already a perfect square
- Values that need several repeated small squares

## Common Mistakes

- Treating it like a one-time-use knapsack
- Forgetting to initialize worst-case values for DP
- Minimizing over all squares larger than the current target

## Pattern Transfer

- Complete knapsack
- Minimum-step DP
- 322.Coin Change

## Self-Check

- What does `dp[i]` mean?
- Why can the same square be reused?
- Why is `dp[i - j*j] + 1` the right transition?

## Function

```python
class Solution:
    def numSquares(self, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/279-perfect-squares/python -q
```
