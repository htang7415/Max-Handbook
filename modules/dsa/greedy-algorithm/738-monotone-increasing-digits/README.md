# 738.Monotone Increasing Digits

> Track: `dsa` | Topic: `greedy-algorithm`

## Problem in One Line

Return the largest number less than or equal to `n` whose digits are monotonically nondecreasing.

## Recognition Cues

- The output must stay as large as possible while fixing digit order.
- A violation at one digit can cascade leftward.
- Once a digit is decreased, everything to its right should become `9`.

## Baseline Idea

Search downward from `n` until you find a monotone number. That works, but it can take many checks.

## Core Insight

Scan from right to left. When `digits[i] < digits[i-1]`, decrement `digits[i-1]` and remember that all digits to the right should eventually become `9`. This propagates the largest valid correction.

## Invariant / State

- `marker` is the first index that must be filled with `9`s after a decrease.

## Walkthrough

For `332`:
- Compare from the right and see `2 < 3`, so decrement the middle digit.
- Then see another violation and decrement the first digit.
- Fill the rest with `9`s to get `299`.

## Complexity

- Time: `O(d)` where `d` is the number of digits
- Space: `O(d)`

## Edge Cases

- Already monotone numbers
- Repeated equal digits
- Cascading decreases like `332`

## Common Mistakes

- Fixing only the first violation without propagating left
- Filling the tail with the wrong digit after a decrease
- Requiring strict increase instead of nondecreasing order

## Pattern Transfer

- Greedy digit repair
- Largest valid number under a constraint
- Right-to-left constraint propagation

## Self-Check

- Why does the suffix become all `9`s after a decrease?
- Why can fixing one digit create a new violation on the left?
- What does `marker` represent?

## Function

```python
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
```

## Run tests

```bash
pytest modules/dsa/greedy-algorithm/738-monotone-increasing-digits/python -q
```
