# 700.Search in a Binary Search Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Find and return the subtree rooted at the node whose value equals `val`.

## Recognition Cues

- The tree is a BST, so left and right choices are meaningful.
- You only need one matching node, not a full traversal.
- Comparisons can discard half the search space at each step.

## Baseline Idea

Traverse the whole tree and compare every node. That works, but it ignores the BST ordering.

## Core Insight

At each node:
- go left if `val` is smaller
- go right if `val` is larger
- stop when the value matches or the search falls off the tree

## Invariant / State

- `current` is the root of the only subtree where `val` can still appear.

## Walkthrough

For BST `[4,2,7,1,3]` and `val = 2`:
- Compare with `4`, go left.
- Compare with `2`, match and return that node.

## Complexity

- Time: `O(h)` where `h` is tree height
- Space: `O(1)` iterative space

## Edge Cases

- Empty tree
- Target at the root
- Target absent

## Common Mistakes

- Traversing both subtrees even after BST ordering narrows the search
- Returning just the value instead of the subtree root
- Going the wrong direction on comparison

## Pattern Transfer

- BST insert/delete/search
- 98.Validate Binary Search Tree
- Ordered tree navigation

## Self-Check

- Why does BST ordering allow a single path search?
- What does the function return when the value is absent?
- What exactly is returned when the value is found?

## Function

```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/700-search-in-a-binary-search-tree/python -q
```
