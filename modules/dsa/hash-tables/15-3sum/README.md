# 15.3Sum

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Return all unique triplets whose values sum to zero.

## Recognition Cues

- The target sum is fixed at zero.
- You need unique triplets, not just a count or one solution.
- Sorting can group duplicates and make pointer movement meaningful.
- After fixing one value, the remaining task becomes a two-pointer `2Sum` search.

## Baseline Idea

Try all triples directly. That takes `O(n^3)`.

## Core Insight

Sort the array, fix one number, then use left and right pointers to search the remaining pair. The sorted order lets pointer moves adjust the sum predictably, and duplicates can be skipped cleanly.

## Invariant / State

- For a fixed index `i`, pointers search only in the sorted suffix to the right.
- Duplicate anchor and pointer values are skipped so each triplet is recorded once.

## Walkthrough

For `[-1, 0, 1, 2, -1, -4]`:
- Sort to `[-4, -1, -1, 0, 1, 2]`.
- Fix `-1`, then move left and right pointers inward until the sum reaches `0`.
- Skip duplicate anchors and duplicate pointer values so `[-1, 0, 1]` and `[-1, -1, 2]` appear once each.

## Complexity

- Time: `O(n^2)`
- Space: `O(1)` extra space, ignoring output

## Edge Cases

- No valid triplets
- Many zeros
- Repeated values that could create duplicate triplets

## Common Mistakes

- Returning duplicate triplets
- Forgetting to sort before using two pointers
- Moving only one pointer after finding a valid triplet

## Pattern Transfer

- 1.Two Sum
- 454.4Sum II
- 18.4Sum
- Sorted `k`-sum reduction

## Self-Check

- Why does sorting make two-pointer movement valid?
- Why do duplicates need to be skipped at both the anchor and pointer levels?
- After fixing one value, what smaller problem remains?

## Function

```python
def three_sum(nums: list[int]) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/15-3sum/python -q
```
