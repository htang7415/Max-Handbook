# 435.Non-overlapping Intervals

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Remove the fewest intervals so the remaining intervals do not overlap.

## Recognition Cues

- Minimizing removals is equivalent to maximizing the number kept.
- Interval scheduling usually rewards the earliest finishing choice.
- Sorting by end time is the natural greedy order.

## Baseline Idea

Try every subset of intervals and keep the largest non-overlapping one. That works, but it is combinatorial.

## Core Insight

Sort intervals by end time and greedily keep the next interval whose start is at least the current end. This maximizes how many intervals survive, so removals are `total - kept`.

## Invariant / State

- `end` is the finishing time of the last kept interval.
- `count` is the number of non-overlapping intervals kept so far.

## Walkthrough

For `[[1,2],[2,3],[3,4],[1,3]]`:
- Keep `[1,2]`
- Keep `[2,3]`
- Keep `[3,4]`
- Drop `[1,3]`
- Only `1` removal is needed

## Complexity

- Time: `O(n log n)`
- Space: `O(1)` extra, ignoring sort internals

## Edge Cases

- Empty interval list
- All intervals overlapping
- Touching endpoints that do not overlap

## Common Mistakes

- Sorting by start instead of end
- Treating touching endpoints as overlap when `start >= end` is allowed
- Counting removals directly instead of maximizing kept intervals

## Pattern Transfer

- Interval scheduling
- Earliest-finish greedy strategy
- 452 and 56 interval problems

## Self-Check

- Why does earliest finish leave the most room for later intervals?
- Why is the answer `len(intervals) - kept`?
- When do two intervals count as non-overlapping here?

## Function

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/435-non-overlapping-intervals/python -q
```
