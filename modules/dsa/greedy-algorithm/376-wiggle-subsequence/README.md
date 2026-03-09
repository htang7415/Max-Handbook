# 376.Wiggle Subsequence

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Find the longest subsequence whose consecutive differences strictly alternate signs.

## Recognition Cues

- Only changes in direction matter.
- Equal adjacent values do not help.
- Keeping turning points greedily is enough.

## Baseline Idea

Try all subsequences and check which ones wiggle. That works, but it is exponential.

## Core Insight

Track the previous nonzero difference. Every time the current difference changes sign relative to the previous one, extend the wiggle length. Local turning points are all that matter.

## Invariant / State

- `prev_diff` stores the sign of the last accepted wiggle step.
- `count` is the wiggle length built so far.

## Walkthrough

For `[1, 7, 4, 9, 2, 5]`:
- Differences alternate `+ - + - +`
- Every sign change extends the wiggle
- The full length is `6`

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty array
- One element
- Flat repeated values

## Common Mistakes

- Counting zero differences as wiggles
- Tracking actual values instead of difference signs
- Confusing subsequence with subarray

## Pattern Transfer

- Greedy turning-point selection
- Sign-change tracking
- Compressing a sequence to its essential shape

## Self-Check

- Why can interior points on the same slope be discarded?
- What role does `prev_diff` play?
- Why do equal consecutive values not help?

## Function

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/376-wiggle-subsequence/python -q
```
