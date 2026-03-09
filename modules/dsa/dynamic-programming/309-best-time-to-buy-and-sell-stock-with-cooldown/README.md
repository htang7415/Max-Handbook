# 309.Best Time to Buy and Sell Stock with Cooldown

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum stock profit when you must wait one day after selling before buying again.

## Recognition Cues

- Transactions are unlimited, but selling creates a one-day restriction.
- The cooldown changes what states are reachable on the next day.
- A small state machine is natural.

## Baseline Idea

Try every sequence of buys, sells, and waits recursively. That models the rules, but it repeats too many states.

## Core Insight

Track three states:
- `hold`: best profit while holding a stock
- `sold`: best profit on the day you just sold
- `rest`: best profit while not holding and not in a just-sold state

The cooldown is enforced because buying can only transition from `rest`, not from `sold`.

## Invariant / State

- `hold`, `sold`, and `rest` summarize every valid way to end the current day.

## Walkthrough

For `[1, 2, 3, 0, 2]`:
- Buy at `1`, sell at `3`.
- The next day is cooldown, so you cannot buy immediately after that sell.
- Buy later at `0`, then sell at `2`.
- Total profit becomes `3`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty input
- One day
- Prices where one long hold beats multiple short trades

## Common Mistakes

- Allowing a buy immediately after a sell
- Collapsing `sold` and `rest` into one state
- Updating states in the wrong order without saving previous values

## Pattern Transfer

- Stock state-machine DP
- 122 unlimited-transactions stock DP
- Finite-state DP with constraints

## Self-Check

- Why can buying come only from `rest`?
- What is the difference between `sold` and `rest`?
- Why must previous-state values be saved before updating?

## Function

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/309-best-time-to-buy-and-sell-stock-with-cooldown/python -q
```
