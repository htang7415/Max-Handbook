# Golden And Snapshot Test Tradeoffs

> Track: `software-engineering` | Topic: `testing`

## Concept

Golden and snapshot tests are useful when output shape matters, but they become noisy when the output changes often or includes nondeterministic values.

## Key Points

- Snapshot tests are best for stable output formats, not highly volatile text.
- Nondeterministic values like timestamps make snapshot diffs noisy.
- Large snapshot changes should trigger review of whether the test is still the right tool.

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
