# 344.Reverse String

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Reverse the character array in place.

## Recognition Cues

- The input is mutable and must be changed in place.
- You only need to swap elements symmetrically.
- Extra arrays are unnecessary.

## Baseline Idea

Create a reversed copy and write it back. That is simple, but it uses extra space.

## Core Insight

The first and last characters should swap, then the second and second-last, and so on until the pointers meet.

## Invariant / State

- `left` points to the next character that belongs near the end.
- `right` points to the next character that belongs near the front.
- Everything outside `[left, right]` is already in its final position.

## Walkthrough

For `["h", "e", "l", "l", "o"]`:
- Swap `h` and `o`.
- Swap `e` and `l`.
- Stop when the pointers meet in the middle.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty array
- Single character
- Even-length string

## Common Mistakes

- Forgetting that the function should modify the input in place
- Moving only one pointer after a swap
- Looping one step too far

## Pattern Transfer

- 27.Remove Element
- 151.Reverse Words in a String
- 977.Squares of a Sorted Array

## Self-Check

- Why is no extra array needed?
- What part of the array is guaranteed correct after each swap?
- Why does the loop stop at `left < right`?

## Function

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/344-reverse-string/python -q
```
