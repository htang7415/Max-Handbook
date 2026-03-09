# 763.Partition Labels

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Partition the string so each letter appears in at most one part, and return the part sizes.

## Recognition Cues

- A partition can close only after all letters inside it are finished.
- The last occurrence of each character determines how far a part must extend.
- Greedily closing as soon as possible produces the most partitions.

## Baseline Idea

Try every partitioning of the string and check whether characters stay inside one part. That works, but it is far too expensive.

## Core Insight

Precompute the last index of every character. While scanning the string, keep extending the current partition end to the farthest last occurrence of any character seen so far. When the scan reaches that end, close the partition.

## Invariant / State

- `end` is the farthest last occurrence among all characters in the current partition.

## Walkthrough

For `"ababcbacadefegdehijhklij"`:
- The first partition keeps expanding until index `8`
- The next closes at index `15`
- The last closes at the end
- The partition sizes are `[9, 7, 8]`

## Complexity

- Time: `O(n)`
- Space: `O(1)` relative to alphabet size

## Edge Cases

- One character
- Entire string must stay together
- Repeated letters spread far apart

## Common Mistakes

- Closing a partition before all its letters reach their last occurrence
- Forgetting to update the partition end while scanning inside it
- Returning boundaries instead of lengths

## Pattern Transfer

- Greedy interval expansion
- Last-occurrence preprocessing
- Segmenting while preserving local constraints

## Self-Check

- Why does the partition end depend on the farthest last occurrence?
- When is it safe to close a partition?
- Why is the greedy earliest-close rule optimal?

## Function

```python
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/763-partition-labels/python -q
```
