# AI-Assisted Dev Loop

> Track: `software-engineering` | Topic: `tooling`

## Concept

An AI-assisted dev loop is safe when the task, constraints, checks, and review handoff are explicit instead of being left inside the model's hidden reasoning.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| AI-generated change | The model will edit production code or tests | You are only asking for explanation |
| Review handoff | A human needs to evaluate generated output | No code or artifact will be produced |
| Risk triage | Paths include auth, payments, migrations, secrets, or generated code | The change is isolated documentation |

## First Principles

- A change request should include acceptance checks, not just a task sentence.
- The next step after code generation should usually be targeted verification, not immediate merge.
- Risk should rise when a change touches sensitive paths or generated outputs.

## Workflow

1. Write the task, constraints, and acceptance checks.
2. Generate or edit the patch.
3. Run targeted checks before review.
4. Send passing changes to human review.
5. Ship only after checks and review both pass.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Missing acceptance checks | Generated code has no objective finish line | `make_change_request` rejects empty checks |
| Skipping verification | Patch moves to review or ship too early | `next_stage` returns `run_checks` before review |
| Sensitive or generated diff | Plausible code hides high-risk behavior | `review_risk` returns `high` |

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
