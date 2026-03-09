# 198.House Robber

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Maximize the amount stolen without robbing two adjacent houses.

## Recognition Cues

- Each choice excludes its immediate neighbor.
- The answer is an optimal value, not the actual set of houses.
- The current decision depends on whether the previous house was used.

## Baseline Idea

Try all subsets of houses and discard those with adjacent choices. That is exponential.

## Core Insight

At each house, either skip it and keep the previous best, or rob it and add its value to the best answer from two houses back.

## Invariant / State

- `prev1` is the best answer up to the previous house.
- `prev2` is the best answer up to the house before that.

## Walkthrough

For `[2, 7, 9, 3, 1]`:
- Best after `2` is `2`.
- Best after `7` is `7`.
- Best after `9` is `11`.
- Continue to finish with `12`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty list
- One house
- A larger value that appears after a tempting adjacent choice

## Common Mistakes

- Summing all locally large houses without respecting adjacency
- Forgetting the empty-input case
- Using recursion without memoization

## Pattern Transfer

- 213.House Robber II
- 337.House Robber III
- Take-or-skip DP patterns

## Self-Check

- What do `prev1` and `prev2` mean?
- Why can the answer be tracked with only two states?
- What are the two options at each house?

## Function

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/198-house-robber/python -q
```
