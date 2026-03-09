# Edit Distance Summary

> Track: `dsa` | Topic: `dynamic-programming`

## What This Module Covers

This summary reviews two-string alignment DP: LCS, deletion distance, edit distance, subsequence checks, and related prefix-table problems.

## Recognition Cues

- Two sequences are compared character by character.
- Prefix pairs naturally define subproblems.
- The operations or match rules determine the transition family.

## Core Ideas

- LCS keeps shared structure.
- Deletion distance can be derived from LCS.
- Edit distance adds insert, delete, and replace transitions.
- Subsequence problems often collapse to simpler pointer or boolean DP versions.

## Common Mistakes

- Confusing substring with subsequence.
- Using the wrong DP meaning for `dp[i][j]`.
- Forgetting empty-prefix initialization.

## Connections

- 1143, 583, and 72 are closely related.
- Some special cases simplify to greedy scans.
- Interval or palindrome DP is different because the state is over one string's boundaries, not two strings' prefixes.

## Self-Check

- What does `dp[i][j]` mean in each string-alignment problem?
- Which operations are allowed by the problem statement?
- When can LCS be used as an intermediate result?
