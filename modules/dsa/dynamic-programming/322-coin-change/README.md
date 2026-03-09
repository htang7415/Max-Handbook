# 322.Coin Change

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Return the fewest coins needed to make the target amount, or `-1` if it is impossible.

## Recognition Cues

- You need a minimum count.
- Coin values can be reused unlimited times.
- This is a complete-knapsack style optimization problem.

## Baseline Idea

Try all combinations of coins recursively and keep the smallest valid count. That works, but it revisits the same remaining amounts repeatedly.

## Core Insight

Let `dp[amount]` be the fewest coins needed to form that total. For each coin, update all reachable totals by considering one more use of that coin.

## Invariant / State

- `dp[t]` is the best known minimum coin count for total `t`.
- `dp[0] = 0` because zero coins are needed to make amount zero.

## Walkthrough

For `coins = [1, 2, 5]` and `amount = 11`:
- Using coin `1` fills all totals with a baseline count.
- Coin `2` improves some totals.
- Coin `5` improves `10` and then `11`, leading to `5 + 5 + 1`, so the answer is `3`.

## Complexity

- Time: `O(len(coins) * amount)`
- Space: `O(amount)`

## Edge Cases

- Amount `0`
- Impossible target
- Coin set with `1`

## Common Mistakes

- Confusing minimum-count DP with counting the number of combinations
- Forgetting to initialize unreachable states to a large sentinel
- Returning the sentinel instead of `-1` when no solution exists

## Pattern Transfer

- Complete knapsack
- 279.Perfect Squares
- Minimum-step DP

## Self-Check

- What does `dp[t]` represent?
- Why can a coin be reused multiple times?
- How do you detect that the amount is impossible?

## Function

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/322-coin-change/python -q
```
