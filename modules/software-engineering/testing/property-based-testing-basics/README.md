# Property-Based Testing Basics

> Track: `software-engineering` | Topic: `testing`

## Concept

Property-based testing checks broad invariants across many generated or enumerated inputs instead of relying only on a few hand-picked examples.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Broad input space | Hand-picked examples miss edge cases | The behavior has no stable invariant |
| Helper logic | Properties like idempotence or commutativity should always hold | One exact output is the entire contract |
| Regression triage | You need counterexamples, not just pass/fail | Inputs are expensive or unsafe to generate |

## First Principles

- A property describes what should always hold, not one exact output.
- Small helper generators are enough to teach the idea without a heavy framework.
- Counterexamples are more useful than "one more passing example."

## Workflow

1. Write the invariant as a predicate.
2. Collect or generate representative cases.
3. Run every case through the predicate.
4. Return failing cases as counterexamples.
5. Add the counterexample to regression coverage.

## Minimal Code Mental Model

```python
failing = failing_cases(["abc", "", "racecar"], reverse_twice_property)
ok = property_holds([(1, 2), (3, 5)], sum_commutative_property)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Property is too vague | Test passes without protecting behavior | Predicate should encode the invariant directly |
| Counterexample discarded | The same bug can return | `failing_cases` returns exact failing inputs |
| Empty cases misunderstood | Vacuous pass hides missing coverage | Empty lists pass but should not be the only suite |

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
