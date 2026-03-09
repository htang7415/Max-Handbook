# 53.Maximum Subarray

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Find the contiguous subarray with the largest sum.

## Recognition Cues

- The subarray must be contiguous.
- Negative prefix sums should be dropped when they stop helping.
- The greedy choice of abandoning a bad prefix matches the optimal answer.

## Baseline Idea

Check every subarray and compute the maximum sum. That works, but it is quadratic or worse.

## Core Insight

If the running sum becomes worse than starting fresh at the current value, discard the previous prefix. The best subarray ending here is either:
- the current value alone
- the previous best ending here plus the current value

## Invariant / State

- `current` is the best subarray sum ending at the current index.
- `best` is the largest subarray sum seen anywhere.

## Walkthrough

For `[-2,1,-3,4,-1,2,1,-5,4]`:
- Early negative prefixes are abandoned
- The segment `[4,-1,2,1]` reaches sum `6`
- That remains the best answer

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- One element
- All negative values
- Large positive run after negative noise

## Common Mistakes

- Resetting to `0` and breaking all-negative inputs
- Confusing subarray with subsequence
- Returning the final running sum instead of the global best

## Pattern Transfer

- Kadane-style greedy/DP hybrids
- Rolling best-ending-here reasoning
- 53 DP variant in the other topic

## Self-Check

- Why can a harmful prefix be dropped safely?
- What does `current` represent?
- Why must all-negative arrays still return a negative number?

## Function

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/53-maximum-subarray/python -q
```
