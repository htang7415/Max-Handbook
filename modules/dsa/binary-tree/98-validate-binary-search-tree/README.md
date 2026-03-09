# 98.Validate Binary Search Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Decide whether the binary tree satisfies the BST ordering rules everywhere.

## Recognition Cues

- A node’s validity depends on the full ancestor range, not just its parent.
- Local comparisons alone are insufficient.
- Recursive lower/upper bounds fit naturally.

## Baseline Idea

Check only whether each node is larger than its left child and smaller than its right child. That fails on deeper violations.

## Core Insight

Carry valid value bounds down the recursion. Every node must stay strictly between the lower and upper bounds inherited from its ancestors.

## Invariant / State

- `helper(node, low, high)` means the entire subtree rooted at `node` must lie in `(low, high)`.

## Walkthrough

For `[5,1,4,None,None,3,6]`:
- Node `4` is in the right subtree of `5`, so it must be greater than `5`.
- Its left child `3` violates that global bound, so the tree is not a BST.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single node
- Duplicates, which are invalid for strict BSTs

## Common Mistakes

- Checking only parent-child relationships
- Allowing equality in the bounds
- Forgetting to propagate ancestor constraints

## Pattern Transfer

- 700.Search in a Binary Search Tree
- 530.Minimum Absolute Difference in BST
- Range-constrained tree recursion

## Self-Check

- Why are parent-child checks alone insufficient?
- What do `low` and `high` mean?
- Why must the inequalities be strict?

## Function

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/98-validate-binary-search-tree/python -q
```
