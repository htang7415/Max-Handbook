# 96.Unique Binary Search Trees

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many structurally unique BSTs can be built using values `1..n`.

## Recognition Cues

- You are counting structures, not building them.
- Choosing a root splits the values into left and right subtrees.
- The number of BSTs for `n` depends on all smaller subtree sizes.

## Baseline Idea

Recursively try every possible root and count all resulting left/right subtree combinations. That works, but it repeats the same subtree-size counts.

## Core Insight

Let `dp[i]` be the number of unique BSTs using `i` nodes. For each possible root, the left subtree size and right subtree size multiply, because every left structure can pair with every right structure.

## Invariant / State

- `dp[i]` stores the number of BST structures possible with exactly `i` nodes.

## Walkthrough

For `n = 3`:
- Root `1` gives left size `0`, right size `2`
- Root `2` gives left size `1`, right size `1`
- Root `3` gives left size `2`, right size `0`
- Adding those products yields `5`

## Complexity

- Time: `O(n^2)`
- Space: `O(n)`

## Edge Cases

- `n = 1`
- Small base cases `n = 0` and `n = 1`

## Common Mistakes

- Forgetting that left and right subtree counts multiply
- Missing the empty-tree base case `dp[0] = 1`
- Confusing BST count with BST construction

## Pattern Transfer

- Catalan-number style DP
- Count-by-root decomposition
- Structural counting over smaller sizes

## Self-Check

- Why do left and right subtree counts multiply?
- Why is `dp[0] = 1` instead of `0`?
- What does `dp[i]` represent?

## Function

```python
class Solution:
    def numTrees(self, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/96-unique-binary-search-trees/python -q
```
