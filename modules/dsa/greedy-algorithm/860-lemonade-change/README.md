# 860.Lemonade Change

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Decide whether you can give correct change to each customer in order.

## Recognition Cues

- Customers arrive in fixed order.
- Only `$5`, `$10`, and `$20` bills appear.
- Larger bills should be preserved when smaller change can cover future cases better.

## Baseline Idea

Try different ways of making change for each customer and see whether any full sequence works. That works, but it is unnecessary.

## Core Insight

Track how many `$5` and `$10` bills you have. For a `$20`, prefer giving one `$10` and one `$5` instead of three `$5`s, because `$5` bills are the most flexible resource.

## Invariant / State

- `five` and `ten` store exactly the bills available before serving the next customer.

## Walkthrough

For `[5, 5, 5, 10, 20]`:
- Collect three `$5`s
- Exchange one `$5` for the `$10` customer
- Use one `$10` and one `$5` to serve `$20`
- Change is possible throughout

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- First customer pays with `$10` or `$20`
- Exact inventory runs out late
- Many `$20` bills in a row

## Common Mistakes

- Using three `$5`s before a `$10 + $5` option
- Forgetting that order matters
- Tracking total money instead of exact bill counts

## Pattern Transfer

- Greedy resource allocation
- Preserve the most flexible resource
- Simulation with constrained inventory

## Self-Check

- Why is `$10 + $5` better than `5 + 5 + 5` for a `$20`?
- Why is total cash alone not enough to solve the problem?
- What bills must be tracked explicitly?

## Function

```python
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/860-lemonade-change/python -q
```
