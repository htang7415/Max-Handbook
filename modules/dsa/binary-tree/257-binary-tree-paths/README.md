# 257.Binary Tree Paths

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return every root-to-leaf path as a string like `"1->2->5"`.

## Recognition Cues

- You need all root-to-leaf paths.
- The answer is built along traversal, not computed as one aggregate number.
- Leaves are the stopping condition.

## Baseline Idea

Traverse the tree and reconstruct paths afterward from parent pointers. That adds unnecessary bookkeeping.

## Core Insight

Use DFS while carrying the path string built so far. When you hit a leaf, record the completed path.

## Invariant / State

- `path` represents the root-to-current-node path prefix.
- A leaf finalizes exactly one full path string.

## Walkthrough

For `[1,2,3,None,5]`:
- Go left to build `"1->2->5"`.
- Go right to build `"1->3"`.
- Return both strings.

## Complexity

- Time: proportional to all nodes plus path-string construction
- Space: `O(h)` recursion depth, excluding output

## Edge Cases

- Empty tree
- Single-node tree
- One-sided tree

## Common Mistakes

- Recording paths at internal nodes instead of only leaves
- Forgetting separators between node values
- Mutating one shared path string incorrectly

## Pattern Transfer

- 112.Path Sum
- Root-to-leaf DFS traversal
- Tree path accumulation problems

## Self-Check

- When is a node a leaf for this problem?
- Why are paths recorded only at leaves?
- What does the recursive `path` argument represent?

## Function

```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/257-binary-tree-paths/python -q
```
