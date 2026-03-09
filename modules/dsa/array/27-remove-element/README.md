# 27.Remove Element

> Track: `dsa` | Topic: `array`

## Problem in One Line

Remove every occurrence of `val` from the array in place and return the new valid length.

## Recognition Cues

- The array may be reordered beyond the returned length.
- You only need the new length and the kept prefix.
- In-place overwrite is better than repeated deletion.

## Baseline Idea

Shift the array left every time you find `val`. That works, but repeated shifting can take `O(n^2)`.

## Core Insight

Use a fast pointer to scan every element and a slow pointer to write back only the elements that should stay.

## Invariant / State

- `nums[:slow]` always contains the kept elements seen so far.
- `fast` scans the next unread value.

## Walkthrough

For `nums = [3, 2, 2, 3]`, `val = 3`:
- Skip the first `3`.
- Keep `2`, write it to index `0`.
- Keep the next `2`, write it to index `1`.
- Skip the final `3`.
- Return `2`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- No element matches `val`
- Every element matches `val`
- Single-element input

## Common Mistakes

- Incrementing `slow` even when the current value should be removed
- Assuming values beyond the returned length still matter
- Trying to delete elements instead of overwrite them

## Pattern Transfer

- 344.Reverse String
- 977.Squares of a Sorted Array
- In-place array compaction patterns

## Self-Check

- What does `nums[:slow]` mean at any point?
- Why is overwrite enough without actual deletion?
- Why do values after index `slow - 1` not matter?

## Function

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/array/27-remove-element/python -q
```
