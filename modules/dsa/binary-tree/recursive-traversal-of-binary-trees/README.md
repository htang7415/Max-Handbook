# Recursive Traversal of Binary Trees

> Track: `dsa` | Topic: `binary-tree`

## What This Module Covers

This note covers recursive preorder, inorder, and postorder traversal, which form the base mental model for most tree problems.

## Recognition Cues

- The operation at a node is naturally defined relative to its left and right subtrees.
- Traversal order changes when the node value is processed.
- The recursive version is the clearest first solution.

## Core Ideas

- Preorder: node, left, right.
- Inorder: left, node, right.
- Postorder: left, right, node.
- The base case is always an empty node.

## Common Mistakes

- Using the wrong traversal order for the task.
- Forgetting the `None` base case.
- Not deciding whether the recursive call mutates shared output or returns a new value.

## Connections

- Iterative traversal simulates this recursion with a stack.
- BST inorder traversal has sorted-order meaning.
- Many tree DP problems are postorder-style aggregations.

## Self-Check

- What changes between preorder, inorder, and postorder?
- Why is the empty node the natural base case?
- Which traversal order is best when children must be solved first?

## Function

```python
def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
```
