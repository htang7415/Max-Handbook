# Introduction to Stack and Queue

> Track: `dsa` | Topic: `stack-and-queue`

## What This Module Covers

This introduction covers the two base access disciplines: stacks are LIFO, queues are FIFO, and each naturally matches different problem shapes.

## Recognition Cues

- The newest item should be processed first: think stack.
- The oldest item should be processed first: think queue.
- The problem simulates nesting, traversal order, or staged processing.

## Core Ideas

- Stacks model reversal, matching, and explicit recursion state.
- Queues model level-order processing and first-ready work.
- The data structure choice is about access order, not lookup speed.

## Common Mistakes

- Choosing a stack when the process is really breadth-first.
- Using recursion when an explicit stack would make the state clearer.
- Forgetting that order discipline is the entire point of the structure.

## Connections

- Binary-tree BFS uses queues.
- Monotonic stacks extend the stack idea with an ordering invariant.
- Parentheses, duplicate removal, and traversal simulation all reuse stack logic.

## Self-Check

- What access order does the problem demand?
- Is the process depth-first, breadth-first, or last-in-first-out?
- Would a deque simplify the implementation?
