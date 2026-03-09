# 15.3Sum

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Return all unique triplets whose values sum to zero.

## Recognition Cues

- The target sum is fixed at zero.
- You need unique triplets, not just a count or one solution.
- A complement lookup can reduce the inner search from pair scanning to set membership.

## Baseline Idea

Try all triples directly. That takes `O(n^3)`.

## Core Insight

Fix the first number, then scan the rest while storing seen values in a hash set. For each second number, check whether the needed third value has already appeared.

## Invariant / State

- For a fixed `first`, `seen` stores the values already considered as the second element.
- A sorted tuple in `result` ensures the same triplet is stored only once.

## Walkthrough

For `[-1, 0, 1, 2, -1, -4]`:
- Fix `-1`, then look for pairs summing to `1`.
- Encounter `0`, then `1`, which completes `[-1, 0, 1]`.
- Another branch finds `[-1, -1, 2]`.

## Complexity

- Time: `O(n^2)`
- Space: `O(n)` auxiliary space plus result storage

## Edge Cases

- No valid triplets
- Many zeros
- Repeated values that could create duplicate triplets

## Common Mistakes

- Returning duplicate triplets
- Forgetting that the same values can appear in different index orders
- Building complements against the wrong fixed value

## Pattern Transfer

- 1.Two Sum
- 454.4Sum II
- Meet-in-the-middle style sum problems

## Self-Check

- Why does fixing one value reduce the problem to a two-sum variant?
- Why is deduplication needed even with a hash set?
- What does the `seen` set contain for each outer loop iteration?

## Function

```python
def three_sum(nums: list[int]) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/15-3sum/python -q
```
