# 70.Climbing Stairs

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many distinct ways there are to reach step `n` if you can climb 1 or 2 steps at a time.

## Recognition Cues

- You are counting ways, not constructing paths.
- The current answer depends on smaller instances of the same problem.
- Each move has only a small number of options.

## Baseline Idea

Use recursion and branch into “take 1 step” or “take 2 steps.” This repeats the same subproblems many times.

## Core Insight

To reach step `n`, the last move must come from step `n - 1` or `n - 2`, so `f(n) = f(n - 1) + f(n - 2)`.

## Invariant / State

- `a` stores the number of ways to reach the previous step.
- `b` stores the number of ways to reach the current step.

## Walkthrough

For `n = 5`:
- Ways to reach steps `1` and `2` are `1` and `2`.
- Step `3` has `3` ways.
- Step `4` has `5` ways.
- Step `5` has `8` ways.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- `n = 1`
- `n = 2`
- Very small inputs where the base cases matter

## Common Mistakes

- Using the recurrence without handling base cases first
- Confusing “number of ways” with “minimum steps”
- Using recursion without memoization and getting exponential time

## Pattern Transfer

- 746.Min Cost Climbing Stairs
- Fibonacci Number
- House Robber

## Self-Check

- Why do only the previous two states matter?
- What are the correct base cases?
- How is this similar to Fibonacci and how is it different?

## Function

```python
class Solution:
    def climbStairs(self, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/70-climbing-stairs/python -q
```
