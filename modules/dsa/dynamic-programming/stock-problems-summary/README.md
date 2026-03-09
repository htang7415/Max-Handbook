# Stock Problems Summary

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This summary organizes the stock DP family by constraints: one transaction, unlimited transactions, bounded transactions, cooldown, and transaction fee.

## Recognition Cues

- The state depends on whether you currently hold a stock.
- Extra rules add more state or restrict transitions.
- Most variants are finite-state DP, not large table DP.

## Core Ideas

- `hold` and `cash` are the base states.
- Bounded transactions add more buy/sell stages.
- Cooldown adds a "just sold" or rest distinction.
- Fees modify the sell transition.

## Common Mistakes

- Solving one stock variant with another variant's transition rules.
- Updating states in the wrong order.
- Forgetting whether the current state means "holding", "just sold", or "resting".

## Connections

- 121, 122, 123, 188, 309, and 714 are one family with different state constraints.
- Greedy stock solutions appear when constraints are loose enough.
- Small-state DP is a useful mental model beyond stock problems.

## Self-Check

- What are the minimal states for a given stock variant?
- Which extra rule changes the transition?
- When does a stock problem collapse to a greedy scan?
