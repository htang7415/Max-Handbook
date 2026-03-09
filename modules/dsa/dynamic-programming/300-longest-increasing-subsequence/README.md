# 300.Longest Increasing Subsequence

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the length of the longest strictly increasing subsequence.

## Recognition Cues

- Order matters, but the subsequence does not need to be contiguous.
- Each position can extend earlier smaller values.
- The `O(n^2)` DP focuses on subsequences ending at each index.

## Baseline Idea

Enumerate subsequences recursively and keep the longest increasing one. That works, but the branching factor is too large.

## Core Insight

Let `dp[i]` be the LIS length ending exactly at index `i`. To compute it, inspect all earlier indices `j < i`; if `nums[j] < nums[i]`, then `nums[i]` can extend the subsequence ending at `j`.

## Invariant / State

- `dp[i]` is the best increasing subsequence length that must end at `nums[i]`.

## Walkthrough

For `[10, 9, 2, 5, 3, 7, 101, 18]`:
- `2` starts a subsequence of length `1`.
- `5` extends `2` to length `2`.
- `7` extends the best earlier smaller value to length `3`.
- `101` extends again to length `4`.

## Complexity

- Time: `O(n^2)`
- Space: `O(n)`

## Edge Cases

- Empty array
- All equal values
- Strictly decreasing array

## Common Mistakes

- Confusing subsequence with subarray
- Using `<=` instead of `<` for strict increase
- Forgetting that the final answer is `max(dp)`, not just `dp[-1]`

## Pattern Transfer

- 674.Longest Continuous Increasing Subsequence for the contiguous variant
- Sequence DP by ending position
- 1143-style state definitions on prefixes/endpoints

## Self-Check

- What does `dp[i]` represent?
- Why can `nums[i]` only extend earlier smaller values?
- Why is the answer not always at the last index?

## Function

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/300-longest-increasing-subsequence/python -q
```
