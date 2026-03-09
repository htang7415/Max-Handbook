# 213.House Robber II

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the most money you can rob when the houses form a circle.

## Recognition Cues

- Adjacent houses cannot both be robbed.
- The first and last houses are also adjacent because the street is circular.
- Breaking the circle into linear cases simplifies the problem.

## Baseline Idea

Try every valid subset of houses that avoids adjacent picks and keep the best sum. That works, but the search space grows exponentially.

## Core Insight

In a circle, you cannot take both the first and last house. So solve two linear robber problems:
- rob houses `0..n-2`
- rob houses `1..n-1`

Take the larger of those two answers.

## Invariant / State

- For the linear helper, `prev1` is the best result up to the previous house.
- `prev2` is the best result up to the house before that.

## Walkthrough

For `[2, 3, 2]`:
- If you exclude the last house, the best from `[2, 3]` is `3`.
- If you exclude the first house, the best from `[3, 2]` is also `3`.
- The final answer is `3`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- One house
- Two houses
- A circle where the endpoints would otherwise both be attractive

## Common Mistakes

- Solving it like the linear house robber problem without handling the circle
- Forgetting the single-house special case
- Including both first and last houses in the same scenario

## Pattern Transfer

- 198.House Robber
- Break a circular constraint into linear cases
- Rolling DP over arrays

## Self-Check

- Why are exactly two linear cases enough?
- Why must first and last be separated?
- What do `prev1` and `prev2` represent in the helper?

## Function

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/213-house-robber-ii/python -q
```
