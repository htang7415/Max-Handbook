# Cache Admission Policies

> Track: `databases` | Topic: `caching`

## Concept

Cache admission decides which responses are worth storing at all. In noisy workloads, admitting every key can waste capacity on one-hit misses, so a small frequency gate can keep the cache focused on hotter items.

## Key Points

- Always-admit is simple, but it lets cold noise evict useful entries.
- Frequency-based admission waits for repeat demand before spending cache space.
- Admission and eviction solve different problems: one decides what gets in, the other decides what stays.
- This matters for AI products where long-tail prompts or document queries can create many low-reuse keys.
- A frequency threshold should be positive; `0` is not a meaningful gate.

## Minimal Code Mental Model

```python
stream = ["q1", "q2", "q1", "q3", "q1"]
summary = admitted_keys(stream, min_hits=2)
```

## Function

```python
def validate_min_hits(min_hits: int) -> None:
def request_counts(stream: list[str]) -> dict[str, int]:
def admit_always(key: str) -> bool:
def admit_on_frequency(key: str, counts: dict[str, int], min_hits: int) -> bool:
def admitted_keys(stream: list[str], min_hits: int) -> dict[str, list[str]]:
```

## Run tests

```bash
pytest modules/databases/caching/cache-admission-policies/python -q
```
