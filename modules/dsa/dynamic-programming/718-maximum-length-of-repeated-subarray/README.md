# 718.Maximum Length of Repeated Subarray

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the longest contiguous subarray that appears in both arrays.

## Recognition Cues

- The match must be contiguous in both arrays.
- This is closer to longest common substring than longest common subsequence.
- Matching endpoints can extend a previous diagonal match.

## Baseline Idea

Try every pair of starting positions and extend while values match. That works, but it repeats overlapping comparisons.

## Core Insight

Let `dp[i][j]` be the length of the longest common suffix ending at `nums1[i - 1]` and `nums2[j - 1]`. If those values match, extend the diagonal by one; otherwise the common suffix length is zero.

## Invariant / State

- `dp[i][j]` stores the repeated-subarray length ending exactly at those two positions.

## Walkthrough

For `[1, 2, 3, 2, 1]` and `[3, 2, 1, 4, 7]`:
- The repeated contiguous segment `[3, 2, 1]` appears in both arrays.
- The diagonal matches build up to length `3`.

## Complexity

- Time: `O(mn)`
- Space: `O(mn)`

## Edge Cases

- One empty array
- No common subarray
- Many repeated equal values

## Common Mistakes

- Confusing repeated subarray with subsequence
- Forgetting to reset to `0` on a mismatch
- Returning the last DP cell instead of the global maximum

## Pattern Transfer

- Longest common substring style DP
- 1143 LCS for the non-contiguous variant
- DP on matching suffixes

## Self-Check

- Why does a mismatch force the DP value to zero?
- What does `dp[i][j]` mean?
- How is this different from LCS?

## Function

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/718-maximum-length-of-repeated-subarray/python -q
```
