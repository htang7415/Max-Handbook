# 452.Minimum Number of Arrows to Burst Balloons

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Find the fewest arrows needed to burst all balloon intervals.

## Recognition Cues

- Intervals overlap and one action can cover many of them.
- The goal is minimum number of shots, not merged intervals themselves.
- Choosing a point as late as possible can preserve future options.

## Baseline Idea

Try all possible shooting positions or repeatedly merge overlap groups. That is more complicated than needed.

## Core Insight

Sort balloons by ending coordinate. Shoot one arrow at the current earliest end, and reuse it for every balloon that still overlaps that point.

## Invariant / State

- `end` is the position of the latest arrow shot.
- Every processed balloon that starts at or before `end` is already burst by the current arrow.

## Walkthrough

For `[[10,16],[2,8],[1,6],[7,12]]`:
- Sort by end to get `[[1,6],[2,8],[7,12],[10,16]]`.
- Shoot at `6`, bursting the first two balloons.
- `7` starts after `6`, so shoot a second arrow.

## Complexity

- Time: `O(n log n)` due to sorting
- Space: depends on sort implementation, otherwise `O(1)` extra

## Edge Cases

- Empty input
- One balloon
- Balloons that only touch at endpoints

## Common Mistakes

- Sorting by start instead of end for this greedy rule
- Starting a new arrow when intervals still overlap at an endpoint
- Confusing this with interval merging

## Pattern Transfer

- 56.Merge Intervals
- 435.Non-overlapping Intervals
- End-sorted interval greedy problems

## Self-Check

- Why is sorting by end the right greedy order?
- When can the current arrow be reused?
- Why does touching at an endpoint still count as overlap here?

## Function

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/452-minimum-number-of-arrows-to-burst-balloons/python -q
```
