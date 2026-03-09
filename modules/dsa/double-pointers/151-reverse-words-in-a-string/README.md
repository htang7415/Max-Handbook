# 151.Reverse Words in a String

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Reverse the order of words in the string while removing extra spaces.

## Recognition Cues

- Words are separated by irregular spaces.
- You need a cleaned string with single spaces between words.
- Reversal can be done in stages with pointer-based string processing.

## Baseline Idea

Split on whitespace, reverse the list of words, and join them again. That is simple, but it skips the pointer-based in-place reasoning this topic is meant to teach.

## Core Insight

Compact spaces first, reverse the entire character sequence, then reverse each word individually.

## Invariant / State

- The compaction phase keeps a cleaned prefix with single spaces only.
- After reversing the full character list, each word is backward but in the correct final position.
- Reversing each word restores readable order.

## Walkthrough

For `"  hello   world  "`:
- Compact to `"hello world"`.
- Reverse all characters to `"dlrow olleh"`.
- Reverse each word to get `"world hello"`.

## Complexity

- Time: `O(n)`
- Space: `O(n)` in Python due to conversion to a list of characters

## Edge Cases

- Leading and trailing spaces
- Multiple spaces between words
- Single word

## Common Mistakes

- Leaving extra spaces in the result
- Reversing words before reversing the whole sequence
- Forgetting that Python strings are immutable

## Pattern Transfer

- 344.Reverse String
- In-place text normalization
- Multi-pass pointer processing

## Self-Check

- Why do we compact spaces before reversing?
- What is true about the string after the full reverse?
- Why does reversing each word afterward fix the final order?

## Function

```python
class Solution:
    def reverseWords(self, s: str) -> str:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/151-reverse-words-in-a-string/python -q
```
