# Stack and Queue Summary

> Track: `dsa` | Topic: `stack-and-queue`

## What This Module Covers

This summary reviews stack and queue patterns: pair matching, traversal order, staged processing, and structure simulation.

## Recognition Cues

- Nested or reversible behavior suggests a stack.
- Level-order or arrival-order processing suggests a queue.
- The main difficulty is access discipline, not value computation.

## Core Ideas

- Stack top represents the most recent unresolved state.
- Queue front represents the next pending work item.
- Many "simulation" problems become easy once the right container is chosen.

## Common Mistakes

- Solving an order-discipline problem with the wrong container.
- Forgetting the meaning of the top or front element.
- Missing an explicit stack or queue simulation because the problem feels abstract.

## Connections

- Binary-tree traversals.
- Monotonic stack problems.
- BFS and frontier processing across graphs and trees.

## Self-Check

- What invariant does the top or front represent?
- When do you need FIFO versus LIFO?
- How do stacks simulate recursion?
