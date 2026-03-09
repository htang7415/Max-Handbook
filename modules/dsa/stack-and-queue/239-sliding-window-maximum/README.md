# 239.Sliding Window Maximum

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Return the maximum value in every sliding window of size `k`.

## Recognition Cues

- A fixed-size window moves one step at a time.
- You need the maximum for every window, not just one.
- Recomputing the maximum from scratch wastes work.

## Baseline Idea

For each window, scan its `k` elements and take the max. That works, but it takes `O(nk)`.

## Core Insight

Keep a decreasing deque of indices. The front always stores the index of the current window maximum.

## Invariant / State

- Indices in the deque are inside the current window.
- Their values are in decreasing order from front to back.
- The front index is the max of the current window.

## Walkthrough

For `[1, 3, -1, -3, 5, 3, 6, 7]` with `k = 3`:
- Build the first window deque so `3` is at the front.
- As the window moves, remove expired indices and smaller trailing values.
- Each step exposes the new maximum at the deque front.

## Complexity

- Time: `O(n)`
- Space: `O(k)`

## Edge Cases

- `k = 1`
- All values equal
- Strictly decreasing input

## Common Mistakes

- Storing values instead of indices
- Forgetting to evict indices outside the window
- Removing larger values instead of smaller trailing ones

## Pattern Transfer

- 739.Daily Temperatures
- Monotonic deque problems
- Fixed-window optimization

## Self-Check

- Why are indices needed instead of values?
- Why is the deque decreasing?
- What does the deque front guarantee?

## Function

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/239-sliding-window-maximum/python -q
```
