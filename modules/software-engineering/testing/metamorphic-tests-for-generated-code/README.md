# Metamorphic Tests For Generated Code

> Track: `software-engineering` | Topic: `testing`

## Concept

Metamorphic tests check whether behavior stays consistent under transformations that should preserve a known invariant, which is especially useful when AI-generated code lacks obvious example cases.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Generated algorithm | Exact expected outputs are hard to enumerate | No invariant-preserving transformation exists |
| Normalization logic | Reordering, casing, or duplicates should not change meaning | Output order is the core behavior |
| Regression hunting | Example tests miss equivalent-input bugs | One deterministic example fully covers the contract |

## First Principles

- The key question is not only "is this output correct?" but also "does this invariant survive equivalent inputs?"
- Reordering, casing, normalization, and grouping are common invariant-preserving transformations.
- Metamorphic checks often catch subtle regressions that example-based tests miss.

## Workflow

1. Define the invariant that should survive transformation.
2. Build equivalent input variants.
3. Evaluate the first input as the expected behavior.
4. Compare every variant against that expected result.
5. Report variant indexes that break the invariant.

## Minimal Code Mental Model

```python
failures = metamorphic_failures(
    lambda values: sorted_unique(values),
    [["b", "a", "a"], ["a", "b"]],
)
assert failures == []
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Empty equivalent set | There is no reference behavior | `metamorphic_failures` rejects empty inputs |
| Transformation changes meaning | Test fails for the wrong reason | Inputs must be equivalent under the stated invariant |
| Idempotence broken | Normalization changes on repeated application | `preserves_idempotence` checks repeat application |

## Function

```python
def sorted_unique(values: list[str]) -> list[str]:
def metamorphic_failures(evaluator, equivalent_inputs: list[list[str]]) -> list[int]:
def preserves_idempotence(values: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/testing/metamorphic-tests-for-generated-code/python -q
```
