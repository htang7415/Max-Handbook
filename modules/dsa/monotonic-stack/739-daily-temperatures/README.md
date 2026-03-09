# 739.Daily Temperatures

> Track: `dsa` | Topic: `monotonic-stack`

## Problem in One Line

For each day, compute how many days you must wait to see a warmer temperature.

## Recognition Cues

- Each position wants the next greater value to the right.
- You need answers for every index, not just one.
- Revisiting earlier unresolved indices is useful.

## Baseline Idea

For each day, scan forward until you find a warmer day. This works, but it takes `O(n^2)` in the worst case.

## Core Insight

Keep a stack of indices whose warmer day has not been found yet. When a higher temperature arrives, it resolves one or more earlier indices immediately.

## Invariant / State

- The stack stores indices in decreasing temperature order.
- Every index in the stack is still waiting for its next warmer day.

## Walkthrough

For `[73, 74, 75, 71, 69, 72, 76, 73]`:
- `73` waits on the stack.
- `74` resolves `73` with wait `1`.
- `75` resolves `74` with wait `1`.
- `72` later resolves `69` and `71`.
- `76` resolves several remaining indices at once.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- Empty input
- Strictly decreasing temperatures
- Repeated temperatures

## Common Mistakes

- Storing temperatures instead of indices
- Forgetting that equal temperatures do not count as warmer
- Updating answers without removing resolved indices

## Pattern Transfer

- 496.Next Greater Element I
- 503.Next Greater Element II
- 84.Largest Rectangle in Histogram

## Self-Check

- Why do we store indices instead of values?
- What order do temperatures have inside the stack?
- Why is each index pushed and popped at most once?

## Function

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/monotonic-stack/739-daily-temperatures/python -q
```
