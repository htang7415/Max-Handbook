# 392.Is Subsequence

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Decide whether `s` appears inside `t` as a subsequence.

## Recognition Cues

- Characters of `s` must appear in order inside `t`.
- Characters do not need to be adjacent.
- A single pass through `t` is enough for one query.

## Baseline Idea

Try every subsequence of `t` and check whether any of them equals `s`. That works conceptually, but it is wildly inefficient.

## Core Insight

Scan through `t` once with a pointer into `s`. Whenever the current character of `t` matches the next needed character of `s`, advance the pointer. If the pointer reaches the end of `s`, then `s` is a subsequence.

## Invariant / State

- `i` is the number of characters from the front of `s` already matched in order.

## Walkthrough

For `s = "abc"` and `t = "ahbgdc"`:
- Match `a`
- Skip `h`
- Match `b`
- Skip `g`, `d`
- Match `c`
- All characters in `s` were matched in order

## Complexity

- Time: `O(len(t))`
- Space: `O(1)`

## Edge Cases

- Empty `s`
- `s` longer than `t`
- Repeated characters in `s`

## Common Mistakes

- Confusing subsequence with substring
- Advancing the `s` pointer when characters do not match
- Overcomplicating a single-query problem with DP

## Pattern Transfer

- Two-pointer sequence matching
- 1143.Longest Common Subsequence for the general DP version
- Stream matching over one pass

## Self-Check

- What does pointer `i` represent?
- Why does one left-to-right scan of `t` suffice?
- What makes subsequence different from substring?

## Function

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/392-is-subsequence/python -q
```
