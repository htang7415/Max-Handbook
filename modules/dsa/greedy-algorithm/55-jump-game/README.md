# 55.Jump Game

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Decide whether you can reach the last index from the first index.

## Recognition Cues

- Each position gives a local reach range.
- You only need to know whether the end is reachable, not the full path.
- A running best reach can summarize everything seen so far.

## Baseline Idea

Try all possible jumps recursively or with DP. That works, but it does more work than needed because many paths lead to the same reachability question.

## Core Insight

While scanning left to right, track the farthest index reachable so far. If you ever reach an index beyond that boundary, the answer is immediately `False`.

## Invariant / State

- `farthest` is the greatest index reachable using jumps from positions already scanned.
- Every index `<= farthest` is reachable.

## Walkthrough

For `[2, 3, 1, 1, 4]`:
- At index `0`, `farthest = 2`.
- At index `1`, update `farthest = 4`.
- Since the last index is now reachable, the answer is `True`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Single-element array
- A zero that blocks all progress
- Early large jumps that cover the rest of the array

## Common Mistakes

- Continuing to scan after landing beyond the reachable boundary
- Treating every zero as failure, even when it is already bypassed
- Using DP where a running reach is enough

## Pattern Transfer

- 45.Jump Game II
- Gas Station
- Interval reachability style greedy problems

## Self-Check

- Why is the farthest reachable index enough to summarize the past?
- What exactly makes the algorithm return `False`?
- Why can a zero still be harmless in some inputs?

## Function

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/55-jump-game/python -q
```
