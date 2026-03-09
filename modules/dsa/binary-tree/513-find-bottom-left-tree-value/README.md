# 513.Find Bottom Left Tree Value

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Find the leftmost value in the last row of the tree.

## Recognition Cues

- The answer depends on tree depth and left-to-right level order.
- BFS naturally groups nodes by level.
- Only the first node of each level matters.

## Baseline Idea

Compute all levels and then take the first value of the last level. That works, but BFS can track the needed value on the fly.

## Core Insight

Run BFS level by level and record the first node in the queue at each level. The last recorded value is the answer.

## Invariant / State

- At the start of each BFS level, `queue[0]` is the leftmost node of that level.
- `leftmost` always stores the leftmost value of the most recently started level.

## Walkthrough

For `[1, 2, 3, 4, None, 5, 6, None, None, 7]`:
- Level starts with `1`, then `2`, then `4`, then `7`.
- The last recorded leftmost value is `7`.

## Complexity

- Time: `O(n)`
- Space: `O(w)` where `w` is the max width

## Edge Cases

- Single-node tree
- One-sided tree
- Deeper right subtree with a lower leftmost node

## Common Mistakes

- Tracking the first node seen overall instead of per level
- Using DFS without careful depth tracking
- Assuming the deepest left child is always the answer

## Pattern Transfer

- 102.Binary Tree Level Order Traversal
- BFS level tracking
- Bottom/left view tree problems

## Self-Check

- Why does `queue[0]` represent the leftmost node of a level?
- When is `leftmost` updated?
- Why does BFS fit this problem naturally?

## Function

```python
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/513-find-bottom-left-tree-value/python -q
```
