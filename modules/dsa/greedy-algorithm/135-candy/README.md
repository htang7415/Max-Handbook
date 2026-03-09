# 135.Candy

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Give each child candies so higher-rated children get more than their neighbors, while minimizing the total.

## Recognition Cues

- Local neighbor constraints apply in both directions.
- A single left-to-right pass misses right-side comparisons.
- Two greedy passes can satisfy both sides.

## Baseline Idea

Try all valid candy assignments and keep the minimum total. That works conceptually, but it is not practical.

## Core Insight

First pass left-to-right: satisfy the rule relative to the left neighbor. Second pass right-to-left: satisfy the rule relative to the right neighbor, taking the max so the first pass is not broken.

## Invariant / State

- After the first pass, every child with a higher left rating has more candy than the left neighbor.
- After the second pass, both left and right neighbor rules hold.

## Walkthrough

For `[1, 0, 2]`:
- Left-to-right gives `[1, 1, 2]`
- Right-to-left fixes the middle relation, producing `[2, 1, 2]`
- Total candies: `5`

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- One child
- Equal adjacent ratings
- Strictly increasing or decreasing ratings

## Common Mistakes

- Using one pass only
- Overwriting the first pass in the second instead of taking `max`
- Giving extra candies to equal ratings unnecessarily

## Pattern Transfer

- Two-pass greedy constraints
- Local consistency from both directions
- Rating / slope-style greedy problems

## Self-Check

- Why are two passes needed?
- What does the right-to-left pass repair?
- Why do equal ratings not force extra candies?

## Function

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/135-candy/python -q
```
