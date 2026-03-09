# 18.4Sum

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Return all unique quadruplets whose values sum to the target.

## Recognition Cues

- Four nested loops would be too slow.
- The target equation can be split into two pair sums.
- You need unique quadruplets, not just the count.

## Baseline Idea

Try every quadruple directly. That takes `O(n^4)`.

## Core Insight

Precompute earlier pair sums in a hash table. For each later pair, look up the complementary sum needed to reach the target.

## Invariant / State

- `pair_sums[s]` stores index pairs seen so far whose values sum to `s`.
- Each later pair checks whether an earlier pair completes the target.
- Sorted tuples in `result` deduplicate quadruplets by value.

## Walkthrough

For `[1, 0, -1, 0, -2, 2]` with target `0`:
- Earlier pairs build sums like `1`, `0`, and `-1`.
- Later pairs look up the needed complementary sums.
- Valid quadruplets such as `[-2, -1, 1, 2]` and `[-2, 0, 0, 2]` are collected.

## Complexity

- Time: `O(n^3)` in this implementation
- Space: `O(n^2)`

## Edge Cases

- No valid quadruplets
- Repeated values
- All values equal with one valid answer

## Common Mistakes

- Returning duplicate quadruplets
- Allowing the same index to be reused
- Building pair sums too late to match with future pairs

## Pattern Transfer

- 454.4Sum II
- 15.3Sum
- Pair-sum hashing with deduplication

## Self-Check

- Why are pair sums the right decomposition here?
- What does the hash table store?
- Why is deduplication still needed after using indices?

## Function

```python
def four_sum(nums: list[int], target: int) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/18-4sum/python -q
```
