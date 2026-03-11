# Property-Based Testing Basics

> Track: `software-engineering` | Topic: `testing`

## Concept

Property-based testing checks broad invariants across many generated or enumerated inputs instead of relying only on a few hand-picked examples.

## Key Points

- A property describes what should always hold, not one exact output.
- Small helper generators are enough to teach the idea without a heavy framework.
- Counterexamples are more useful than “one more passing example.”

## Minimal Code Mental Model

```python
failing = failing_cases(["abc", "", "racecar"], reverse_twice_property)
ok = property_holds([(1, 2), (3, 5)], sum_commutative_property)
```

## Function

```python
def failing_cases(cases: list[object], predicate: callable) -> list[object]:
def property_holds(cases: list[object], predicate: callable) -> bool:
def reverse_twice_property(text: str) -> bool:
def sum_commutative_property(pair: tuple[int, int]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/testing/property-based-testing-basics/python -q
```
