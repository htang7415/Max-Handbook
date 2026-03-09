# 111.Minimum Depth of Binary Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the number of nodes on the shortest path from the root to a leaf.

## Recognition Cues

- The tree question asks for the shortest root-to-leaf path.
- Missing children matter; you cannot always take `min(left, right)` blindly.
- Leaf definition is central.

## Baseline Idea

Compute both child depths and take the smaller one. That fails when one child is missing, because a missing child is not a valid root-to-leaf path.

## Core Insight

If one child is missing, the minimum depth must come from the existing child. Only when both children exist can you take the smaller depth.

## Invariant / State

- `minDepth(node)` returns the minimum root-to-leaf depth of the subtree rooted at `node`.
- A `None` child does not count as a candidate path from a non-leaf parent.

## Walkthrough

For a root whose left child is `None` and right child leads to a chain:
- You cannot use depth `0` from the missing side.
- The minimum depth is `1 + minDepth(right)`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack, where `h` is tree height

## Edge Cases

- Empty tree
- Single-node tree
- Completely one-sided tree

## Common Mistakes

- Using `1 + min(left_depth, right_depth)` even when one child is missing
- Treating any `None` child as a leaf
- Confusing minimum depth with tree height

## Pattern Transfer

- 104.Maximum Depth of Binary Tree
- BFS shortest-path tree layers
- Leaf-sensitive recursive aggregation

## Self-Check

- Why is a node with one missing child not a leaf?
- When is it valid to take the minimum of two child depths?
- How does this differ from maximum depth?

## Function

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/111-minimum-depth-of-binary-tree/python -q
```
