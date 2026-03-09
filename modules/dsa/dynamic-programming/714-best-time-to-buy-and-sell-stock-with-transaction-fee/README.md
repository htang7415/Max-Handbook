# 714.Best Time to Buy and Sell Stock with Transaction Fee

> Track: `dsa` | Topic: `dynamic-programming`

## Problem in One Line

Find the maximum stock profit when every sale pays a transaction fee.

## Recognition Cues

- Trading is unlimited, but each completed sale has a cost.
- A small buy/hold state machine still works.
- The fee changes the sell transition, not the buy rule.

## Baseline Idea

Enumerate all valid transaction sequences and subtract the fee from every sell. That works, but it repeats many states.

## Core Insight

Track:
- `cash`: best profit while not holding a stock
- `hold`: best profit while holding a stock

When selling, subtract the fee from the gained profit.

## Invariant / State

- `cash` is the best finished profit after the current day.
- `hold` is the best balance after the current day while owning one stock.

## Walkthrough

For `[1, 3, 2, 8, 4, 9]` with fee `2`:
- Buy at `1`, sell at `8` for profit `5`
- Buy at `4`, sell at `9` for profit `3`
- Total becomes `8`

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- One day
- Fee larger than every possible gain
- Rising prices where multiple trades still help after fees

## Common Mistakes

- Subtracting the fee on buy instead of sell without adjusting the state meaning
- Mixing this up with the cooldown variant
- Updating `hold` using an already-updated `cash` value

## Pattern Transfer

- Stock state-machine DP
- 122 and 309 stock variants
- Small-state rolling DP

## Self-Check

- What do `cash` and `hold` represent?
- Where should the fee be applied?
- Why do previous-state values matter during the update?

## Function

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/dynamic-programming/714-best-time-to-buy-and-sell-stock-with-transaction-fee/python -q
```
