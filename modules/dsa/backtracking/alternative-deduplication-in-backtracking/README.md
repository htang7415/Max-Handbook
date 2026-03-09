# Alternative Deduplication in Backtracking

> Track: `dsa` | Topic: `backtracking`

## What This Module Covers

This note shows a depth-local deduplication strategy: use a fresh set at each recursion level to avoid taking the same value twice from sibling branches.

## Recognition Cues

- The input contains duplicates.
- You want unique results without overcomplicating global state.
- Duplicate handling depends on "same tree level" rather than "same tree path".

## Core Ideas

- A local set tracks which values have already been used at the current depth.
- Sibling branches must not start from the same value twice.
- This approach is often clearer than global used-state when duplicate control is the main difficulty.

## Common Mistakes

- Reusing one set across all depths.
- Confusing duplicate skipping on the same level with duplicate skipping along one path.
- Accidentally banning valid repeated values that occur at different depths.

## Connections

- `Subsets II` and `Permutations II`.
- Sorted-input skip rules versus depth-local deduplication.
- Backtracking templates with repeated input values.

## Self-Check

- Why must the dedup set be recreated at each depth?
- What does "same level" mean in the recursion tree?
- When is sorting-plus-skip enough, and when is a local set clearer?

## Function

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
```
