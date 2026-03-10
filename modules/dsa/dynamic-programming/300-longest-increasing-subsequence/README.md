# 300.Longest Increasing Subsequence

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the length of the longest strictly increasing subsequence.

## Recognition Cues

- Order matters, but the subsequence does not need to be contiguous.
- You want the length only, not the actual subsequence.
- Replacing larger tails with smaller values can keep future options open.

## Baseline Idea

Enumerate subsequences recursively and keep the longest increasing one. That works, but the branching factor is too large.

## Core Insight

Maintain `tails`, where `tails[length - 1]` is the smallest possible tail value of an increasing subsequence of that length. For each number, binary search the first tail it can replace.

## Invariant / State

- `tails` stays sorted.
- Replacing a tail with a smaller value never hurts a future longer subsequence.

## Walkthrough

For `[10, 9, 2, 5, 3, 7, 101, 18]`:
- Start with `tails = []`.
- Insert `10`, then replace it with `9`, then with `2`, keeping the best tail for length `1`.
- Extend to `[2, 3, 7, 18]`, so the LIS length is `4`.

## Complexity

- Time: `O(n log n)`
- Space: `O(n)`

## Edge Cases

- Empty array
- All equal values
- Strictly decreasing array

## Common Mistakes

- Confusing subsequence with subarray
- Using `bisect_right` and allowing duplicates into a strictly increasing subsequence
- Assuming `tails` stores the actual LIS rather than the best tail values

## Pattern Transfer

- 674.Longest Continuous Increasing Subsequence for the contiguous variant
- Patience sorting style sequence problems
- Binary search over monotone helper state

## Self-Check

- What does `tails[i]` represent?
- Why is replacing a larger tail with a smaller one safe?
- Why does binary search apply here?

## Function

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/300-longest-increasing-subsequence/python -q
```
