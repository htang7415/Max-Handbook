# 134.Gas Station

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Return the starting gas station index that allows a full circuit, or `-1` if impossible.

## Recognition Cues

- You need one valid start, not all starts.
- A failed segment invalidates every station inside that segment as a start.
- Total surplus versus deficit determines whether any solution exists.

## Baseline Idea

Try every station as a starting point and simulate the whole circuit. That works, but it is quadratic.

## Core Insight

If the running tank becomes negative while starting from `start`, then every station between `start` and the failure point also fails. So reset the start to the next station. A valid answer exists only if total gas is at least total cost.

## Invariant / State

- `tank` is the fuel left while testing the current candidate start.
- `total` tracks whether the entire instance is feasible at all.

## Walkthrough

For `gas = [1, 2, 3, 4, 5]` and `cost = [3, 4, 5, 1, 2]`:
- Early starts fail because the running tank drops below zero.
- Resetting eventually lands on station `3`.
- From station `3`, the full circuit is possible.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Impossible total gas
- One station
- Failure very late in the scan

## Common Mistakes

- Forgetting to check total feasibility
- Not resetting the start after a negative running tank
- Assuming a failed station only invalidates itself

## Pattern Transfer

- Greedy reset when a prefix becomes impossible
- Prefix-surplus reasoning
- Circular route feasibility

## Self-Check

- Why does a negative tank invalidate every station in the failed segment?
- Why is total gas versus total cost the global feasibility check?
- What does resetting `start` accomplish?

## Function

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/134-gas-station/python -q
```
