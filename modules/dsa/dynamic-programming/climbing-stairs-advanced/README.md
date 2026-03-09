# Climbing Stairs (Advanced)

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This variant generalizes climbing stairs: instead of fixed step sizes like `1` and `2`, you may use any step sizes from a provided list.

## Recognition Cues

- You are counting ways to reach a target total.
- Step sizes can be reused.
- The answer depends on smaller totals that lead into the current total.

## Core Ideas

- Let `dp[i]` be the number of ways to reach stair `i`.
- Each allowed step size contributes from `dp[i - step]` when it fits.
- The loop order determines whether order matters in the count.

## Common Mistakes

- Forgetting that variable steps change the recurrence, not the overall DP structure.
- Using the wrong loop order for ordered versus unordered counting.
- Missing the base case `dp[0] = 1`.

## Connections

- Combination Sum IV and coin-change counting variants.
- Complete-knapsack style counting over totals.
- Rolling one-dimensional DP over reachable sums.

## Self-Check

- What does `dp[i]` represent?
- Why does `dp[0]` need to be `1`?
- Does this version count ordered paths or unordered selections?

## Function

```python
class Solution:
    def climbStairsAdvanced(self, n: int, steps: List[int]) -> int:
```
