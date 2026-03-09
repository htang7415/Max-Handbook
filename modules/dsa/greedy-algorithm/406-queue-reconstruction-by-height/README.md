# 406.Queue Reconstruction by Height

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Reconstruct the queue so each person has exactly `k` taller-or-equal people in front.

## Recognition Cues

- Taller people constrain shorter people, but not vice versa.
- Sorting can remove ambiguity in insertion order.
- Position `k` becomes meaningful once taller people are already placed.

## Baseline Idea

Try every queue ordering and check whether it satisfies all `k` constraints. That works, but it is factorial.

## Core Insight

Sort by height descending and `k` ascending. Then insert each person at index `k`. Because taller-or-equal people are already fixed, inserting a shorter person does not break the earlier constraints.

## Invariant / State

- Before inserting a new person, the queue already satisfies the constraints for everyone placed so far.

## Walkthrough

For `[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`:
- Sort descending by height
- Insert each person at index `k`
- The final queue becomes `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

## Complexity

- Time: `O(n^2)` due to list insertions
- Space: `O(n)`

## Edge Cases

- One person
- Multiple people with the same height
- Many `k = 0` entries

## Common Mistakes

- Sorting shorter people first
- Sorting same-height people by descending `k`
- Assuming insertion order does not matter

## Pattern Transfer

- Greedy by fixing the most constrained elements first
- Sort then insert
- Constraint-preserving reconstruction

## Self-Check

- Why are taller people processed first?
- Why should same-height people be sorted by increasing `k`?
- Why does inserting a shorter person later not break earlier placements?

## Function

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/406-queue-reconstruction-by-height/python -q
```
