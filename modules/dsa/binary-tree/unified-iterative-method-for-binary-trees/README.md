# Unified Iterative Method for Binary Trees

> Track: `dsa` | Topic: `binary-tree`

## What This Module Covers

This note shows the unified stack-plus-marker pattern that can express preorder, inorder, and postorder traversal with one iterative framework.

## Recognition Cues

- You want one reusable iterative template for multiple traversal orders.
- The main challenge is distinguishing "first time seen" from "ready to process".
- A visited marker or null marker can encode recursive return points.

## Core Ideas

- Push nodes in an order that simulates recursive expansion.
- Use a marker to indicate when a node should now be processed.
- Changing the push order changes the traversal order while keeping the same overall template.

## Common Mistakes

- Treating the marker like a regular node.
- Pushing children in the wrong order for the intended traversal.
- Forgetting that the unified template is simulating recursion state explicitly.

## Connections

- Recursive traversal provides the conceptual reference.
- Iterative traversal uses specialized versions of the same idea.
- Stack discipline is what makes the simulation work.

## Self-Check

- What does the marker represent?
- How does push order control preorder versus inorder versus postorder?
- Why is this method more uniform than writing three separate stack algorithms?

## Function

```python
def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
```
