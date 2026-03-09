# Introduction to Hash Table

> Track: `dsa` | Topic: `hash-tables`

## What This Module Covers

This introduction covers the basic hash-table move: store values as keys so membership, counts, and complements can be checked in constant average time.

## Recognition Cues

- You need fast membership or frequency checks.
- A complement, duplicate, or prior occurrence matters.
- Order is less important than lookup speed.

## Core Ideas

- Hash maps trade memory for fast average lookup.
- Frequency counting is the simplest reusable pattern.
- Many nested-loop scans collapse into one-pass hash lookups.

## Common Mistakes

- Using a list or repeated scan when a map lookup is the actual need.
- Storing the wrong value for each key.
- Forgetting that hash-based solutions usually lose order unless you track it explicitly.

## Connections

- Two Sum, anagrams, and frequency-comparison problems.
- Sets use the same lookup idea when counts are unnecessary.
- Arrays often provide the scan order while the hash map provides memory.

## Self-Check

- When do you need a set versus a dictionary?
- What should each key map to in a given problem?
- What tradeoff does a hash table make?

## Function

```python
def frequency_map(values: list[int]) -> dict[int, int]:
```
