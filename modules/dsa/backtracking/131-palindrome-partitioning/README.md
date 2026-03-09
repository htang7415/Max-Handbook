# 131.Palindrome Partitioning

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Split the string into all possible lists of palindromic substrings.

## Recognition Cues

- You need all valid cuts of a string.
- Each chosen segment must satisfy a property, here being a palindrome.
- Backtracking over end positions is natural.

## Baseline Idea

Generate all partitions of the string and check each segment afterward. That works, but it explores many invalid branches.

## Core Insight

At position `start`, try every end position. Recurse only when `s[start:end+1]` is a palindrome.

## Invariant / State

- `path` stores the palindromic segments chosen so far.
- `start` is the next index to partition.
- Reaching `start == len(s)` means the whole string has been partitioned validly.

## Walkthrough

For `"aab"`:
- Choose `"a"`, then `"a"`, then `"b"` to get `["a", "a", "b"]`.
- Backtrack and choose `"aa"`, then `"b"` to get `["aa", "b"]`.

## Complexity

- Time: exponential in the number of partitions
- Space: `O(n)` recursion depth, excluding the output

## Edge Cases

- Empty string
- One character
- Strings with many palindromic overlaps like `"aaa"`

## Common Mistakes

- Accepting non-palindromic segments
- Forgetting to copy the current path
- Treating every substring choice as valid

## Pattern Transfer

- 93.Restore IP Addresses
- Backtracking with validity predicates
- String segmentation search

## Self-Check

- What does the palindrome test prune?
- When is a partition complete?
- Why can the same prefix lead to multiple valid partitions?

## Function

```python
class Solution:
    def partition(self, s: str) -> list[list[str]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/131-palindrome-partitioning/python -q
```
