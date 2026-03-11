# 459.Repeated Substring Pattern

> Track: `dsa` | Topic: `string`

## Problem in One Line

Decide whether the string can be built by repeating one of its proper substrings.

## Recognition Cues

- The question is about a whole-string repetition pattern.
- You only need a yes/no answer.
- Prefix/suffix structure matters more than checking every candidate substring directly.

## Baseline Idea

Try every substring length that divides `len(s)` and test whether repeating it reconstructs the string. That works, but it is more manual.

## Core Insight

If a string is built from a repeating unit, then its longest proper prefix that is also a suffix reveals that period. KMP's `lps` table makes that check direct.

## Invariant / State

- `lps[i]` stores the longest proper prefix of `s[:i+1]` that is also a suffix.
- If `lps[-1] = k`, then the candidate repeating block length is `n - k`.

## Why This Works

- If `s` is made by repeating some block of length `p`, then the whole string has a prefix-suffix overlap of length `n - p`.
- So the final `lps` value exposes how much of the string matches itself after a shift.
- If `k = lps[-1]`, then `n - k` is the shortest candidate period consistent with that overlap.
- The extra divisibility check matters because overlap alone is not enough. The block must tile the full string exactly, so `n % (n - k) == 0`.

## Walkthrough

For `"abab"`:
- Build `lps = [0, 0, 1, 2]`.
- The longest proper prefix/suffix length is `2`.
- The candidate block length is `4 - 2 = 2`, and `4 % 2 == 0`, so the pattern repeats.

## Complexity

- Time: `O(n)`
- Space: `O(n)` for the `lps` table

## Edge Cases

- Empty string
- Single character
- Strings made of one repeated character

## Common Mistakes

- Treating any nonzero prefix/suffix match as enough without checking divisibility
- Building the `lps` table incorrectly on mismatch fallback
- Treating a single character as a repeated pattern

## Pattern Transfer

- 28.Implement strStr()
- KMP prefix-function problems
- String periodicity checks

## Self-Check

- What does `lps[-1]` tell you about the whole string?
- Why is the candidate period length `n - lps[-1]`?
- Why must that candidate period divide the full length exactly?

## Function

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
```

## Run tests

```bash
pytest modules/dsa/string/459-repeated-substring-pattern/python -q
```
