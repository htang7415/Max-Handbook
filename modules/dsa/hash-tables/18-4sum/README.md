# 18.4Sum

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Return all unique quadruplets whose values sum to the target.

## Recognition Cues

- Four nested loops would be too slow.
- Sorting helps manage duplicates and enables pruning.
- After fixing two values, the remaining task becomes a two-pointer search on a sorted suffix.

## Baseline Idea

Try every quadruple directly. That takes `O(n^4)`.

## Core Insight

Sort the array, fix the first two values, then use left and right pointers to search for the remaining pair. The sorted order makes both pruning and duplicate skipping straightforward.

## Invariant / State

- For fixed indices `i` and `j`, the pointers search only in the range to the right of `j`.
- Duplicate anchors and duplicate pointer values are skipped so each quadruplet appears once.

## Walkthrough

For `[1, 0, -1, 0, -2, 2]` with target `0`:
- Sort to `[-2, -1, 0, 0, 1, 2]`.
- Fix `-2`, then `-1`, and search with pointers.
- Repeat for the next anchor choices, skipping duplicates and collecting only unique quadruplets.

## Complexity

- Time: `O(n^3)` after sorting
- Space: `O(1)` extra space, ignoring output

## Edge Cases

- No valid quadruplets
- Repeated values
- All values equal with one valid answer

## Common Mistakes

- Returning duplicate quadruplets
- Forgetting to skip duplicates for the first or second anchor
- Moving the wrong pointer after comparing the sum to `target`

## Pattern Transfer

- 454.4Sum II
- 15.3Sum
- Sorted `k`-sum problems
- Two-pointer search after fixing anchors

## Self-Check

- Why is this one dimension harder than `3Sum`?
- Which loops or pointers need duplicate skipping?
- After fixing two numbers, what problem are the pointers solving?

## Function

```python
def four_sum(nums: list[int], target: int) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/18-4sum/python -q
```
