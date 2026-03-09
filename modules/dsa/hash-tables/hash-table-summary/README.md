# Hash Table Summary

> Track: `dsa` | Topic: `hash-tables`

## What This Module Covers

This summary condenses the main hash-table ideas: frequency maps, membership sets, complement lookups, and quick summary statistics over a collection.

## Recognition Cues

- The task wants counts or existence checks.
- You can answer the question if you remember what has already been seen.
- Order is not the main source of difficulty.

## Core Ideas

- Hash maps count and associate.
- Hash sets deduplicate and test membership.
- One-pass scans become possible when you store the right key/value pair.

## Common Mistakes

- Storing the wrong information in the map.
- Updating counts or indices at the wrong time.
- Forgetting that hashed solutions usually need extra work if deterministic order matters.

## Connections

- Arrays provide the scan order.
- Sorting sometimes replaces hashing when order matters more than lookup speed.
- Backtracking also uses sets for duplicate control, but at recursion depth level.

## Self-Check

- What is the minimal information a given hash solution needs to store?
- When does frequency matter versus simple membership?
- When should hashing be replaced by sorting?

## Function

```python
def hash_table_summary(values: list[str]) -> dict[str, int | str | None]:
```
