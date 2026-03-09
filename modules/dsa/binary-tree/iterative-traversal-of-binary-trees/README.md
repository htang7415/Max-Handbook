# Iterative Traversal of Binary Trees

> Track: `dsa` | Topic: `binary-tree`

## What This Module Covers

This note shows how to replace recursive DFS with an explicit stack for preorder, inorder, and postorder traversal.

## Recognition Cues

- You want DFS order without recursion.
- The call stack behavior must be simulated manually.
- Traversal order depends on when a node is processed relative to its children.

## Core Ideas

- A stack stores the unfinished path of work.
- Preorder is easiest because nodes are processed when popped.
- Inorder and postorder need more careful push order or revisit logic.

## Common Mistakes

- Pushing children in the wrong order.
- Forgetting that stack order reverses processing order.
- Treating all three traversals as the same iterative pattern.

## Connections

- Recursive traversal gives the conceptual model.
- Unified iterative traversal uses one general stack pattern for all orders.
- Stack-and-queue fundamentals explain why DFS naturally uses a stack.

## Self-Check

- Why does preorder push right child before left child?
- What extra structure does inorder need compared with preorder?
- Why is postorder the trickiest iterative traversal?

## Function

```python
def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
```
