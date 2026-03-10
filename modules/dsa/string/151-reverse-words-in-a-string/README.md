# 151.Reverse Words in a String

> Track: `dsa` | Topic: `string`

## Problem in One Line

Reverse the order of the words in a string while collapsing extra spaces.

## Recognition Cues

- The task is about words, not individual characters.
- Extra spaces must be removed in the final answer.
- In-place character work can solve both spacing cleanup and word reversal.

## Baseline Idea

Split the string into words, reverse the list, and join with single spaces. That works in Python, but it hides the underlying string-manipulation pattern.

## Core Insight

First compact spaces so the string has single separators only. Then reverse the whole character array, and finally reverse each word in place to restore each word's spelling.

## Invariant / State

- After compaction, words are separated by exactly one space and there are no leading or trailing spaces.
- After reversing the whole array, words appear in reverse order but each word's characters are reversed.
- Reversing each word restores the correct spelling.

## Walkthrough

For `"  hello   world  "`:
- Compact spaces to `"hello world"`.
- Reverse the whole string to `"dlrow olleh"`.
- Reverse each word to get `"world hello"`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- Leading and trailing spaces
- Multiple spaces between words
- A single word
- An input that is only spaces

## Common Mistakes

- Reversing characters instead of words
- Preserving extra spaces in the output
- Forgetting to reverse each word after reversing the whole string

## Pattern Transfer

- Two-phase in-place reversal problems
- String normalization tasks
- Pointer-based word parsing

## Self-Check

- Why do spaces need to be compacted before reversing?
- What should the result be for an input containing only spaces?
- Why do we reverse the whole string before reversing each word?

## Function

```python
class Solution:
    def reverseWords(self, s: str) -> str:
```

## Run tests

```bash
pytest modules/dsa/string/151-reverse-words-in-a-string/python -q
```
