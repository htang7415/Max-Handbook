# 404.Sum of Left Leaves

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the sum of all leaf nodes that are left children of their parents.

## Recognition Cues

- The property depends on both node position and node type.
- You must distinguish left leaves from all other nodes.
- Recursive traversal can carry the left-child context implicitly.

## Baseline Idea

Traverse every node, store whether it was reached from the left, and sum qualifying leaves afterward. That works, but a direct recursive check is simpler.

## Core Insight

At each node, if its left child exists and is a leaf, add that value immediately; otherwise recurse into both subtrees.

## Invariant / State

- The recursive call returns the sum of left leaves in the current subtree.
- A node contributes only when it is both a left child and a leaf.

## Walkthrough

For `[3, 9, 20, None, None, 15, 7]`:
- `9` is a left leaf, so add `9`.
- `15` is also a left leaf under `20`, so add `15`.
- Total is `24`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single node
- Tree with only right children

## Common Mistakes

- Summing all left children, even when they are not leaves
- Summing all leaves regardless of side
- Forgetting that `None` contributes zero

## Pattern Transfer

- 112.Path Sum
- Leaf-sensitive recursion
- Structural tree property checks

## Self-Check

- What exactly makes a node a left leaf?
- Why is a left internal node not counted?
- How does the recursion avoid double counting?

## Function

```python
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/404-sum-of-left-leaves/python -q
```
