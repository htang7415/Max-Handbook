# 232.Implement Queue using Stacks

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Implement FIFO queue operations using only stacks.

## Recognition Cues

- The required behavior is queue-like, but the allowed primitive is a stack.
- Reversing order twice restores FIFO behavior.
- Delayed transfer can avoid unnecessary work.

## Baseline Idea

Move all elements between stacks on every pop or peek. That works, but it does extra transfers.

## Core Insight

Push into `in_stack`. Only when `out_stack` is empty do you transfer everything from `in_stack`, reversing order once so the oldest item is on top.

## Invariant / State

- `in_stack` stores newly pushed items.
- `out_stack` stores items in queue-pop order.
- If `out_stack` is non-empty, its top is the current queue front.

## Walkthrough

Push `1`, then `2`:
- `in_stack = [1, 2]`, `out_stack = []`.
- On `peek`, move to `out_stack = [2, 1]`.
- The queue front is now `1`.

## Complexity

- Amortized time per operation: `O(1)`
- Space: `O(n)`

## Edge Cases

- Queue with one element
- Multiple `peek` calls without new pushes
- Push after some pops have already happened

## Common Mistakes

- Transferring on every pop even when `out_stack` already has items
- Mixing the front element between both stacks
- Forgetting the amortized argument

## Pattern Transfer

- 225.Implement Stack using Queues
- Two-container amortized data structures
- Reversal-based simulation

## Self-Check

- Why is transfer only needed when `out_stack` is empty?
- Which stack contains the logical front?
- Why is the total work still linear across many operations?

## Function

```python
class MyQueue:
    def push(self, x: int) -> None:
    def pop(self) -> int:
    def peek(self) -> int:
    def empty(self) -> bool:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/232-implement-queue-using-stacks/python -q
```
