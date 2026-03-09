# 93.Restore IP Addresses

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Insert dots into the string to form all valid IPv4 addresses.

## Recognition Cues

- You must split the string into exactly four parts.
- Each part has strict validity rules: `0..255` and no leading zeros.
- The answer is all valid segmentations.

## Baseline Idea

Try all possible ways to place three dots and validate afterward. That works, but backtracking with early validity checks prunes sooner.

## Core Insight

Build the IP one segment at a time. At each step, only consider segment lengths `1` to `3`, and recurse only when the segment is valid.

## Invariant / State

- `path` stores the segments chosen so far.
- `start` is the next character index to consume.
- A complete answer requires exactly four segments and full consumption of the string.

## Walkthrough

For `"25525511135"`:
- Start with segment `"255"`.
- Continue with `"255"`, then either `"11"` or `"111"`.
- Record `"255.255.11.135"` and `"255.255.111.35"`.

## Complexity

- Time: bounded by the branching of four segments of length at most three
- Space: `O(4)` recursion depth, excluding the output

## Edge Cases

- String too short or too long
- Segments with leading zeros like `"01"`
- Segments greater than `255`

## Common Mistakes

- Allowing leading zeros in multi-digit segments
- Accepting fewer than four segments
- Forgetting that the full string must be consumed

## Pattern Transfer

- Palindrome partitioning
- Fixed-count segmentation backtracking
- Constraint-based string splitting

## Self-Check

- Why are only segment lengths `1..3` relevant?
- When is `"0"` valid and when is `"00"` invalid?
- What conditions make a path a complete answer?

## Function

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/93-restore-ip-addresses/python -q
```
