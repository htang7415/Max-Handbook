# 455.Assign Cookies

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Assign cookies to maximize the number of content children.

## Recognition Cues

- Each child needs one resource with a minimum threshold.
- Small resources should not be wasted on easy targets if avoidable.
- Sorting can expose the locally optimal assignment order.

## Baseline Idea

Try all cookie-child assignments and take the best count. That is combinatorial.

## Core Insight

Sort both lists and always give the smallest available cookie that can satisfy the current least-greedy child.

## Invariant / State

- Children before index `child` are already content.
- Processed cookies before the current one have been used as efficiently as possible.

## Walkthrough

For greed `[1, 2, 3]` and cookies `[1, 1]`:
- The first cookie satisfies the child with greed `1`.
- The second cookie is too small for greed `2`.
- Only one child is content.

## Complexity

- Time: `O(n log n + m log m)` for sorting
- Space: depends on sort implementation, otherwise `O(1)` extra

## Edge Cases

- No cookies
- More cookies than children
- Several children with the same greed

## Common Mistakes

- Giving large cookies to easy children too early
- Sorting only one of the two lists
- Advancing the child pointer when the cookie is too small

## Pattern Transfer

- Interval/resource matching greedy problems
- Scheduling with sorted constraints
- Minimum feasible assignment strategies

## Self-Check

- Why is the smallest feasible cookie the right choice?
- What does the `child` pointer represent?
- Why can a cookie that is too small be discarded immediately?

## Function

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/455-assign-cookies/python -q
```
