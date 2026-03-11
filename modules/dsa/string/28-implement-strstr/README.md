# 28.Implement strStr()

> Track: `dsa` | Topic: `string`

## Problem in One Line

Return the starting index of the first occurrence of `needle` inside `haystack`.

## Recognition Cues

- You need substring matching.
- The answer is the first valid starting index.
- Repeated prefix/suffix structure can be reused after a mismatch.

## Baseline Idea

Try every starting index and compare the next `len(needle)` characters. That works, but it repeats work after mismatches.

## Core Insight

KMP preprocesses `needle` so a mismatch can jump to the longest reusable prefix instead of restarting from scratch.

## Invariant / State

- `lps[i]` stores the length of the longest proper prefix of `needle[:i+1]` that is also a suffix.
- `needle_index` is how many characters of `needle` currently match the suffix of the scanned `haystack` prefix.

## Why This Works

- When a mismatch happens after matching some prefix of `needle`, you do not need to restart from zero if part of that matched block is also a suffix.
- `lps[i]` tells you the longest prefix you can keep after failing at position `i`.
- So KMP never throws away reusable prefix information. It shifts the pattern to the largest position that is still consistent with what was already matched.
- That is why characters in `haystack` are not re-scanned from scratch, giving linear-time matching.

## Walkthrough

For `haystack = "hello"` and `needle = "ll"`:
- Build `lps = [0, 1]` for `"ll"`.
- Scan `"hello"` left to right while tracking the current matched prefix length.
- When the second `l` is matched, the full pattern is found and the answer is `2`.

## Complexity

- Time: `O(n + m)`
- Space: `O(m)` for the `lps` table

## Edge Cases

- Empty `needle`
- `needle` longer than `haystack`
- Overlapping matches such as `"aaa"` and `"aa"`

## Common Mistakes

- Forgetting that an empty `needle` returns `0`
- Building the `lps` table incorrectly on repeated prefixes
- Resetting to the start of `needle` instead of falling back with `lps`

## Pattern Transfer

- 459.Repeated Substring Pattern
- KMP-based string matching
- Find First Occurrence in a String

## Self-Check

- What does `lps[i]` mean?
- What should happen when `needle` is empty?
- Why does KMP avoid re-checking characters after a mismatch?

## Function

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/string/28-implement-strstr/python -q
```
