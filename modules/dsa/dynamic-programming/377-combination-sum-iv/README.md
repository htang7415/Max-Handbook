# 377.Combination Sum IV

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Count how many ordered sequences of numbers add up to the target.

## Recognition Cues

- You are counting ways, not minimizing or maximizing.
- Order matters, so `[1, 2]` and `[2, 1]` are different answers.
- Prefix-sum style DP over target totals is natural.

## Baseline Idea

Recursively try every next number until the running sum reaches the target. That works, but it recomputes the same remaining totals many times.

## Core Insight

Let `dp[total]` be the number of ordered sequences that sum to `total`. For each total, every number `num` can be the last step if `total >= num`, so add `dp[total - num]`.

## Invariant / State

- `dp[t]` stores the number of ordered combinations that produce total `t`.
- `dp[0] = 1` because there is exactly one way to make total zero: choose nothing.

## Walkthrough

For `nums = [1, 2, 3]` and `target = 4`:
- `dp[1] = 1`
- `dp[2] = dp[1] + dp[0] = 2`
- `dp[3] = dp[2] + dp[1] + dp[0] = 4`
- `dp[4] = 7`

## Complexity

- Time: `O(target * len(nums))`
- Space: `O(target)`

## Edge Cases

- Target `0`
- No possible sequence
- Repeated small numbers creating many orderings

## Common Mistakes

- Counting unordered combinations instead of ordered sequences
- Forgetting that `dp[0] = 1`
- Swapping loop order and accidentally changing the meaning of the count

## Pattern Transfer

- Count DP over totals
- 518.Coin Change II for the unordered version
- Staircase / ways-to-reach-a-total problems

## Self-Check

- Why does order matter here but not in Coin Change II?
- What does `dp[t]` mean exactly?
- Why is `dp[0]` equal to `1`?

## Function

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/377-combination-sum-iv/python -q
```
