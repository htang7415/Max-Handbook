# 102.Binary Tree Level Order Traversal

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the node values level by level from top to bottom.

## Recognition Cues

- The output is grouped by distance from the root.
- You need to process nodes in breadth-first order.
- A queue matches the traversal order directly.

## Baseline Idea

You can do a DFS and store values by depth, but a queue-based breadth-first search matches the required traversal more directly.

## Core Insight

Before each level starts, the queue already contains exactly the nodes in that level. Process that many nodes, then enqueue their children for the next round.

## Invariant / State

- The queue holds the current frontier of the traversal.
- `len(queue)` at the start of a round is the number of nodes in the current level.

## Walkthrough

For `[3, 9, 20, null, null, 15, 7]`:
- Start with queue `[3]`, output level `[3]`.
- Next queue is `[9, 20]`, output level `[9, 20]`.
- Next queue is `[15, 7]`, output level `[15, 7]`.

## Complexity

- Time: `O(n)`
- Space: `O(w)`, where `w` is the maximum width of the tree

## Edge Cases

- Empty tree
- Single-node tree
- Left-skewed or right-skewed tree

## Common Mistakes

- Forgetting to handle `root is None`
- Iterating over a queue while appending children without freezing the level size
- Mixing nodes from two different levels into the same output list

## Pattern Transfer

- 111.Minimum Depth of Binary Tree
- 513.Find Bottom Left Tree Value
- Binary Tree Right Side View

## Self-Check

- Why does `len(queue)` need to be captured before processing a level?
- What exactly is inside the queue after one level finishes?
- When would DFS be more natural than BFS here?

## Function

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/102-binary-tree-level-order-traversal/python -q
```
