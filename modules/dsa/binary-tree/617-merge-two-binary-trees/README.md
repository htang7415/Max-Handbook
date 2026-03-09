# 617.Merge Two Binary Trees

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Merge two binary trees by summing overlapping nodes and keeping non-overlapping children.

## Recognition Cues

- The two trees must be traversed together.
- Matching positions combine; missing nodes fall through.
- A paired recursive merge fits naturally.

## Baseline Idea

Traverse one tree and separately insert values from the other by path. That is more complicated than direct paired recursion.

## Core Insight

At each pair of nodes:
- if one is missing, return the other
- if both exist, sum values and recursively merge their children

## Invariant / State

- `mergeTrees(root1, root2)` returns the merged subtree for those two positions.

## Walkthrough

For roots `1` and `2`:
- Merge to `3`.
- Recursively merge left children and right children.
- Keep any subtree that exists in only one tree.

## Complexity

- Time: `O(n)` over all visited nodes
- Space: `O(h)` recursion stack

## Edge Cases

- One tree is `None`
- Trees with disjoint shapes
- Single-node trees

## Common Mistakes

- Forgetting to preserve a non-`None` subtree when the other side is missing
- Mutating and losing references to child subtrees
- Assuming both trees always have the same shape

## Pattern Transfer

- 226.Invert Binary Tree
- 101.Symmetric Tree
- Paired recursion over two trees

## Self-Check

- What should be returned if one node is `None`?
- Why is paired recursion natural here?
- What part of the tree can be reused unchanged?

## Function

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/617-merge-two-binary-trees/python -q
```
