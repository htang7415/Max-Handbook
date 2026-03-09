# 647.Palindromic Substrings

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many substrings of the string are palindromes.

## Recognition Cues

- Every palindrome has a center.
- Both odd-length and even-length palindromes matter.
- Expanding around centers gives a direct count without a DP table.

## Baseline Idea

Check every substring and test whether it is a palindrome. That works, but it rescans characters repeatedly.

## Core Insight

Treat each index as:
- the center of an odd palindrome
- the left center of an even palindrome

Expand outward while the characters match, counting every valid expansion.

## Invariant / State

- Each `expand(left, right)` call counts exactly the palindromic substrings centered at that pair.

## Walkthrough

For `"aaa"`:
- Center at index `0` gives `"a"`
- Center at index `1` gives `"a"` and `"aaa"`
- Even centers give `"aa"` twice
- Total count is `6`

## Complexity

- Time: `O(n^2)`
- Space: `O(1)`

## Edge Cases

- Empty string
- One character
- All characters the same

## Common Mistakes

- Counting only odd-length palindromes
- Missing overlapping palindromes with the same center
- Confusing subsequences with substrings

## Pattern Transfer

- Center-expansion palindrome problems
- 5.Longest Palindromic Substring
- Symmetric two-pointer expansion

## Self-Check

- Why does every palindrome have a center representation?
- Why do we need both odd and even centers?
- What does one expansion step add to the count?

## Function

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/647-palindromic-substrings/python -q
```
