# 63.Unique Paths II

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count paths from the top-left to bottom-right of a grid when some cells are blocked by obstacles.

## Recognition Cues

- This is `Unique Paths`, but some cells cannot be used.
- The answer is still path counting on a grid.
- Obstacles zero out transitions.

## Baseline Idea

Recursively try moving right and down while checking obstacles. That repeats the same subproblems and gets slow.

## Core Insight

Use DP like `Unique Paths`, but whenever a cell has an obstacle, its path count becomes zero.

## Invariant / State

- `dp[j]` stores the number of ways to reach the current row at column `j`.
- Obstacle cells reset `dp[j]` to zero because no path may pass through them.

## Walkthrough

For
`[[0,0,0],[0,1,0],[0,0,0]]`:
- The obstacle blocks the center cell.
- Paths accumulate around it from top and left.
- Final answer is `2`.

## Complexity

- Time: `O(m * n)`
- Space: `O(n)`

## Edge Cases

- Start cell blocked
- End cell blocked
- Single row or column with obstacles

## Common Mistakes

- Forgetting to zero out blocked cells
- Carrying path counts through obstacles
- Reusing the recurrence from `Unique Paths` without obstacle handling

## Pattern Transfer

- 62.Unique Paths
- Grid DP with forbidden states
- Minimum path sum with blocked cells

## Self-Check

- What should happen if the starting cell is an obstacle?
- Why must `dp[j]` become zero at blocked cells?
- How is this recurrence different from obstacle-free unique paths?

## Function

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/63-unique-paths-ii/python -q
```
