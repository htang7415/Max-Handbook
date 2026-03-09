# 509.Fibonacci Number

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Return the `n`th Fibonacci number.

## Recognition Cues

- Each answer depends only on the previous two answers.
- This is the smallest useful example of DP / rolling state.
- A full DP table is not necessary because only two prior values matter.

## Baseline Idea

Define Fibonacci recursively from the mathematical recurrence. That works, but naive recursion recomputes the same values repeatedly.

## Core Insight

Build the sequence iteratively from the bottom up while keeping only the two most recent values.

## Invariant / State

- `a` and `b` always represent consecutive Fibonacci values from the sequence built so far.

## Walkthrough

For `n = 4`:
- Start from `F(0) = 0`, `F(1) = 1`
- Compute `F(2) = 1`
- Compute `F(3) = 2`
- Compute `F(4) = 3`

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- `n = 0`
- `n = 1`

## Common Mistakes

- Using exponential recursion for a simple recurrence
- Off-by-one errors in the loop bounds
- Losing track of which variable is the older versus newer Fibonacci value

## Pattern Transfer

- Rolling DP
- Climbing stairs
- Any recurrence with fixed-width dependency

## Self-Check

- Why are only two variables enough?
- What are the base cases?
- What does each loop iteration compute?

## Function

```python
class Solution:
    def fib(self, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/509-fibonacci-number/python -q
```
