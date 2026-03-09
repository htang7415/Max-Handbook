# 583.Delete Operation for Two Strings

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Return the minimum number of deletions needed to make the two strings equal.

## Recognition Cues

- Only deletions are allowed.
- The common part you want to keep is a shared subsequence.
- The longest common subsequence gives the maximum kept overlap.

## Baseline Idea

Try deleting characters from either side recursively until the strings match. That works, but overlapping subproblems make it slow.

## Core Insight

If the longest common subsequence has length `L`, then:
- `word1` must delete `len(word1) - L` characters
- `word2` must delete `len(word2) - L` characters

So the answer is `len(word1) + len(word2) - 2 * L`.

## Invariant / State

- `dp[i][j]` stores the LCS length for `word1[:i]` and `word2[:j]`.

## Walkthrough

For `"sea"` and `"eat"`:
- The LCS is `"ea"` with length `2`.
- `"sea"` deletes `1` character.
- `"eat"` deletes `1` character.
- Total deletions: `2`.

## Complexity

- Time: `O(mn)`
- Space: `O(mn)`

## Edge Cases

- One empty string
- No common subsequence
- Strings already equal

## Common Mistakes

- Recomputing deletions directly instead of using the LCS shortcut
- Confusing subsequence with substring
- Forgetting the extra zero row and column for empty prefixes

## Pattern Transfer

- 1143.Longest Common Subsequence
- Transform-one-string problems
- Keep-the-overlap reasoning

## Self-Check

- Why does the LCS tell you what to keep?
- How do deletions relate to LCS length?
- What does `dp[i][j]` mean here?

## Function

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/583-delete-operation-for-two-strings/python -q
```
