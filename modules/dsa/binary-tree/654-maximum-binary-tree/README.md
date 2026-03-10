# 654.Maximum Binary Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Build a binary tree where each subtree root is the maximum value in its subarray.

## Recognition Cues

- The tree structure is defined directly by array maxima.
- Each value's parent is the nearest greater value that survives on one side.
- A decreasing stack can maintain those greater-value relationships in one pass.

## Baseline Idea

For each subarray, scan for the maximum value, make it the root, and recurse on the left and right pieces. This matches the definition directly, but repeated scans can cost `O(n^2)`.

## Core Insight

Use a decreasing monotonic stack. When a larger value arrives, smaller stacked nodes become its left subtree; if a larger stacked node remains, the current node becomes that node's right child.

## Invariant / State

- The stack is strictly decreasing by node value.
- Every popped node is smaller than the current value, so it belongs in the current node's left subtree.
- If the stack is non-empty after popping, the current node is the right child of the nearest greater node on the left.

## Walkthrough

For `nums = [3, 2, 1, 6, 0, 5]`:
- Push `3`, `2`, `1` onto the decreasing stack.
- When `6` arrives, pop `1`, `2`, and `3`; the last popped chain becomes the left subtree of `6`.
- Push `0`, then when `5` arrives, pop `0` so it becomes the left child of `5`, and attach `5` as the right child of `6`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- Empty array
- Single-element array
- Strictly increasing or decreasing input

## Common Mistakes

- Forgetting to attach popped nodes as the current node's left child
- Overwriting the nearest greater left parent instead of attaching the current node as its right child
- Assuming the stack should be increasing instead of decreasing

## Pattern Transfer

- Cartesian tree construction
- Monotonic stack parent-child linking
- Next greater element style structure building

## Self-Check

- Why does the stack stay decreasing?
- Why does a popped node belong in the current node's left subtree?
- Why does the remaining stack top become the current node's parent on the left?

## Function

```python
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/654-maximum-binary-tree/python -q
```
