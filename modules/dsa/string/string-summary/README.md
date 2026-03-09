# String Summary

> Track: `dsa` | Topic: `string`

## What This Module Covers

This summary reviews the main string patterns in the track: reversing, normalization, substring matching, and word-level transformations.

## Recognition Cues

- The task works at the level of characters, words, or substrings.
- Whitespace or punctuation handling affects correctness.
- Small boundary rules often matter more than the main loop.

## Core Ideas

- Strings behave like arrays of characters when mutation is allowed.
- Tokenize-transform-rebuild is a common workflow for word problems.
- Substring, subsequence, and token order are different problem shapes.

## Common Mistakes

- Confusing substring and subsequence.
- Ignoring whitespace normalization rules.
- Reversing characters when the problem asks to reverse words.

## Connections

- Arrays for index reasoning.
- Dynamic programming for edit distance and subsequence families.
- Stack or pointer techniques for cancellation and reversal.

## Self-Check

- Does the problem care about characters, words, or substrings?
- What transformations preserve order and which ones reorder it?
- Where are the likely spacing or boundary bugs?
