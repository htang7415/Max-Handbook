# 202.Happy Number

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Repeatedly replace `n` by the sum of the squares of its digits and decide whether the process ends at `1`.

## Recognition Cues

- A transformation is applied over and over to a number.
- You must distinguish “reaches 1” from “loops forever.”
- Detecting repeated states is the key.

## Baseline Idea

Keep simulating and hope it reaches `1`. That can loop forever when the number is unhappy.

## Core Insight

If the process ever repeats a number, it is in a cycle and will never reach `1`. A hash set detects that cycle immediately.

## Invariant / State

- `seen` contains every intermediate number already produced.
- If `n` appears in `seen` again, the process has entered a loop.

## Walkthrough

For `19`:
- `1^2 + 9^2 = 82`
- `8^2 + 2^2 = 68`
- `6^2 + 8^2 = 100`
- `1^2 + 0^2 + 0^2 = 1`, so it is happy.

## Complexity

- Time: bounded by the number of generated states before repetition
- Space: `O(number of seen states)`

## Edge Cases

- `n = 1`
- Small unhappy numbers like `2`
- Values that quickly enter a cycle

## Common Mistakes

- Forgetting to detect repeated states
- Reusing the partially reduced `n` incorrectly while summing digits
- Assuming every sequence eventually reaches `1`

## Pattern Transfer

- Floyd cycle detection problems
- Digit transformation problems
- Repeated-state simulation

## Self-Check

- Why does seeing the same number twice prove a cycle?
- What does the hash set store?
- Why is `1` the only successful stopping state?

## Function

```python
def is_happy(n: int) -> bool:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/202-happy-number/python -q
```
