# 977.Squares of a Sorted Array

> Track: `dsa` | Topic: `array`

## Problem in One Line

Return the squares of the sorted array in nondecreasing order.

## Recognition Cues

- The input is already sorted, but squaring negative numbers breaks that order.
- The largest square must come from one of the ends.
- A second sorted pass is avoidable.

## Baseline Idea

Square every value, then sort the result. That works, but it takes `O(n log n)`.

## Core Insight

Compare absolute values at the left and right ends. Write the larger square into the result from back to front.

## Invariant / State

- `left` and `right` bound the unread part of the input.
- `write` points to the next largest square position in the output.
- Everything after `write` is already in final sorted order.

## Walkthrough

For `[-4, -1, 0, 3, 10]`:
- Compare `-4` and `10`, write `100`.
- Compare `-4` and `3`, write `16`.
- Continue until the result becomes `[0, 1, 9, 16, 100]`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- All negative values
- All nonnegative values
- Zeros in the middle

## Common Mistakes

- Forgetting that the largest square can come from the left end
- Filling the result from front to back
- Comparing raw values instead of squared magnitudes

## Pattern Transfer

- 344.Reverse String
- 27.Remove Element
- Two-ended array processing

## Self-Check

- Why are the array ends the only candidates for the next largest square?
- Why is the output filled from right to left?
- When does the left pointer move versus the right pointer?

## Function

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/array/977-squares-of-a-sorted-array/python -q
```
