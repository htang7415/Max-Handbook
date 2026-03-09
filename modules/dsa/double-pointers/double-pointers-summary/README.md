# Double Pointers Summary

> Track: `dsa` | Topic: `double-pointers`

## What This Module Covers

This summary collects the main two-pointer patterns: opposite-end scans, fast/slow gaps, read/write compaction, and linked-list pointer synchronization.

## Recognition Cues

- Two positions move through the same structure with different roles.
- The answer depends on relative movement, not just one current value.
- You want `O(1)` extra space while scanning.

## Core Ideas

- Opposite-end pointers fit sorted arrays and symmetry problems.
- Fast/slow pointers fit linked lists and fixed-gap tasks.
- Read/write pointers fit in-place filtering and compaction.

## Common Mistakes

- Advancing the wrong pointer after a comparison.
- Forgetting what each pointer semantically represents.
- Comparing linked-list values when the problem really depends on node identity.

## Connections

- Arrays and linked lists share pointer logic but differ in access cost.
- Sliding windows are specialized pointer methods over contiguous ranges.
- Monotonic stacks solve some boundary problems that plain pointers cannot.

## Self-Check

- What role does each pointer play in a given solution?
- When should pointers move independently versus together?
- How does pointer reasoning differ between arrays and linked lists?
