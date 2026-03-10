# 222.Count Complete Tree Nodes

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the number of nodes in the tree.

## Recognition Cues

- The tree is complete, not just arbitrary.
- A complete tree may contain perfect subtrees.
- Height checks can avoid visiting every node.

## Baseline Idea

Traverse the tree and count nodes directly in `O(n)`.

## Core Insight

If the leftmost height and rightmost height of a subtree are equal, that subtree is perfect and its node count is `(2^h) - 1`.

## Invariant / State

- Equal leftmost and rightmost heights mean the current subtree is perfect.
- Otherwise, recurse into left and right children and combine the counts.

## Walkthrough

For `[1,2,3,4,5,6]`:
- The root is not a perfect subtree because its left and right boundary heights differ.
- The left subtree rooted at `2` is perfect, so count it in `O(1)` from its height.
- Recurse only where the last level is incomplete, then combine the counts.

## Complexity

- Time: `O((log n)^2)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single-node tree
- Last level partially filled

## Common Mistakes

- Forgetting that the perfect-subtree formula counts nodes, not edges
- Measuring only one side height and assuming the subtree is perfect
- Falling back to full traversal and missing the complete-tree optimization

## Pattern Transfer

- Height-based complete-tree checks
- Perfect binary tree counting
- Binary-search-style structure exploitation on trees

## Self-Check

- When does a complete subtree become a perfect subtree?
- Why does equal leftmost and rightmost height imply `(2^h) - 1` nodes?
- Why is the complexity `O((log n)^2)` instead of `O(n)`?

## Function

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/222-count-complete-tree-nodes/python -q
```
