# Golden And Snapshot Test Tradeoffs

> Track: `software-engineering` | Topic: `testing`

## Concept

Golden and snapshot tests are useful when output shape matters, but they become noisy when the output changes often or includes nondeterministic values.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Golden test | Output is stable and exact expected text matters | Output is large structured data |
| Snapshot test | Large structured output should be reviewed as a whole | Output includes nondeterministic values |
| Specific assertions | Only a few fields matter | Whole-output diffs improve review quality |

## First Principles

- Snapshot tests are best for stable output formats, not highly volatile text.
- Nondeterministic values like timestamps make snapshot diffs noisy.
- Large snapshot changes should trigger review of whether the test is still the right tool.

## Workflow

1. Decide whether the output is stable.
2. Choose golden, snapshot, or specific-field assertions.
3. Estimate snapshot noise from changed lines and nondeterministic values.
4. Require reviewer sign-off for snapshot updates.
5. Block high-noise snapshots instead of blessing churn.

## Minimal Code Mental Model

```python
kind = recommended_output_test(stable_output=True, large_structured_output=True)
risk = snapshot_noise_risk(changed_lines=40, has_nondeterministic_values=False)
ok = snapshot_update_allowed(
    changed_lines=8,
    has_nondeterministic_values=False,
    reviewer_signed_off=True,
)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Snapshot includes nondeterminism | Diff changes every run | `snapshot_noise_risk` returns `high` |
| Large diff auto-accepted | Review hides semantic change | `snapshot_update_allowed` requires sign-off |
| Wrong test type | Test is noisy or too weak | `recommended_output_test` chooses by stability and size |

## Function

```python
def recommended_output_test(stable_output: bool, large_structured_output: bool) -> str:
def snapshot_noise_risk(changed_lines: int, has_nondeterministic_values: bool) -> str:
def snapshot_update_allowed(
    changed_lines: int,
    has_nondeterministic_values: bool,
    reviewer_signed_off: bool,
) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/testing/golden-and-snapshot-test-tradeoffs/python -q
```
