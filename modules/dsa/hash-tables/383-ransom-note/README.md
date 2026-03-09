# 383.Ransom Note

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Decide whether the ransom note can be formed using letters from the magazine, with each letter used at most once.

## Recognition Cues

- Available character counts are limited.
- Order does not matter; frequency does.
- This is a “can supply enough of each token?” problem.

## Baseline Idea

Search the magazine for each character in the ransom note and remove matches as you go. That is awkward and can be quadratic.

## Core Insight

Count magazine letters first, then subtract counts while scanning the ransom note. If any needed character runs out, return `False`.

## Invariant / State

- `counts[ch]` is the number of unused copies of `ch` still available from the magazine.

## Walkthrough

For `"aab"` from `"baa"`:
- Count magazine letters: `a:2, b:1`.
- Consume `a`, `a`, then `b`.
- All required letters are available, so return `True`.

## Complexity

- Time: `O(m + n)`
- Space: `O(k)` for distinct characters

## Edge Cases

- Empty ransom note
- Missing character entirely
- Not enough repeated copies of a character

## Common Mistakes

- Forgetting that each magazine character can only be used once
- Checking only membership instead of counts
- Building counts from the wrong string

## Pattern Transfer

- 242.Valid Anagram
- Frequency map problems
- Resource accounting with hash maps

## Self-Check

- What does a zero count mean?
- Why can membership alone be insufficient?
- Why is the magazine counted instead of the ransom note?

## Function

```python
def can_construct(ransom_note: str, magazine: str) -> bool:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/383-ransom-note/python -q
```
