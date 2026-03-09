# 494.Target Sum

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many ways you can assign `+` and `-` signs so the expression equals `target`.

## Recognition Cues

- Each number is assigned one of two signs.
- The task asks for a count of valid assignments.
- The problem can be transformed into counting subsets with a derived sum.

## Baseline Idea

Try every sign assignment recursively and count the successful ones. That works, but it explores `2^n` possibilities.

## Core Insight

Let the positive-sign subset sum be `P`. Since `P - (total - P) = target`, we get `2P = total + target`. So the problem becomes: count subsets whose sum is `(total + target) // 2`.

## Invariant / State

- `dp[s]` is the number of ways to choose a subset of the processed numbers with sum `s`.

## Walkthrough

For `[1, 1, 1, 1, 1]` and target `3`:
- Total is `5`, so subset target is `(5 + 3) / 2 = 4`.
- Count subsets that sum to `4`.
- There are `5` such choices, so the answer is `5`.

## Complexity

- Time: `O(n * subset)`
- Space: `O(subset)`

## Edge Cases

- Target larger than the total sum
- Parity mismatch where `total + target` is odd
- Zero values, which multiply the number of valid assignments

## Common Mistakes

- Missing the subset-sum transformation
- Forgetting to reject impossible parity or magnitude cases
- Iterating sums forward and reusing the same number multiple times

## Pattern Transfer

- Counted 0/1 knapsack
- 416.Partition Equal Subset Sum
- Sign-assignment to subset-sum transformation

## Self-Check

- How do you derive the subset target?
- Why do zeros increase the number of ways?
- Why must the sum loop go backward?

## Function

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/494-target-sum/python -q
```
