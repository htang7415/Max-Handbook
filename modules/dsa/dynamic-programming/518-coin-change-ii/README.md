# 518.Coin Change II

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many unordered combinations of coins make up the amount.

## Recognition Cues

- You are counting combinations, not minimizing coins.
- Coin order does not matter.
- Coins can be reused unlimited times.

## Baseline Idea

Recursively try how many times to use each coin and count the valid totals. That works, but it repeats many subproblems.

## Core Insight

Let `dp[total]` be the number of combinations that make `total`. Process coins one by one. For each coin, update totals forward so the coin can be reused, but the outer coin loop prevents counting different orders separately.

## Invariant / State

- After processing some coins, `dp[t]` is the number of combinations using only those coins that make total `t`.

## Walkthrough

For `amount = 5` and `coins = [1, 2, 5]`:
- Coin `1` gives one way to make every total.
- Coin `2` adds new combinations such as `2 + 2 + 1`.
- Coin `5` adds one more combination using the single `5`.
- The final count is `4`.

## Complexity

- Time: `O(amount * len(coins))`
- Space: `O(amount)`

## Edge Cases

- Amount `0`
- No valid combination
- One coin type

## Common Mistakes

- Counting permutations instead of combinations
- Swapping loop order and changing the meaning of the count
- Forgetting that amount `0` has one valid combination

## Pattern Transfer

- Complete knapsack counting DP
- 377.Combination Sum IV for the ordered version
- Unbounded resource counting

## Self-Check

- Why does coin order not matter here?
- Why must the coin loop be outside the total loop?
- What does `dp[0] = 1` represent?

## Function

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/518-coin-change-ii/python -q
```
