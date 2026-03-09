# 112.Path Sum

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Decide whether the tree has any root-to-leaf path whose node values sum to the target.

## Recognition Cues

- The sum is accumulated along a root-to-leaf path.
- A valid match must end at a leaf, not any internal node.
- Recursion naturally carries the remaining sum down the tree.

## Baseline Idea

Generate every root-to-leaf path, compute each sum, and compare. That works, but it builds more path data than needed.

## Core Insight

Subtract the current node’s value from the target as you recurse. At a leaf, the path works exactly when the remaining sum equals the leaf’s value.

## Invariant / State

- `targetSum` in each recursive call means “sum still needed from this node downward.”

## Walkthrough

For target `22` on the classic example tree:
- Start at `5`, remaining `17`.
- Go to `4`, remaining `13`, then `11`, remaining `2`.
- At leaf `2`, the remaining sum matches, so return `True`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single-node tree
- A prefix sum matching the target before reaching a leaf

## Common Mistakes

- Returning `True` at any matching intermediate node
- Forgetting to subtract the current value before recursing
- Treating `None` as a valid path

## Pattern Transfer

- 257.Binary Tree Paths
- Root-to-leaf DFS problems
- Recursive accumulation on trees

## Self-Check

- Why must the path end at a leaf?
- What does the remaining target mean?
- What should happen on an empty tree?

## Function

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/112-path-sum/python -q
```
