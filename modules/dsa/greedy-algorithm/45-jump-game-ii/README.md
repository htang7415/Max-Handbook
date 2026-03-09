# 45.Jump Game II

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Return the minimum number of jumps needed to reach the last index.

## Recognition Cues

- You need the fewest jumps, not just reachability.
- A current jump defines a reachable window.
- Within that window, only the farthest next reach matters.

## Baseline Idea

Try every possible jump path and take the smallest count. That becomes exponential or quadratic depending on memoization.

## Core Insight

Scan the current reachable window and track the farthest next position. When you reach the end of the current window, you must commit to one more jump and expand the window.

## Invariant / State

- `current_end` is the farthest index reachable using the current number of jumps.
- `farthest` is the farthest index reachable with one more jump from within the current window.

## Walkthrough

For `[2, 3, 1, 1, 4]`:
- From index `0`, the first jump covers indices `1` and `2`.
- Inside that window, index `1` extends reach to `4`.
- When the window ends, take the second jump and finish.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Single-element array
- A large first jump reaches the end immediately
- Short windows that still extend far

## Common Mistakes

- Incrementing jumps at every index instead of only at window boundaries
- Confusing this problem with reachability-only Jump Game
- Updating `current_end` before fully scanning the current window

## Pattern Transfer

- 55.Jump Game
- Interval expansion greedy problems
- Minimum-step coverage problems

## Self-Check

- Why is it safe to delay taking a jump until the current window ends?
- What does `farthest` summarize?
- How is this different from the reachability version?

## Function

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/45-jump-game-ii/python -q
```
