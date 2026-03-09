# 343.Integer Break

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Split the integer into at least two positive integers so their product is as large as possible.

## Recognition Cues

- You must split the number at least once.
- The target is a maximum product, not a sum.
- Smaller optimal products can be reused inside larger splits.

## Baseline Idea

Try every partition recursively and compute the best product. That works, but repeated subproblems make it inefficient.

## Core Insight

Let `dp[i]` be the best product obtainable by breaking integer `i`. For each split `i = j + (i - j)`, consider either stopping at the raw remainder or further breaking it with `dp[i - j]`.

## Invariant / State

- `dp[i]` stores the best product achievable after splitting `i` at least once.

## Walkthrough

For `n = 10`:
- Splits like `1 + 9`, `2 + 8`, `3 + 7`, and so on are considered.
- The best route is `3 + 3 + 4`, giving product `36`.

## Complexity

- Time: `O(n^2)`
- Space: `O(n)`

## Edge Cases

- `n = 2`
- `n = 3`
- Values where one side should keep splitting and the other should not

## Common Mistakes

- Forgetting that at least one split is required
- Using only `j * (i - j)` and missing the case where the remainder should keep splitting
- Not seeding the small base cases correctly

## Pattern Transfer

- Maximize-value DP over partitions
- Rod-cutting style transitions
- Choosing between stopping and continuing a split

## Self-Check

- Why do we compare `j * (i - j)` and `j * dp[i - j]`?
- Why is `dp[2] = 1`?
- Why must the number be split at least once?

## Function

```python
class Solution:
    def integerBreak(self, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/343-integer-break/python -q
```
