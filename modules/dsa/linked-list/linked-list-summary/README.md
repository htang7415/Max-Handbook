# Linked List Summary

> Track: `dsa` | Topic: `linked-list`

## What This Module Covers

This summary reviews the main linked-list ideas: sequential traversal, pointer rewiring, dummy nodes, intersections, and cycle reasoning.

## Recognition Cues

- You cannot jump by index.
- The problem is really about pointer structure.
- Edge cases often occur at the head or tail.

## Core Ideas

- Traversal and rewiring are the two base moves.
- Dummy nodes remove many head-deletion special cases.
- Fast/slow pointer logic solves cycle and midpoint families.

## Common Mistakes

- Comparing values when node identity matters.
- Forgetting to save a `next` pointer before rewiring.
- Writing list logic as if it were array logic.

## Connections

- Double-pointer patterns on linked lists.
- Tree pointer reasoning shares the same identity-first mindset.
- Hash tables can trade space for simpler cycle or intersection checks.

## Self-Check

- When do you need node identity instead of value equality?
- Which linked-list problems benefit from dummy nodes?
- What does fast/slow movement buy you?

## Function

```python
def linked_list_summary(head: ListNode | None) -> dict[str, int | bool | None]:
```
