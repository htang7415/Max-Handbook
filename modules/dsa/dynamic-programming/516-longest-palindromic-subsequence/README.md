# 516.Longest Palindromic Subsequence

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the length of the longest subsequence of the string that is also a palindrome.

## Recognition Cues

- The answer depends on matching characters at both ends of a substring.
- Characters inside the ends form a smaller version of the same problem.
- This is interval DP over substring boundaries.

## Baseline Idea

Try every subsequence and test whether it is a palindrome. That works, but it is exponential.

## Core Insight

Let `dp[i][j]` be the longest palindromic subsequence length inside `s[i:j+1]`. If `s[i] == s[j]`, those characters can wrap the best answer from inside; otherwise, drop one end and take the better result.

## Invariant / State

- `dp[i][j]` stores the best palindromic subsequence length for the closed interval `[i, j]`.

## Walkthrough

For `"bbbab"`:
- Matching outer `b` characters can wrap a smaller interior solution.
- The best answer becomes `4`, from `"bbbb"` as a subsequence.

## Complexity

- Time: `O(n^2)`
- Space: `O(n^2)`

## Edge Cases

- Empty string
- One character
- No repeated characters

## Common Mistakes

- Confusing subsequence with substring
- Filling the interval DP in the wrong order
- Forgetting the base case `dp[i][i] = 1`

## Pattern Transfer

- Interval DP
- 647.Palindromic Substrings
- 1143-style two-end recurrence thinking

## Self-Check

- What does `dp[i][j]` mean?
- Why must `i` move backward when filling the table?
- When characters do not match, why is the answer `max(dp[i+1][j], dp[i][j-1])`?

## Function

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/516-longest-palindromic-subsequence/python -q
```
