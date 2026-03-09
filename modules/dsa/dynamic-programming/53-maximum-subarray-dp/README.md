# 53.Maximum Subarray (DP)

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the contiguous subarray with the largest possible sum.

## Recognition Cues

- The subarray must be contiguous.
- You want the best running segment, not an arbitrary subset.
- The best subarray ending at the current position depends only on the previous one.

## Baseline Idea

Check every subarray and compute its sum. That works, but it is quadratic or worse.

## Core Insight

At each value, either:
- start a new subarray here
- extend the best subarray ending at the previous index

This is Kadane's algorithm as a rolling DP.

## Invariant / State

- `current` is the best subarray sum that must end at the current index.
- `best` is the largest subarray sum seen anywhere so far.

## Walkthrough

For `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:
- Negative prefixes are dropped when they hurt the running sum.
- The segment `[4, -1, 2, 1]` accumulates to `6`.
- No later segment beats that sum.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- One element
- All negative numbers
- Large positive run after an early negative prefix

## Common Mistakes

- Confusing subarray with subsequence
- Resetting the running sum to `0` and breaking all-negative cases
- Returning the last running sum instead of the global best

## Pattern Transfer

- Rolling DP
- Greedy/DP hybrid reasoning
- 674.Longest Continuous Increasing Subsequence

## Self-Check

- What does `current` represent?
- Why can a negative running prefix be abandoned?
- Why must all-negative arrays still return the least negative element?

## Function

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/53-maximum-subarray-dp/python -q
```
