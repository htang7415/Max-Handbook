# Multiple Knapsack Theory

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This note covers bounded knapsack, where each item has a limited count, and shows the common expansion-to-0-1 approach.

## Recognition Cues

- Items have capacity costs, values, and limited multiplicities.
- Reuse is allowed only up to a bound.
- The easiest teaching approach is often to expand the bounded items into multiple 0-1 items.

## Core Ideas

- Replace each bounded item with repeated 0-1 items according to its count.
- Run 0-1 knapsack on the expanded list.
- The conceptual difference from complete knapsack is the finite quantity.

## Common Mistakes

- Treating bounded items like unlimited items.
- Forgetting that expansion changes input size.
- Losing track of whether the loop direction should still be 0-1 style after expansion.

## Connections

- 0-1 knapsack provides the implementation core.
- Complete knapsack is the unbounded contrast case.
- Binary splitting is a more advanced optimization beyond the teaching version here.

## Self-Check

- How is bounded reuse different from unlimited reuse?
- Why does expansion reduce the problem to 0-1 knapsack?
- What tradeoff does the expansion method make?

## Function

```python
class Solution:
    def multipleKnapsack(self, weights: List[int], values: List[int], counts: List[int], capacity: int) -> int:
```
