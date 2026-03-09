# 707.Design Linked List

> Track: `dsa` | Topic: `linked-list`

## Problem in One Line

Implement a singly linked list that supports indexed reads, inserts, and deletes.

## Recognition Cues

- You are building the data structure itself, not just using it.
- Indexed operations need boundary checks.
- A dummy head simplifies head insertions and deletions.

## Baseline Idea

Handle head operations separately from general indexed operations. That works, but it creates duplicated edge-case logic.

## Core Insight

Use a dummy head and track the current size so inserts and deletes can be handled uniformly from a predecessor node.

## Invariant / State

- `head` is a dummy node before the real first element.
- `size` matches the number of real nodes.
- Traversal for index `i` always stops at the predecessor when mutation is needed.

## Walkthrough

For operations `addAtHead(1)`, `addAtTail(3)`, `addAtIndex(1, 2)`:
- The list becomes `1`.
- Then `1 -> 3`.
- Then `1 -> 2 -> 3`.

## Complexity

- `get`, `addAtIndex`, `deleteAtIndex`: `O(n)`
- `addAtHead`: `O(1)`
- `addAtTail`: `O(n)` in this singly linked version

## Edge Cases

- Invalid indices
- Insert at the head
- Insert at the tail
- Delete the last element

## Common Mistakes

- Forgetting to update `size`
- Inserting at index `size + 1`
- Deleting without stopping at the predecessor

## Pattern Transfer

- 203.Remove Linked List Elements
- 24.Swap Nodes In Pairs
- Sentinel-node linked-list design

## Self-Check

- Why is a dummy head useful?
- What index values should be ignored?
- When should `size` change?

## Function

```python
class MyLinkedList:
    def get(self, index: int) -> int:
    def addAtHead(self, val: int) -> None:
    def addAtTail(self, val: int) -> None:
    def addAtIndex(self, index: int, val: int) -> None:
    def deleteAtIndex(self, index: int) -> None:
```

## Run tests

```bash
pytest modules/dsa/linked-list/707-design-linked-list/python -q
```
