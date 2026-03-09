# Complete Knapsack Theory

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This note covers the complete knapsack, where each item may be used unlimited times.

## Recognition Cues

- Items can be reused.
- Capacity is still the limiting resource.
- Loop direction changes compared with 0-1 knapsack.

## Core Ideas

- Use a 1D capacity DP.
- Iterate capacities forward so one item can contribute multiple times in the same pass.
- The state meaning stays "best value for capacity `c`", but the update order changes because reuse is allowed.

## Common Mistakes

- Reusing the backward loop from 0-1 knapsack.
- Forgetting that the same item may appear multiple times in the optimal answer.
- Treating this as a separate idea instead of a loop-order variation of knapsack.

## Connections

- Coin Change and Perfect Squares are complete-knapsack descendants.
- 0-1 knapsack differs mainly in whether reuse is allowed.
- Counting versions change the aggregation rule but keep the same capacity mindset.

## Self-Check

- Why does forward iteration allow reuse?
- What is unchanged between 0-1 and complete knapsack?
- Which real problems behave like unlimited-item knapsack?

## Function

```python
class Solution:
    def completeKnapsack(self, weights: List[int], values: List[int], capacity: int) -> int:
```
