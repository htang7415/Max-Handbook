# 541.Reverse String II

> Track: `dsa` | Topic: `string`

## Problem in One Line

For every block of `2k` characters, reverse the first `k` characters.

## Recognition Cues

- The operation repeats in fixed-size blocks.
- You only reverse part of each block.
- The last block may be shorter than `2k`.

## Baseline Idea

Slice the string into many temporary substrings and rebuild it block by block. That works, but pointer-based reversal on a character list is more direct.

## Core Insight

Walk in steps of `2k`, and reverse only the range `[start, start + k - 1]` within each block, clipped to the string length.

## Invariant / State

- `start` is the first index of the current `2k` block.
- The reversal range is always from `start` to `min(start + k - 1, len(chars) - 1)`.

## Walkthrough

For `"abcdefg"`, `k = 2`:
- Reverse `"ab"` to get `"bacdefg"`.
- Skip `"cd"`.
- Reverse `"ef"` to get `"bacdfeg"`.
- The final `"g"` stays as is.

## Complexity

- Time: `O(n)`
- Space: `O(n)` in Python due to character list conversion

## Edge Cases

- String shorter than `k`
- Final block length between `k` and `2k`
- `k = 1`

## Common Mistakes

- Reversing the whole `2k` block instead of just the first `k`
- Going out of bounds on the final block
- Forgetting to advance by `2k`

## Pattern Transfer

- 344.Reverse String
- Block-based string manipulation
- Two-pointer in-place reversal

## Self-Check

- Which part of each `2k` block is reversed?
- Why do we use `min(...)` for the right boundary?
- What happens when fewer than `k` characters remain?

## Function

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
```

## Run tests

```bash
pytest modules/dsa/string/541-reverse-string-ii/python -q
```
