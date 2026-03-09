# 56.Merge Intervals

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Merge all overlapping intervals and return the condensed list.

## Recognition Cues

- Intervals can overlap after sorting.
- Local overlap decisions determine the global merged result.
- Sorting by start time exposes the structure.

## Baseline Idea

Compare every interval with every other interval and repeatedly merge overlaps. That is more complicated and slower than necessary.

## Core Insight

Sort by start point. Then either extend the last merged interval if the next interval overlaps, or start a new interval if it does not.

## Invariant / State

- `merged` is always a sorted list of non-overlapping intervals.
- `merged[-1]` is the only interval the next sorted interval can overlap with.

## Walkthrough

For `[[1,3],[2,6],[8,10],[15,18]]`:
- Merge `[1,3]` with `[2,6]` into `[1,6]`.
- `[8,10]` does not overlap, so start a new interval.
- `[15,18]` also stands alone.

## Complexity

- Time: `O(n log n)` due to sorting
- Space: `O(n)` for the output

## Edge Cases

- Empty input
- Touching intervals like `[1,4]` and `[4,5]`
- One interval fully contained in another

## Common Mistakes

- Forgetting to sort first
- Comparing against all prior intervals instead of just the last merged one
- Mishandling touching endpoints

## Pattern Transfer

- Insert Interval
- 452.Minimum Number of Arrows to Burst Balloons
- 435.Non-overlapping Intervals

## Self-Check

- Why is only the last merged interval relevant after sorting?
- When do two intervals count as overlapping?
- Why does sorting dominate the time complexity?

## Function

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/56-merge-intervals/python -q
```
