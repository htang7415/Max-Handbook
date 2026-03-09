# Knapsack Summary

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This summary compares the main knapsack families: 0-1, complete, multiple, feasibility, counting, and optimization variants.

## Recognition Cues

- A resource capacity constrains what can be taken.
- Choices are item-based and state is capacity-based.
- Loop direction and aggregation rule are the main variant switches.

## Core Ideas

- 0-1 knapsack uses backward capacity updates.
- Complete knapsack uses forward capacity updates.
- Counting problems change `max/min` into `+`.
- Feasibility problems change values into boolean reachability.

## Common Mistakes

- Using the wrong loop direction.
- Mixing optimization and counting transitions.
- Missing that many named problems are just knapsack in disguise.

## Connections

- Target Sum, Partition Equal Subset Sum, Coin Change, and Perfect Squares.
- Capacity DP patterns generalize beyond literal weight/value stories.
- Multi-dimensional knapsack extends the same reasoning with more resources.

## Self-Check

- What changes between 0-1 and complete knapsack?
- How does counting knapsack differ from maximizing knapsack?
- How do you spot a disguised knapsack problem?
