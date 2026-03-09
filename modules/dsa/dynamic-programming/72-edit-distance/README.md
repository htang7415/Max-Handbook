# 72.Edit Distance

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Return the minimum number of insertions, deletions, and replacements needed to turn one word into another.

## Recognition Cues

- Three edit operations are allowed.
- The problem compares all prefixes of two strings.
- A 2D DP table naturally captures the best cost for every prefix pair.

## Baseline Idea

Recursively try all valid edits and keep the minimum count. That works, but the same prefix pairs are revisited many times.

## Core Insight

Let `dp[i][j]` be the minimum edits to convert `word1[:i]` into `word2[:j]`. If the last characters match, no new edit is needed; otherwise choose the best among delete, insert, and replace.

## Invariant / State

- `dp[i][j]` is the optimal edit distance between the two prefixes.

## Walkthrough

For `"horse"` and `"ros"`:
- Replace `h` with `r`
- Delete one extra character
- Delete another extra character
- Total edit distance is `3`

## Complexity

- Time: `O(mn)`
- Space: `O(mn)`

## Edge Cases

- One empty string
- Identical strings
- Completely different strings

## Common Mistakes

- Mixing up insert and delete directions
- Forgetting base cases for empty prefixes
- Using LCS-style transitions when replacement is allowed

## Pattern Transfer

- Two-string DP
- 583.Delete Operation for Two Strings
- Prefix-edit state tables

## Self-Check

- What does `dp[i][j]` mean?
- Why do empty-prefix rows and columns have simple linear values?
- Which three transitions are considered on a mismatch?

## Function

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/72-edit-distance/python -q
```
