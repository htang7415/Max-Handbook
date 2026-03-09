# 459.Repeated Substring Pattern

> Track: `dsa` | Topic: `string`

## Problem in One Line

Decide whether the string can be built by repeating one of its proper substrings.

## Recognition Cues

- The question is about a whole-string repetition pattern.
- You only need a yes/no answer.
- A structural string trick may be simpler than checking every substring manually.

## Baseline Idea

Try every substring length that divides `len(s)` and test whether repeating it reconstructs the string. That works, but it is more manual.

## Core Insight

If `s` is made of repeated pieces, then `s` appears inside `(s + s)[1:-1]`. Non-repeating strings do not.

## Invariant / State

- `doubled = s + s` contains every cyclic shift of `s`.
- Removing the first and last characters prevents matching the original string trivially at the ends.

## Walkthrough

For `"abab"`:
- `doubled = "abababab"`.
- `doubled[1:-1] = "bababa"`.
- `"abab"` appears inside that substring, so the pattern repeats.

## Complexity

- Time: depends on substring search, typically linear-ish in practice for this built-in approach
- Space: `O(n)` for the doubled string

## Edge Cases

- Empty string
- Single character
- Strings made of one repeated character

## Common Mistakes

- Forgetting to remove the first and last characters
- Treating the empty string as repeating
- Assuming any repeated character implies a repeated substring pattern

## Pattern Transfer

- 28.Implement strStr()
- KMP-style periodicity checks
- String rotation/repetition tricks

## Self-Check

- Why do we slice to `doubled[1:-1]`?
- Why does a repeating string reappear inside the doubled middle section?
- Why does a single-character string return `False`?

## Function

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
```

## Run tests

```bash
pytest modules/dsa/string/459-repeated-substring-pattern/python -q
```
