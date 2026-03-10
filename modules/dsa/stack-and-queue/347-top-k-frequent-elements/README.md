# 347.Top K Frequent Elements

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Return the `k` values that appear most often in the array.

## Recognition Cues

- Frequency counting is the first step.
- You need the top `k`, not a fully sorted order of everything.
- A min-heap lets you keep only the best `k` candidates seen so far.

## Baseline Idea

Count the values, sort all `(value, frequency)` pairs by frequency, then take the first `k`. That works, but it sorts more than needed.

## Core Insight

After counting frequencies, keep a min-heap of size `k`. If a new value is more frequent than the smallest heap entry, replace it.

## Invariant / State

- The heap stores at most `k` pairs `(frequency, value)`.
- The heap root is the weakest current top-`k` candidate.

## Walkthrough

For `[1, 1, 1, 2, 2, 3]` with `k = 2`:
- Count frequencies: `1 -> 3`, `2 -> 2`, `3 -> 1`.
- Push `(3, 1)`, `(2, 2)`, and `(1, 3)` into a min-heap while trimming it back to size `2`.
- The heap ends with the two most frequent values: `1` and `2`.

## Complexity

- Time: `O(n log k)`
- Space: `O(n)` for counts plus `O(k)` for the heap

## Edge Cases

- One element
- `k` equals the number of distinct values
- Negative numbers

## Common Mistakes

- Sorting all values when a bounded heap is enough
- Forgetting to pop when the heap grows beyond size `k`
- Forgetting that the result order within the top `k` does not matter here

## Pattern Transfer

- Frequency counting with `Counter`
- Heap-based top-`k` selection
- Top-`k` selection problems

## Self-Check

- Why does the heap root represent the weakest current top-`k` choice?
- Why is it safe to discard the heap root when the heap grows past size `k`?
- When does result order matter, and when does it not?

## Function

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/347-top-k-frequent-elements/python -q
```
