# 122.Best Time to Buy and Sell Stock II

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Find the maximum profit when you may complete as many stock transactions as you want.

## Recognition Cues

- Unlimited transactions are allowed.
- Every positive day-to-day increase can be captured.
- Greedy accumulation replaces explicit buy/sell boundary search.

## Baseline Idea

Search for every possible set of buy and sell days and keep the best total profit. That works, but it is more complex than necessary.

## Core Insight

Any rising segment can be decomposed into consecutive positive differences. Summing all positive day-to-day gains captures the same total as buying at the segment start and selling at the end.

## Invariant / State

- `profit` is the total gain from all positive increases seen so far.

## Walkthrough

For `[7, 1, 5, 3, 6, 4]`:
- Take gain `5 - 1 = 4`
- Take gain `6 - 3 = 3`
- Total profit is `7`

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty input
- One day
- Prices always decreasing

## Common Mistakes

- Treating this like the one-transaction stock problem
- Overcomplicating the buy/sell boundaries
- Ignoring small positive increases that should be taken

## Pattern Transfer

- Greedy accumulation of local gains
- Stock problems with relaxed constraints
- 121 and DP stock variants

## Self-Check

- Why does summing positive differences equal the best total profit?
- Why is this different from the one-transaction version?
- What happens when prices only decrease?

## Function

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/122-best-time-to-buy-and-sell-stock-ii/python -q
```
