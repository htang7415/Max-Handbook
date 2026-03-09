# 968.Binary Tree Cameras

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Place the fewest cameras so every tree node is monitored.

## Recognition Cues

- A camera covers its parent, itself, and its children.
- Coverage decisions depend on child states.
- Postorder greedy decisions work because children should be resolved first.

## Baseline Idea

Try all possible camera placements and keep the smallest valid set. That works conceptually, but it is exponential.

## Core Insight

Do a postorder DFS and classify each node as:
- `0`: not covered
- `1`: has a camera
- `2`: covered without a camera

If any child is uncovered, place a camera at the current node. This postpones cameras upward and avoids wasting them on leaves.

## Invariant / State

- `dfs(node)` returns the coverage state of that subtree root after greedily minimizing cameras below it.

## Walkthrough

For a small chain-like tree:
- Leaves report uncovered to their parent
- Their parent places a camera
- That camera covers itself, its children, and its parent
- The root gets one only if it remains uncovered at the end

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- One node
- Skewed tree

## Common Mistakes

- Placing cameras on leaves too early
- Forgetting to check whether the root is uncovered after DFS
- Collapsing the three states into fewer than needed

## Pattern Transfer

- Postorder greedy on trees
- State-based tree traversal
- Place resources at parents when children demand them

## Self-Check

- Why are leaves treated as uncovered instead of immediately getting cameras?
- Why is postorder traversal necessary?
- When must the root receive an extra camera after DFS?

## Function

```python
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/968-binary-tree-cameras/python -q
```
