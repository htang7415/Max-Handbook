# 1.Two Sum

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Find the two indices whose values add up to `target`.

## Recognition Cues

- You need to match a value with its complement.
- Direct nested loops would be too slow.
- Fast lookup by value is more important than ordering.

## Baseline Idea

Check every pair of indices and return the one whose values sum to `target`. This works, but it takes `O(n^2)` time.

## Core Insight

While scanning the array once, store each earlier value in a hash map. For the current value `x`, check whether `target - x` was seen before.

## Invariant / State

`seen` maps each earlier value to an index where it already appeared.

## Walkthrough

For `nums = [2, 7, 11, 15]` and `target = 9`:
- See `2`, need `7`, not found yet.
- See `7`, need `2`, found at index `0`.
- Return `[0, 1]`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- Duplicate values like `[3, 3]`
- Negative numbers
- Zero as part of the answer

## Common Mistakes

- Returning values instead of indices
- Storing the current value before checking for its complement
- Accidentally reusing the same element twice

## Pattern Transfer

- 454.4Sum II
- 383.Ransom Note
- 349.Intersection of Two Arrays

## Self-Check

- Why do we check for the complement before inserting the current value?
- What makes the hash-map version `O(n)`?
- How do duplicates like `[3, 3]` still work?

## Function

```python
def two_sum(nums: list[int], target: int) -> list[int]:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/1-two-sum/python -q
```
