# 530.Minimum Absolute Difference in BST

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the smallest absolute difference between values of any two nodes in the BST.

## Recognition Cues

- The tree is a BST, so inorder traversal visits values in sorted order.
- The minimum difference in a sorted list must appear between adjacent values.
- One previous value is enough state.

## Baseline Idea

Collect all values, sort them, then scan adjacent differences. That works, but BST inorder traversal gives the sorted order directly.

## Core Insight

During inorder traversal, compare each node only with the previously visited node. Those adjacent values are the only candidates for the minimum difference.

## Invariant / State

- `prev` is the last value visited in inorder order.
- `min_diff` is the best difference seen so far.

## Walkthrough

For BST `[4,2,6,1,3]`:
- Inorder visits `1,2,3,4,6`.
- Adjacent differences are `1,1,1,2`.
- The minimum is `1`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Tree with two nodes
- Deep skewed BST
- Large gaps except one tight pair

## Common Mistakes

- Comparing non-adjacent values unnecessarily
- Forgetting that inorder order is sorted only for BSTs
- Not initializing `prev` carefully

## Pattern Transfer

- Inorder BST problems
- 98.Validate Binary Search Tree
- Sorted-order traversal reasoning

## Self-Check

- Why are adjacent inorder values enough?
- What does `prev` represent?
- Why would this logic fail on a non-BST?

## Function

```python
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/530-minimum-absolute-difference-in-bst/python -q
```
