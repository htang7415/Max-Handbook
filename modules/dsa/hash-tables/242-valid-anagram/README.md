# 242.Valid Anagram

> Track: `dsa` | Topic: `hash-tables`

## Problem in One Line

Decide whether two strings contain exactly the same characters with the same counts.

## Recognition Cues

- Character frequency matters more than order.
- A direct position-by-position comparison is useless.
- Counting occurrences is the natural summary.

## Baseline Idea

Sort both strings and compare them. That works, but sorting costs `O(n log n)`.

## Core Insight

Two strings are anagrams exactly when every character count balances out to zero.

## Invariant / State

- `counts[ch]` records how many more times `ch` appears in `s` than in the portion of `t` processed so far.

## Walkthrough

For `"anagram"` and `"nagaram"`:
- Count characters from the first string.
- Subtract counts using the second string.
- Every count returns to zero, so the strings are anagrams.

## Complexity

- Time: `O(n)`
- Space: `O(k)`, where `k` is the number of distinct characters

## Edge Cases

- Different lengths
- Empty strings
- Repeated characters

## Common Mistakes

- Forgetting to reject different lengths immediately
- Comparing only unique characters instead of counts
- Not handling repeated letters correctly

## Pattern Transfer

- 383.Ransom Note
- Frequency map problems
- Group Anagrams

## Self-Check

- Why does different length immediately imply `False`?
- What does a negative or missing count mean while scanning `t`?
- Why is counting faster than sorting here?

## Function

```python
def is_anagram(s: str, t: str) -> bool:
```

## Run tests

```bash
pytest modules/dsa/hash-tables/242-valid-anagram/python -q
```
