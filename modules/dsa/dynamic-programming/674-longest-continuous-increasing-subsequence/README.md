# 674.Longest Continuous Increasing Subsequence

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the length of the longest contiguous strictly increasing run.

## Recognition Cues

- The sequence must be contiguous.
- Each position depends only on whether it is larger than the previous value.
- A rolling run length is enough.

## Baseline Idea

Check every subarray and keep the longest one that stays strictly increasing. That works, but it does too much repeated scanning.

## Core Insight

Track the length of the current increasing run. If `nums[i] > nums[i - 1]`, extend the run; otherwise reset it to `1`.

## Invariant / State

- `current` is the length of the increasing run ending at the current index.
- `best` is the maximum run length seen so far.

## Walkthrough

For `[1, 3, 5, 4, 7]`:
- `1, 3, 5` grows the run to length `3`
- `4` breaks it, so reset to `1`
- `7` starts a new run of length `2`
- The best answer stays `3`

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty array
- All equal values
- Strictly increasing array

## Common Mistakes

- Confusing contiguous increasing subsequence with LIS
- Using `>=` instead of `>`
- Forgetting to reset the run length when the increase breaks

## Pattern Transfer

- Rolling DP on contiguous segments
- 300.Longest Increasing Subsequence for the non-contiguous variant
- One-pass run tracking

## Self-Check

- Why is contiguity what makes the state so small?
- What does `current` represent?
- How does this differ from LIS?

## Function

```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/674-longest-continuous-increasing-subsequence/python -q
```
