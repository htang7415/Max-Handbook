# 416.Partition Equal Subset Sum

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Decide whether the array can be split into two subsets with equal sum.

## Recognition Cues

- Equal partition means both subsets must sum to half of the total.
- Each number can be used at most once.
- This is a 0/1 subset-sum decision problem.

## Baseline Idea

Try every subset and check whether one of them sums to half of the total. That works, but it is exponential.

## Core Insight

If the total sum is odd, the answer is immediately false. Otherwise, target `total // 2` and use 0/1 knapsack DP to test whether that sum is reachable.

## Invariant / State

- `dp[t]` tells whether sum `t` is achievable from the numbers processed so far.

## Walkthrough

For `[1, 5, 11, 5]`:
- Total is `22`, so target is `11`.
- The subset `[11]` works, and so does `[5, 5, 1]`.
- Since `11` is reachable, the answer is true.

## Complexity

- Time: `O(n * target)`
- Space: `O(target)`

## Edge Cases

- Odd total sum
- One element
- Repeated values

## Common Mistakes

- Forgetting to reject odd totals immediately
- Iterating the target forward instead of backward for 0/1 choice
- Treating it like a complete knapsack where values can be reused

## Pattern Transfer

- 0/1 knapsack
- 1049.Last Stone Weight II
- Subset-sum reachability

## Self-Check

- Why does an odd total make the answer impossible?
- What does `dp[t]` mean?
- Why must the target loop go backward?

## Function

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/416-partition-equal-subset-sum/python -q
```
