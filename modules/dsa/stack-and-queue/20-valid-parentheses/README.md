# 20.Valid Parentheses

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Decide whether every bracket is closed in the correct order.

## Recognition Cues

- Symbols must be matched in nested order.
- The most recent unmatched opener matters first.
- This is a natural LIFO problem.

## Baseline Idea

Repeatedly search backward for a matching opener. That becomes messy and inefficient.

## Core Insight

Push opening brackets onto a stack. When a closing bracket appears, it must match the most recent unmatched opener on top of the stack.

## Invariant / State

- The stack contains unmatched opening brackets.
- If the string is valid so far, the top of the stack is the only opener the next closer may match.

## Walkthrough

For `"{[]}"`:
- Push `{`.
- Push `[`.
- See `]`, match and pop `[`.
- See `}`, match and pop `{`.
- The stack is empty, so the string is valid.

## Complexity

- Time: `O(n)`
- Space: `O(n)` in the worst case

## Edge Cases

- Empty string
- A closing bracket appears first
- Leftover opening brackets at the end

## Common Mistakes

- Popping from an empty stack
- Matching against the wrong bracket type
- Forgetting to check that the stack is empty at the end

## Pattern Transfer

- 150.Evaluate Reverse Polish Notation
- 1047.Remove All Adjacent Duplicates in String
- Basic expression parsing

## Self-Check

- Why is a stack better than a queue here?
- What does a non-empty stack mean after the scan finishes?
- Why must a closer match the top element specifically?

## Function

```python
class Solution:
    def isValid(self, s: str) -> bool:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/20-valid-parentheses/python -q
```
