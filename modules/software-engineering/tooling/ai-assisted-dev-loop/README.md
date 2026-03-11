# AI-Assisted Dev Loop

> Track: `software-engineering` | Topic: `tooling`

## Concept

An AI-assisted dev loop is safe when the task, constraints, checks, and review handoff are explicit instead of being left inside the model's hidden reasoning.

## Key Points

- A change request should include acceptance checks, not just a task sentence.
- The next step after code generation should usually be targeted verification, not immediate merge.
- Risk should rise when a change touches sensitive paths or generated outputs.

## Minimal Code Mental Model

```python
request = make_change_request(
    "Add idempotency to payment retries",
    ["keep API backward compatible"],
    ["contract tests", "targeted retry tests"],
)
stage = next_stage(patch_ready=True, checks_passed=False, review_signed_off=False)
risk = review_risk(["services/payments/api.py", "docs/payments.md"])
```

## Function

```python
def make_change_request(
    task: str,
    constraints: list[str],
    acceptance_checks: list[str],
) -> dict[str, object]:
def next_stage(patch_ready: bool, checks_passed: bool, review_signed_off: bool) -> str:
def review_risk(changed_paths: list[str], touches_generated_code: bool = False) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/ai-assisted-dev-loop/python -q
```
