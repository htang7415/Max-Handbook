# 454.4Sum II

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Count how many quadruples `(i, j, k, l)` satisfy `nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0`.

## Recognition Cues

- Four nested loops would be too slow.
- The condition splits naturally into two pair sums.
- You need a count of combinations, not the quadruples themselves.

## Baseline Idea

Try all quadruples directly. That takes `O(n^4)`.

## Core Insight

Precompute counts of pair sums from the first two arrays. Then for each pair from the other two arrays, look up how many complements make the total zero.

## Invariant / State

- `counts[s]` is the number of ways to form sum `s` using one value from `nums1` and one from `nums2`.
- Each pair from `nums3` and `nums4` contributes `counts[-(c + d)]` answers.

## Walkthrough

For `[1, 2]`, `[-2, -1]`, `[-1, 2]`, `[0, 2]`:
- First two arrays create sums like `-1`, `0`, `1`.
- Later pairs ask for complementary sums.
- Total matches add up to `2`.

## Complexity

- Time: `O(n^2)`
- Space: `O(n^2)`

## Edge Cases

- Many zeros
- Negative and positive values mixed
- Repeated values that increase the count

## Common Mistakes

- Returning unique quadruples instead of the count
- Forgetting that repeated pair sums contribute multiple times
- Building complements from the wrong pair of arrays

## Pattern Transfer

- 1.Two Sum
- Pair-sum hashing
- Meet-in-the-middle counting

## Self-Check

- Why is `O(n^2)` possible here?
- What exactly does the hash map count?
- Why do repeated values matter to the final answer?

## Function

```python
def four_sum_count(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/454-4sum-ii/python -q
```
