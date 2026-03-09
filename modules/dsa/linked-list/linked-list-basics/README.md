# Linked List Basics

> Track: `dsa` | Topic: `linked-list`

## What This Module Covers

This module introduces the singly linked list model: node-by-node traversal, pointer following, and simple structural properties like head, tail, and length.

## Recognition Cues

- Data is connected by pointers, not contiguous indices.
- Access is sequential.
- Insertions and removals depend on pointer rewiring.

## Core Ideas

- Every node stores a value and a `next` pointer.
- Traversal is linear because random access is unavailable.
- Dummy nodes often simplify head-edge cases.

## Common Mistakes

- Treating a linked list like an array with index access.
- Losing the rest of the list while rewiring `next`.
- Forgetting special handling around the head node.

## Connections

- Fast/slow pointers and cycle detection.
- Reverse, remove, and splice operations.
- Dummy-node patterns across many linked-list problems.

## Self-Check

- What operations are easy on a linked list versus an array?
- Why are dummy nodes useful?
- What must be preserved before changing a `next` pointer?

## Function

```python
def linked_list_basics(values: list[int]) -> dict[str, int | None]:
```
