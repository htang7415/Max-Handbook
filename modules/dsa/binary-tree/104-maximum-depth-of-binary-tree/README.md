# 104.Maximum Depth of Binary Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the number of nodes on the longest path from the root down to a leaf.

## Recognition Cues

- The answer for a node depends on the answers for its children.
- You need the longest downward path.
- Tree height and recursion are directly connected.

## Baseline Idea

Traverse every root-to-leaf path and track the longest one found. That works, but a recursive height formula is simpler.

## Core Insight

The maximum depth of a node is `1 + max(depth(left), depth(right))`.

## Invariant / State

- `maxDepth(node)` returns the depth of the subtree rooted at `node`.

## Walkthrough

For a tree with root `3`, children `9` and `20`, and grandchildren `15` and `7` under `20`:
- Leaves have depth `1`.
- Node `20` has depth `2`.
- Root `3` has depth `3`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack, where `h` is tree height

## Edge Cases

- Empty tree
- Single-node tree
- Completely skewed tree

## Common Mistakes

- Counting edges instead of nodes
- Forgetting that an empty tree has depth `0`
- Using the minimum child depth instead of the maximum

## Pattern Transfer

- 111.Minimum Depth of Binary Tree
- Height/balance tree problems
- Recursive postorder aggregation

## Self-Check

- Why does the empty tree return `0`?
- Why do we add `1` at each node?
- What changes if the question asks for minimum depth instead?

## Function

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/104-maximum-depth-of-binary-tree/python -q
```
