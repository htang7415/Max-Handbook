# 17.Letter Combinations of a Phone Number

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Generate all letter combinations that the digit string could represent on a phone keypad.

## Recognition Cues

- Each position offers a small set of choices.
- You need all possible strings.
- The output length equals the number of digits.

## Baseline Idea

Build combinations iteratively by expanding partial strings. That works, but backtracking expresses the choice tree directly.

## Core Insight

At position `index`, choose one letter from the current digit’s mapping, append it to the path, and recurse to the next digit.

## Invariant / State

- `path` holds one partial combination.
- `index` is the digit currently being expanded.
- When `index == len(digits)`, the path is a complete answer.

## Walkthrough

For `"23"`:
- Digit `2` gives `a`, `b`, `c`.
- For each of those, digit `3` gives `d`, `e`, `f`.
- This yields `9` total two-letter combinations.

## Complexity

- Time: proportional to the number of generated combinations
- Space: `O(len(digits))` auxiliary recursion depth

## Edge Cases

- Empty input
- One digit
- Digits like `7` and `9` that map to four letters

## Common Mistakes

- Forgetting to return `[]` for empty input
- Appending the path before all digits are processed
- Not popping the chosen letter during backtracking

## Pattern Transfer

- 77.Combinations
- 46.Permutations
- Product-of-choices backtracking

## Self-Check

- What does each recursion level correspond to?
- Why is the empty input special?
- How does a digit with four letters change the branching factor?

## Function

```python
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/17-letter-combinations-of-a-phone-number/python -q
```
