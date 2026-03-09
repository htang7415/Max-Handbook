# 226.Invert Binary Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Mirror the binary tree by swapping every node’s left and right children.

## Recognition Cues

- The same operation must be applied to every node.
- The left and right subtrees are treated symmetrically.
- Recursion maps naturally onto the tree structure.

## Baseline Idea

Traverse the tree and manually swap children node by node. Recursion is the cleanest way to express that repeated structure.

## Core Insight

Invert the left and right subtrees, then swap them at the current node.

## Invariant / State

- `invertTree(node)` returns the root of the fully inverted subtree rooted at `node`.

## Walkthrough

For root `4` with children `2` and `7`:
- Invert the subtree rooted at `7`.
- Invert the subtree rooted at `2`.
- Swap them so `7` becomes the left child and `2` the right child.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack, where `h` is tree height

## Edge Cases

- Empty tree
- Single-node tree
- A tree with only one side populated

## Common Mistakes

- Swapping children before preserving access to the original subtrees in iterative variants
- Forgetting the `None` base case
- Thinking the tree must remain a BST after inversion

## Pattern Transfer

- 101.Symmetric Tree
- 617.Merge Two Binary Trees
- Recursive tree traversal patterns

## Self-Check

- What does the recursive call return?
- Why is `None` the correct base case?
- How does a skewed tree change the recursion depth?

## Function

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/226-invert-binary-tree/python -q
```
