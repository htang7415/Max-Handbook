# 746.Min Cost Climbing Stairs

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the minimum total cost needed to reach the top of the staircase.

## Recognition Cues

- Each step depends on the cheapest way to reach previous steps.
- You can move 1 or 2 steps at a time.
- The answer is a minimum cost, not a count of ways.

## Baseline Idea

Recursively try both previous steps and take the cheaper result. That repeats the same subproblems many times.

## Core Insight

The minimum cost to reach step `i` is the cheaper of:
- paying `cost[i - 1]` after reaching step `i - 1`
- paying `cost[i - 2]` after reaching step `i - 2`

## Invariant / State

- `prev1` is the minimum cost to reach the previous step.
- `prev2` is the minimum cost to reach the step before that.

## Walkthrough

For `[10, 15, 20]`:
- Reach step `2` with cost `10`.
- Reach step `3` with cost `15`.
- Final answer is `15`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Very short cost list
- A cheap path that skips an expensive step
- Equal costs on many steps

## Common Mistakes

- Returning the cost of the last step instead of the top
- Treating the top as an extra paid step
- Forgetting that you can start from step `0` or step `1`

## Pattern Transfer

- 70.Climbing Stairs
- 198.House Robber
- Rolling-state DP

## Self-Check

- Why is the top itself free?
- What do `prev1` and `prev2` represent?
- How is this different from counting ways to climb stairs?

## Function

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/746-min-cost-climbing-stairs/python -q
```
