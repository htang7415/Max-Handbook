# 474.Ones and Zeroes

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the largest number of strings you can choose with at most `m` zeroes and `n` ones.

## Recognition Cues

- Each string consumes two resources: zeroes and ones.
- Every string can be used at most once.
- This is a 2D 0/1 knapsack problem.

## Baseline Idea

Try every subset of strings and keep the largest valid one. That works, but it grows exponentially.

## Core Insight

Let `dp[i][j]` be the maximum number of strings you can build using at most `i` zeroes and `j` ones. For each string, update the table backward so the same string is not reused.

## Invariant / State

- `dp[i][j]` stores the best answer under capacities `i` zeroes and `j` ones.

## Walkthrough

For `["10", "0", "1"]` with `m = 1`, `n = 1`:
- `"10"` alone fits
- `"0"` and `"1"` together also fit
- The best answer is `2`

## Complexity

- Time: `O(len(strs) * m * n)`
- Space: `O(mn)`

## Edge Cases

- Zero capacities
- Strings that individually exceed the resource limits
- Many small strings competing for the same capacities

## Common Mistakes

- Updating the DP table forward and accidentally reusing a string
- Counting characters incorrectly
- Treating it like a one-dimensional knapsack

## Pattern Transfer

- Multi-dimensional 0/1 knapsack
- Resource-budget DP
- 416-style capacity reasoning with more than one constraint

## Self-Check

- What do the two DP dimensions represent?
- Why must both loops go backward?
- Why is this a 0/1 knapsack instead of a complete knapsack?

## Function

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/474-ones-and-zeroes/python -q
```
