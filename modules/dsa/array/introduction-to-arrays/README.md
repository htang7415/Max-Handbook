# Introduction to Arrays

> Track: `dsa` | Topic: `array`

## What This Module Covers

Arrays provide contiguous storage, direct index access, and a simple model for scans, updates, and range-based reasoning.

## Recognition Cues

- The input is a sequence with meaningful positions.
- You need fast access by index.
- The solution may involve scanning, windowing, or pointer movement.

## Core Ideas

- Arrays reward invariant-based thinking over index ranges.
- Many array problems reduce to choosing the right traversal direction and maintained state.
- Contiguous layout makes binary search, sliding windows, and in-place updates natural.

## Common Mistakes

- Missing off-by-one boundaries.
- Confusing contiguous subarrays with arbitrary subsequences.
- Mutating an array in place without tracking which region is still valid.

## Connections

- Binary search on sorted arrays.
- Two pointers for filtering and symmetric scans.
- Sliding windows for contiguous constraints.

## Self-Check

- What does direct index access buy you?
- When should you think in terms of ranges instead of individual elements?
- Which problems become simpler because arrays are contiguous?
