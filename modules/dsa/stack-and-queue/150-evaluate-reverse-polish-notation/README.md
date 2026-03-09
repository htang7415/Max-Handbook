# 150.Evaluate Reverse Polish Notation

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Evaluate an arithmetic expression written in reverse Polish notation.

## Recognition Cues

- Operators come after their operands.
- Parentheses are unnecessary because evaluation order is implicit.
- The most recent numbers must be combined first.

## Baseline Idea

Reconstruct an infix expression and evaluate it later. That adds unnecessary parsing work.

## Core Insight

Use a stack: push numbers, and when an operator appears, pop the last two values, apply the operator, and push the result back.

## Invariant / State

- The stack stores the values of fully evaluated partial expressions.
- Before an operator is processed, its two operands are at the top of the stack.

## Walkthrough

For `["2", "1", "+", "3", "*"]`:
- Push `2`, push `1`.
- `+` makes `3`.
- Push `3`.
- `*` makes `9`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- A single number
- Negative numbers
- Division that must truncate toward zero

## Common Mistakes

- Popping operands in the wrong order for subtraction or division
- Using floor division instead of truncation toward zero
- Treating numeric tokens as operators

## Pattern Transfer

- 20.Valid Parentheses
- Stack-based expression evaluation
- Parsing arithmetic tokens

## Self-Check

- Why does operand order matter for `-` and `/`?
- What does each stack value represent?
- Why is `int(a / b)` used instead of `a // b` here?

## Function

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/150-evaluate-reverse-polish-notation/python -q
```
