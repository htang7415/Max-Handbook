# 206.Reverse Linked List

> Track: `dsa` | Topic: `linked-list`

## Problem in One Line

Reverse the linked list so the tail becomes the new head.

## Recognition Cues

- Every node’s `next` pointer must change direction.
- The list should be reversed by links, not by copying values.
- Only local pointer updates are needed.

## Baseline Idea

Collect node values and rebuild the list in reverse order. That works, but it uses extra space and avoids the pointer manipulation the problem is teaching.

## Core Insight

Walk through the list once while redirecting each node’s `next` pointer to the previous node.

## Invariant / State

- `prev` is the head of the already reversed prefix.
- `current` is the next node to reverse.
- Everything after `current` is still in original order.

## Walkthrough

For `1 -> 2 -> 3`:
- Reverse `1` to point to `None`.
- Reverse `2` to point to `1`.
- Reverse `3` to point to `2`.
- Return `3`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty list
- Single-node list
- Two-node list

## Common Mistakes

- Losing the rest of the list by overwriting `current.next` too early
- Returning the old head instead of `prev`
- Moving pointers in the wrong order

## Pattern Transfer

- 24.Swap Nodes In Pairs
- 203.Remove Linked List Elements
- Iterative pointer reversal patterns

## Self-Check

- Why must the next node be saved before rewiring `current.next`?
- What does `prev` represent after each step?
- Why is the final answer `prev`?

## Function

```python
def reverse_linked_list(head: ListNode | None) -> ListNode | None:
```

## Run tests

```bash
pytest modules/dsa/linked-list/206-reverse-linked-list/python -q
```
