# Greedy Algorithms Summary

> Track: `dsa` | Topic: `greedy-algorithm`

## What This Module Covers

This summary reviews the main greedy patterns in the track: sorting by the most constraining feature, earliest-finish interval choice, local gain accumulation, and resource-preserving decisions.

## Recognition Cues

- The problem admits a one-way commitment strategy.
- Sorting exposes a safe order of decisions.
- The proof depends on a local choice staying ahead or exchanging with any optimal solution.

## Core Ideas

- Interval problems often reward earliest finish.
- Sequence and stock problems often reward taking every safe local gain.
- Resource-allocation problems often depend on preserving the most flexible resource.
- Correctness needs an argument, not just intuition.

## Common Mistakes

- Using greedy because the code is short, not because the structure supports it.
- Missing the specific invariant that makes the choice safe.
- Confusing a DP recurrence with a greedy simplification.

## Connections

- Sorting is often the setup step for greedy.
- Some stock and maximum-subarray problems have both greedy and DP interpretations.
- Tree greedy problems often use postorder state reasoning.

## Self-Check

- What local choice is the algorithm committing to?
- Why can that choice not hurt the optimal answer?
- What proof technique explains the correctness?
