# 704.Binary Search

> Track: `dsa` | Topic: `array`

## Problem in One Line

Find the index of `target` in a sorted array, or return `-1` if it is missing.

## Recognition Cues

- The input array is already sorted.
- You need faster than a linear scan.
- The answer depends on comparing against a middle value and discarding half.

## Baseline Idea

Scan from left to right until you find the target. This works, but it takes `O(n)` time.

## Core Insight

At each step, compare the middle value with `target`. Because the array is sorted, one half can be discarded immediately.

## Invariant / State

If the target exists, it is always inside the current closed interval `[left, right]`.

## Walkthrough

For `nums = [-1, 0, 3, 5, 9, 12]` and `target = 9`:
- `mid = 2`, value `3`, so search the right half.
- `mid = 4`, value `9`, so return index `4`.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Edge Cases

- Empty array
- Single-element array
- Target at the first or last index
- Target not present

## Common Mistakes

- Mixing closed-interval and half-open interval updates
- Using the wrong loop condition
- Forgetting to move past `mid` after a comparison

## Pattern Transfer

- Search Insert Position
- First Bad Version
- Find First and Last Position of Element in Sorted Array

## Self-Check

- Why does sorted order let you discard half of the search space?
- What does `[left, right]` mean in this implementation?
- Why do the boundary updates use `mid - 1` and `mid + 1`?

## Function

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/array/704-binary-search/python -q
```
