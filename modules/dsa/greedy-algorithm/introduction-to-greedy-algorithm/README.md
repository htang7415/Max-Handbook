# Introduction to Greedy Algorithm

> Track: `dsa` | Topic: `greedy-algorithm`

## What This Module Covers

Greedy algorithms build solutions by making the best local choice available now and relying on a structural reason that this never blocks the global optimum.

## Recognition Cues

- A choice can be made and never revisited.
- Local structure suggests one option clearly dominates others.
- A proof usually argues by exchange, invariant, or staying-ahead logic.

## Core Ideas

- Greedy is not "guess and hope"; it needs a correctness argument.
- Sorting often reveals the right local choice order.
- The key question is why a locally optimal move remains globally safe.

## Common Mistakes

- Calling a heuristic greedy without proving it.
- Choosing the largest or smallest value without understanding the invariant.
- Using greedy on a problem that really needs DP or backtracking.

## Connections

- Interval scheduling, stock accumulation, and local resource allocation.
- Some DP problems collapse to greedy when constraints become looser.
- Exchange arguments are the proof tool that makes greedy reliable.

## Self-Check

- What local choice is being made?
- Why can that choice be committed permanently?
- What proof idea justifies the algorithm?
