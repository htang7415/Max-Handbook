# 503.Next Greater Element II

> Track: `dsa` | Topic: `monotonic-stack`

## Problem in One Line

For each index in a circular array, find the next greater value encountered while wrapping around.

## Recognition Cues

- This is a next-greater-element problem with wraparound.
- A value may need to look past the end of the array.
- Circular behavior can often be simulated by scanning twice.

## Baseline Idea

For each index, scan forward and wrap around until you return to the start. That works, but it can take `O(n^2)`.

## Core Insight

Use the same monotonic-stack idea as standard next-greater problems, but iterate through the array twice so early elements can find greater values near the front after wrapping.

## Invariant / State

- The stack stores indices whose next greater value is still unresolved.
- `result[idx]` is filled the first time a larger value is seen during the doubled scan.

## Walkthrough

For `[1, 2, 1]`:
- `2` resolves the first `1`.
- The last `1` has no greater value to its right in the first pass.
- During the wraparound pass, it sees `2`, so its answer becomes `2`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- All values equal
- Strictly decreasing array
- Single element

## Common Mistakes

- Pushing indices during the second pass and duplicating work
- Forgetting that unresolved answers stay `-1`
- Treating the array as linear instead of circular

## Pattern Transfer

- 496.Next Greater Element I
- 739.Daily Temperatures
- Circular array monotonic stack problems

## Self-Check

- Why is scanning twice enough for circularity?
- Why are indices only pushed during the first pass?
- When does an answer remain `-1`?

## Function

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/monotonic-stack/503-next-greater-element-ii/python -q
```
