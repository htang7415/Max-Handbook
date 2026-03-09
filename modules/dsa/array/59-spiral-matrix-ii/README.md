# 59.Spiral Matrix II

> Track: `dsa` | Topic: `array`

## Problem in One Line

Generate an `n x n` matrix filled with `1` through `n^2` in spiral order.

## Recognition Cues

- You must fill a matrix layer by layer.
- Movement direction changes at boundaries.
- The answer is constructed rather than searched.

## Baseline Idea

Simulate movement one cell at a time with visited markers and direction changes. That works, but it adds extra state.

## Core Insight

Fill the matrix one ring at a time: top row, right column, bottom row, and left column, then move inward.

## Invariant / State

- `start_row` and `start_col` mark the top-left corner of the current ring.
- `offset` determines the right and bottom boundaries of the current ring.
- `value` is the next number to place.

## Walkthrough

For `n = 3`:
- Fill the outer ring with `1` through `8`.
- Place `9` in the center.

## Complexity

- Time: `O(n^2)`
- Space: `O(n^2)` for the output matrix

## Edge Cases

- `n = 1`
- Odd `n` with a center cell
- Even `n` with no center cell

## Common Mistakes

- Overwriting corners twice
- Using inconsistent loop boundaries for the four sides
- Forgetting the center cell when `n` is odd

## Pattern Transfer

- Spiral traversal of a matrix
- Layer-by-layer matrix construction
- Boundary management in 2D arrays

## Self-Check

- Why is the center cell handled separately for odd `n`?
- What does one ring contribute to the matrix?
- Which indices are inclusive or exclusive on each side?

## Function

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
```

## Run tests

```bash
pytest modules/dsa/array/59-spiral-matrix-ii/python -q
```
