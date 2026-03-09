# 203.Remove Linked List Elements

> Track: `dsa` | Topic: `linked-list`

## Problem in One Line

Remove every node whose value equals `val` and return the new head.

## Recognition Cues

- Nodes may need to be removed from the head, middle, or tail.
- Pointer rewiring matters more than value updates.
- A dummy node can simplify head deletion cases.

## Baseline Idea

Handle head removals separately, then walk the list and unlink matching nodes. This works but creates awkward special cases.

## Core Insight

Use a dummy node before the real head so every removal becomes a normal “skip the next node” operation.

## Invariant / State

- `prev.next` is always the next node that still needs to be examined or kept.
- `current` is the node currently being checked against `val`.

## Walkthrough

For `1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6`, removing `6`:
- Keep `1` and `2`.
- Skip the first `6`.
- Keep `3`, `4`, and `5`.
- Skip the final `6`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty list
- All nodes removed
- Consecutive target values at the front

## Common Mistakes

- Forgetting to handle removal of the original head
- Moving `prev` forward after deleting a node
- Losing the rest of the list during rewiring

## Pattern Transfer

- 19.Remove Nth Node From End of List
- 24.Swap Nodes In Pairs
- 206.Reverse Linked List

## Self-Check

- Why does the dummy node remove a special case?
- When should `prev` move forward?
- What goes wrong if `prev` advances after a deletion?

## Function

```python
def remove_linked_list_elements(head: ListNode | None, val: int) -> ListNode | None:
```

## Run tests

```bash
pytest modules/dsa/linked-list/203-remove-linked-list-elements/python -q
```
