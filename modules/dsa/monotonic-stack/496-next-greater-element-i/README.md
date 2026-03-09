# 496.Next Greater Element I

> Track: `dsa` | Topic: `monotonic-stack`

## Problem in One Line

For each value in `nums1`, find the first greater value to its right in `nums2`.

## Recognition Cues

- You want the next greater element to the right.
- Many queries depend on the same reference array `nums2`.
- Precomputing answers once is better than scanning from scratch for each query.

## Baseline Idea

For each value in `nums1`, find its position in `nums2` and scan right until a larger value appears. That can take `O(len(nums1) * len(nums2))`.

## Core Insight

Use a decreasing monotonic stack while scanning `nums2`. When a larger number appears, it resolves the next-greater answer for one or more smaller numbers on the stack.

## Invariant / State

- The stack stores values from `nums2` whose next greater element has not been found yet.
- Values in the stack are in decreasing order.
- `next_greater[x]` stores the resolved answer for value `x`.

## Walkthrough

For `nums2 = [1, 3, 4, 2]`:
- `1` waits on the stack.
- `3` resolves `1`.
- `4` resolves `3`.
- `2` has no larger value afterward, so its answer is `-1`.

## Complexity

- Time: `O(len(nums1) + len(nums2))`
- Space: `O(len(nums2))`

## Edge Cases

- A queried value has no greater value
- `nums1` contains one value
- The next greater value appears immediately

## Common Mistakes

- Storing indices when the mapping is by value
- Forgetting to fill unresolved stack values with `-1`
- Scanning `nums2` separately for each query

## Pattern Transfer

- 739.Daily Temperatures
- 503.Next Greater Element II
- Next-greater monotonic stack problems

## Self-Check

- Why can one scan of `nums2` answer all queries?
- What order do values have in the stack?
- Why is each value pushed and popped at most once?

## Function

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/monotonic-stack/496-next-greater-element-i/python -q
```
