# 24.Swap Nodes In Pairs

> Track: `dsa` | Topic: `linked-list`

## Problem in One Line

Swap every two adjacent nodes in the linked list and return the new head.

## Recognition Cues

- Nodes must be rearranged by pointer rewiring, not by swapping values.
- Head changes after the first swap.
- A dummy node simplifies pair handling.

## Baseline Idea

Swap node values in place. That may work for this problem, but it avoids the pointer manipulation the problem is designed to teach.

## Core Insight

Use a dummy node and swap pairs by rewiring `prev -> second -> first -> next_pair`.

## Invariant / State

- `prev.next` is the first node of the next pair to swap.
- After each iteration, everything before `prev` is already correctly swapped.

## Walkthrough

For `1 -> 2 -> 3 -> 4`:
- Swap `1` and `2` to get `2 -> 1 -> 3 -> 4`.
- Move `prev` to `1`.
- Swap `3` and `4` to get `2 -> 1 -> 4 -> 3`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty list
- Single-node list
- Odd number of nodes

## Common Mistakes

- Losing the rest of the list while rewiring
- Moving `prev` to the wrong node after a swap
- Forgetting that the new head changes after the first pair

## Pattern Transfer

- 203.Remove Linked List Elements
- 19.Remove Nth Node From End of List
- Pair/group rewiring in linked lists

## Self-Check

- Why is a dummy node useful here?
- Which node should `prev` point to after a swap?
- Why does the last node stay unchanged in an odd-length list?

## Function

```python
def swap_nodes_in_pairs(head: ListNode | None) -> ListNode | None:
```

## Run tests

```bash
pytest modules/dsa/linked-list/24-swap-nodes-in-pairs/python -q
```
