# 51.N-Queens

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Place `n` queens on an `n x n` board so no two queens attack each other, and return all valid boards.

## Recognition Cues

- This is a constraint-satisfaction search problem.
- Choices are made row by row.
- Invalid partial boards should be pruned immediately.

## Baseline Idea

Try every board configuration and filter valid ones. That is infeasible because the search space is huge.

## Core Insight

Place one queen per row and track blocked columns and diagonals so invalid positions are skipped before recursing deeper.

## Invariant / State

- `cols` stores used columns.
- `diag1` stores used `row - col` diagonals.
- `diag2` stores used `row + col` diagonals.
- Rows before the current one already have exactly one valid queen each.

## Walkthrough

For `n = 4`:
- Try one queen in row `0`.
- Only safe columns are considered in row `1`.
- Continue until a full valid board is built or the branch fails and backtracks.

## Complexity

- Time: exponential, heavily reduced by pruning
- Space: `O(n)` auxiliary recursion depth and constraint sets

## Edge Cases

- `n = 1`
- `n = 2` and `n = 3` with no solutions
- Small boards where pruning is easy to visualize

## Common Mistakes

- Forgetting diagonal conflicts
- Using the wrong diagonal identifiers
- Failing to undo state during backtracking

## Pattern Transfer

- Sudoku-style constraint backtracking
- 37.Sudoku Solver
- Row-by-row search with pruning

## Self-Check

- Why is one queen per row enough to enforce row safety?
- What do `row - col` and `row + col` represent?
- Why must every set update be undone on backtracking?

## Function

```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/51-n-queens/python -q
```
