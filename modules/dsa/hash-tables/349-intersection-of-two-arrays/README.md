# 349.Intersection of Two Arrays

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Return the unique values that appear in both arrays.

## Recognition Cues

- Membership matters more than ordering.
- Duplicates in the input should collapse in the output.
- Fast lookup by value is enough.

## Baseline Idea

Compare every pair of elements and track the common ones. That works, but it takes `O(n * m)` time.

## Core Insight

Convert both arrays to sets and intersect them, because sets naturally remove duplicates and support fast membership tests.

## Invariant / State

- Each set contains the unique values from one array.
- The set intersection contains exactly the values present in both.

## Walkthrough

For `[1, 2, 2, 1]` and `[2, 2]`:
- Unique values are `{1, 2}` and `{2}`.
- Their intersection is `{2}`.

## Complexity

- Time: `O(n + m)`
- Space: `O(n + m)`

## Edge Cases

- One array is empty
- No common values
- Many duplicate values

## Common Mistakes

- Returning duplicates instead of unique values
- Caring about output order when the problem does not require it
- Using a list for repeated membership checks

## Pattern Transfer

- 242.Valid Anagram
- 202.Happy Number
- Set-based deduplication problems

## Self-Check

- Why do sets solve the uniqueness requirement automatically?
- What happens if one input contains many repeated values?
- Why is output order not stable here?

## Function

```python
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/349-intersection-of-two-arrays/python -q
```
