# 222.Count Complete Tree Nodes

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the number of nodes in the tree.

## Recognition Cues

- The current implementation is simple recursive counting.
- Each subtree contributes its own node count plus one for the root.
- No extra state beyond recursion is needed.

## Baseline Idea

Traverse the tree and count nodes directly. That is already the implementation used here.

## Core Insight

The total nodes in a tree equal `1 + count(left) + count(right)`.

## Invariant / State

- `countNodes(node)` returns the number of nodes in the subtree rooted at `node`.

## Walkthrough

For `[1,2,3,4,5,6]`:
- Count the left subtree rooted at `2`.
- Count the right subtree rooted at `3`.
- Add `1` for the root to get `6`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single-node tree
- Last level partially filled

## Common Mistakes

- Forgetting the base case for `None`
- Counting edges instead of nodes
- Assuming completeness changes the DFS recurrence in this implementation

## Pattern Transfer

- Tree size aggregation
- Recursive subtree counting
- 104.Maximum Depth of Binary Tree

## Self-Check

- What does `countNodes(node)` return?
- Why does the empty tree return `0`?
- Why is the recurrence `1 + left + right`?

## Function

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/222-count-complete-tree-nodes/python -q
```
