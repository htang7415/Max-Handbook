# 337.House Robber III

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum money you can rob from a binary tree when you cannot rob directly connected nodes.

## Recognition Cues

- This is the house-robber rule on a tree instead of a line or circle.
- A node's choice affects its children.
- Each subtree naturally returns two answers: rob this node or skip it.

## Baseline Idea

At each node, recursively try robbing it or skipping it and take the better total. That works conceptually, but recomputes many overlapping subtree cases.

## Core Insight

Use tree DP. For each node, return:
- `rob_this`: best total if this node is robbed
- `skip_this`: best total if this node is skipped

If you rob the node, both children must be skipped. If you skip the node, each child can choose its better state.

## Invariant / State

- `dfs(node)` returns a pair `(rob_this, skip_this)` for that subtree.

## Walkthrough

For `[3, 2, 3, None, 3, None, 1]`:
- If you rob the root `3`, you must skip `2` and `3`.
- Then you may still rob grandchildren `3` and `1`.
- That yields total `7`, which is optimal.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single node
- Tree where skipping the root is better than robbing it

## Common Mistakes

- Treating it like the linear house robber problem
- Returning only one value per subtree instead of rob/skip states
- Forgetting that grandchildren can still be used when the current node is robbed

## Pattern Transfer

- 198.House Robber
- Tree DP with multiple states
- Postorder-style subtree aggregation

## Self-Check

- What do the two returned values mean?
- Why does robbing a node force both children into the skip state?
- Why is the final answer `max(rob_root, skip_root)`?

## Function

```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/337-house-robber-iii/python -q
```
