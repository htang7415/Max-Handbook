# 209.Minimum Size Subarray Sum

> Track: `dsa` | Topic: `array`

## Problem in One Line

Find the shortest contiguous subarray whose sum is at least `target`.

## Recognition Cues

- The subarray must be contiguous.
- You need a minimum-length window, not just existence.
- The numbers are positive, so expanding and shrinking a window is safe.

## Baseline Idea

Try every start index and extend until the sum reaches `target`. This works, but it can take `O(n^2)`.

## Core Insight

Because all numbers are positive, once the window sum reaches `target`, moving the left boundary right is the only way to try to make the window shorter.

## Invariant / State

- The current window is `nums[left:right+1]`.
- `window_sum` is the sum of the current window.
- After the inner loop, the window is the smallest one ending at `right` that is still below `target`.

## Walkthrough

For `target = 7`, `nums = [2, 3, 1, 2, 4, 3]`:
- Expand until the sum reaches `8`.
- Shrink from the left to get windows of lengths `4`, then `3`.
- Later reach `[4, 3]`, which has length `2`, the minimum answer.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- No window reaches `target`
- A single element already reaches `target`
- The whole array is required

## Common Mistakes

- Using this sliding-window logic when negative numbers are allowed
- Forgetting to shrink repeatedly while the sum is still large enough
- Updating the answer before the window actually reaches `target`

## Pattern Transfer

- Fixed and variable sliding-window problems
- Longest substring with constraints
- Minimum window style questions

## Self-Check

- Why does positivity make the sliding window valid here?
- When should the left pointer move?
- What does the inner loop guarantee before it stops?

## Function

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/array/209-minimum-size-subarray-sum/python -q
```
