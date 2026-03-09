# Array Summary

> Track: `dsa` | Topic: `array`

## What This Module Covers

This summary ties together the main array patterns: binary search, read/write pointers, sliding windows, range accumulation, and matrix traversal.

## Recognition Cues

- Sorted data suggests binary search or opposing pointers.
- Contiguous constraints suggest sliding windows.
- In-place filtering suggests read/write pointers.
- Grid inputs suggest row/column boundary control.

## Core Ideas

- Most array solutions become simple once the active index range is clear.
- A few reusable invariants cover many problems: sorted half elimination, kept-prefix compaction, and valid-window maintenance.
- Matrix problems are still array problems with one extra dimension of boundary control.

## Common Mistakes

- Mixing closed and half-open intervals.
- Forgetting that only a prefix of a mutated array may matter afterward.
- Treating a matrix as conceptually different when it is still index reasoning plus boundaries.

## Connections

- Double pointers extends array scans to linked lists and sorted tuples.
- Prefix and range thinking connects arrays to dynamic programming.
- Monotonic stacks often start from array traversal and boundary intuition.

## Self-Check

- How do you tell binary search from sliding window?
- What invariant does a read/write pointer method maintain?
- When is index reasoning more important than value reasoning?
