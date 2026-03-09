# 28.Implement strStr()

> Track: `dsa` | Topic: `string`

## Problem in One Line

Return the starting index of the first occurrence of `needle` inside `haystack`.

## Recognition Cues

- You need substring matching.
- The answer is the first valid starting index.
- A sliding comparison over the string is enough for the basic solution.

## Baseline Idea

Try every starting index and compare the next `len(needle)` characters. This is the straightforward solution for the basic version.

## Core Insight

Only positions where `needle` fully fits can be valid starts, so compare `haystack[i:i+m]` against `needle` for each such index.

## Invariant / State

- `i` is the current candidate starting index.
- The search only needs to examine `0` through `n - m`.

## Walkthrough

For `haystack = "hello"` and `needle = "ll"`:
- Try index `0`: `"he"` does not match.
- Try index `1`: `"el"` does not match.
- Try index `2`: `"ll"` matches, so return `2`.

## Complexity

- Time: `O((n - m + 1) * m)` in the simple scan
- Space: `O(1)` auxiliary space

## Edge Cases

- Empty `needle`
- `needle` longer than `haystack`
- Overlapping matches such as `"aaa"` and `"aa"`

## Common Mistakes

- Forgetting that an empty `needle` returns `0`
- Iterating too far and reading past the valid start range
- Returning the last match instead of the first match

## Pattern Transfer

- 459.Repeated Substring Pattern
- KMP-based string matching
- Find First Occurrence in a String

## Self-Check

- Why is the last valid start index `n - m`?
- What should happen when `needle` is empty?
- Why do overlapping matches still work with the simple scan?

## Function

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/string/28-implement-strstr/python -q
```
