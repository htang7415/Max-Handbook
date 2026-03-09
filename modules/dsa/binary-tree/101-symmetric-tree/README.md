# 101.Symmetric Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Decide whether the binary tree is a mirror of itself around its center.

## Recognition Cues

- The comparison is between left and right subtrees.
- Values and structure must mirror, not just match by level.
- A paired recursion over two nodes is natural.

## Baseline Idea

Traverse both subtrees separately and compare their serializations. That works, but it is indirect and adds extra representation work.

## Core Insight

Two subtrees are mirrors if:
- both roots have the same value
- outer children match each other
- inner children match each other

## Invariant / State

- `mirror(left, right)` answers whether those two nodes root mirrored subtrees.

## Walkthrough

For `[1,2,2,3,4,4,3]`:
- Compare the two `2` nodes.
- Compare `3` with `3` across the outside.
- Compare `4` with `4` across the inside.
- All mirror checks succeed.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- One node
- Matching values with mismatched structure

## Common Mistakes

- Comparing `left.left` with `right.left` instead of `right.right`
- Checking values only and ignoring missing-child structure
- Forgetting that an empty tree is symmetric

## Pattern Transfer

- 226.Invert Binary Tree
- Paired recursion on trees
- Mirror/structural comparison problems

## Self-Check

- Which child pairs must be compared for symmetry?
- Why is structure as important as values?
- What does `mirror(root, root)` mean?

## Function

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/101-symmetric-tree/python -q
```
