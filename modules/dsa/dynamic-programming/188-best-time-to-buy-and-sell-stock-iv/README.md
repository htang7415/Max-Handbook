# 188.Best Time to Buy and Sell Stock IV

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum stock profit when you may complete at most `k` transactions.

## Recognition Cues

- The number of allowed transactions is part of the input.
- Each transaction adds another buy/sell stage.
- This extends the stock-state DP pattern from the smaller stock problems.

## Baseline Idea

Try every possible set of transaction boundaries recursively and keep the best answer. That works conceptually, but it repeats too many overlapping choices.

## Core Insight

Track `k` buy states and `k` sell states. `buy[i]` is the best balance after the `i + 1`th buy, and `sell[i]` is the best profit after the `i + 1`th sell. Each new price updates all transaction stages. If `k` is very large, the problem collapses to the unlimited-transactions version.

## Invariant / State

- `buy[i]` is the best profit balance after performing exactly `i + 1` buys and at most `i` sells.
- `sell[i]` is the best profit after performing exactly `i + 1` sells.

## Walkthrough

For `k = 2` and `[3, 2, 6, 5, 0, 3]`:
- The first buy/sell pair can earn `4` by buying at `2` and selling at `6`.
- The second buy/sell pair can earn `3` by buying at `0` and selling at `3`.
- The DP states combine those into a total profit of `7`.

## Complexity

- Time: `O(nk)`
- Space: `O(k)`

## Edge Cases

- `k = 0`
- Empty price list
- `k` large enough to behave like unlimited transactions
- No profitable trades

## Common Mistakes

- Treating it like the one-transaction or two-transaction stock problems
- Forgetting the unlimited-transactions shortcut when `k` is large
- Mixing up what a buy state and a sell state represent

## Pattern Transfer

- 121, 122, 123 stock DP variants
- Small-state DP generalized by transaction count
- Finite-state trading problems

## Self-Check

- What does `buy[i]` mean?
- Why can large `k` be reduced to unlimited transactions?
- How does transaction `i` depend on transaction `i - 1`?

## Function

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/188-best-time-to-buy-and-sell-stock-iv/python -q
```
