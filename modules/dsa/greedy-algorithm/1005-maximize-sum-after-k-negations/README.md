# 1005.Maximize Sum After K Negations

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Maximize the array sum after exactly `k` sign flips.

## Recognition Cues

- Each operation flips one number's sign.
- Large-magnitude negative values are the most profitable to flip early.
- If flips remain after all negatives are handled, only parity matters.

## Baseline Idea

Try all possible choices of which numbers to flip. That works in theory, but the search space grows quickly.

## Core Insight

Sort by absolute value descending. Greedily flip negative numbers with the largest absolute values first. After that, if `k` is still odd, flip the smallest-absolute-value number once more.

## Invariant / State

- After sorting by absolute value descending, earlier positions have the biggest impact on the sum.

## Walkthrough

For `[3, -1, 0, 2]` with `k = 3`:
- Sort by absolute value: `[3, 2, -1, 0]` up to ordering by abs.
- Flip `-1` to `1`.
- Two flips remain, but flipping `0` changes nothing.
- The maximum sum is `6`.

## Complexity

- Time: `O(n log n)`
- Space: `O(1)` extra, ignoring sort internals

## Edge Cases

- Zero in the array
- All positive values
- More flips than negative numbers

## Common Mistakes

- Flipping small negatives before large negatives
- Forgetting that an odd leftover flip must be used
- Missing that zero absorbs any leftover flips harmlessly

## Pattern Transfer

- Greedy by largest immediate gain
- Sort by absolute impact
- Parity-sensitive greedy cleanup

## Self-Check

- Why are large-absolute-value negatives the best first flips?
- Why does only leftover parity matter at the end?
- Why is zero special here?

## Function

```python
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/1005-maximize-sum-after-k-negations/python -q
```
