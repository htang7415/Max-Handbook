# 235.Lowest Common Ancestor of a BST

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Find the lowest node in the BST that has both `p` and `q` in its subtree.

## Recognition Cues

- The tree is a BST, so the relative values of `p`, `q`, and the current node matter.
- The answer is where the search paths to `p` and `q` diverge.
- You do not need to search both subtrees blindly.

## Baseline Idea

Use the generic binary-tree LCA recursion and search both sides. That works, but BST ordering makes it unnecessary.

## Core Insight

If both targets are smaller, go left. If both are larger, go right. Otherwise the current node is the split point and therefore the LCA.

## Invariant / State

- `current` is always a node whose subtree still contains both targets.

## Walkthrough

For BST root `6` with targets `2` and `8`:
- One target is smaller and one larger than `6`.
- The paths split at `6`, so `6` is the LCA.

## Complexity

- Time: `O(h)` where `h` is tree height
- Space: `O(1)` iterative space

## Edge Cases

- One target is the ancestor of the other
- Targets split at the root
- Small BST with only a few nodes

## Common Mistakes

- Using generic-tree logic and searching both subtrees
- Failing to return the current node when one target equals it
- Going left or right when the targets already split

## Pattern Transfer

- 700.Search in a Binary Search Tree
- BST-guided navigation
- 236.Lowest Common Ancestor of a Binary Tree

## Self-Check

- What does it mean for the paths to split?
- Why can the current node itself be the answer?
- How does BST ordering avoid exploring both sides?

## Function

```python
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/235-lowest-common-ancestor-of-a-bst/python -q
```
