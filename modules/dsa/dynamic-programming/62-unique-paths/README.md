# 62.Unique Paths

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many ways there are to move from the top-left of an `m x n` grid to the bottom-right using only right and down moves.

## Recognition Cues

- You are counting paths on a grid.
- Each state depends on a small number of previous states.
- Moves are restricted to right and down.

## Baseline Idea

Recursively branch right and down from each cell. That repeats the same subproblems many times.

## Core Insight

The number of paths to a cell equals paths from above plus paths from the left.

## Invariant / State

- `dp[j]` stores the number of paths to the current row at column `j`.
- While scanning left to right, `dp[j]` is “from above” and `dp[j - 1]` is “from the left.”

## Walkthrough

For a `3 x 2` grid:
- First row is all `1`s.
- Second row becomes `[1, 2]`.
- Third row becomes `[1, 3]`.
- Answer is `3`.

## Complexity

- Time: `O(m * n)`
- Space: `O(n)`

## Edge Cases

- One row
- One column
- Small grids like `1 x 1`

## Common Mistakes

- Forgetting that the first row and first column each have exactly one path
- Mixing up rows and columns in the loops
- Recomputing all subproblems recursively

## Pattern Transfer

- 63.Unique Paths II
- Grid DP with obstacles
- Minimum path sum style DP

## Self-Check

- Why is the recurrence `top + left`?
- What does the 1D DP array represent?
- Why are the first row and first column all ones?

## Function

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/62-unique-paths/python -q
```
