# 225.Implement Stack using Queues

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Implement stack operations using only queue behavior.

## Recognition Cues

- The required interface is LIFO, but the allowed primitive is FIFO.
- Reordering on push can make pop and top simple.
- Queue rotation can simulate a stack top.

## Baseline Idea

Push normally and rotate elements during every pop. That works, but it moves the cost to the wrong operation.

## Core Insight

After pushing a new element, rotate the queue so the new element moves to the front. Then `pop` and `top` can read directly from the front.

## Invariant / State

- The queue front is always the logical top of the stack.

## Walkthrough

Push `1`, then `2`:
- Queue after pushing `1`: `[1]`
- Queue after pushing `2`: `[2, 1]`
- Now `top()` and `pop()` both see `2` first.

## Complexity

- `push`: `O(n)`
- `pop`, `top`, `empty`: `O(1)`

## Edge Cases

- Single element
- Interleaving pushes and pops
- Reading top repeatedly without mutation

## Common Mistakes

- Rotating the wrong number of elements
- Leaving the newest item at the back
- Confusing queue front with queue back

## Pattern Transfer

- 232.Implement Queue using Stacks
- Amortized vs eager data-structure simulation
- Container-order transformations

## Self-Check

- Why does rotation happen after `push`?
- What does the queue front represent?
- Why do `pop` and `top` become easy after rotation?

## Function

```python
class MyStack:
    def push(self, x: int) -> None:
    def pop(self) -> int:
    def top(self) -> int:
    def empty(self) -> bool:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/225-implement-stack-using-queues/python -q
```
