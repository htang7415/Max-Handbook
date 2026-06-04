# Spec-First AI Coding

> Track: `software-engineering` | Topic: `tooling`

## Concept

AI-generated code is safer when the model is given an explicit spec with contracts, constraints, and verification targets before it starts producing implementation details.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| AI implementation task | The model will write or modify code | The model is only explaining existing code |
| Boundary change | API, schema, state, or workflow behavior can drift | The change is isolated copy editing |
| Review planning | Reviewers need to know what evidence to inspect | No artifact will be merged |

## First Principles

- A vague prompt creates vague code and vague review scope.
- Specs should name the contract, invariants, and verification path.
- Missing spec sections are a delivery risk, not just a documentation gap.

## Workflow

1. Define required spec sections.
2. Compare required sections with present sections.
3. Block generation until the spec is complete.
4. Derive review focus from change tags.
5. Review generated code against the spec, not the prompt alone.

## Minimal Code Mental Model

```python
missing = missing_spec_sections(required, present)
ready = spec_ready_for_generation(required, present)
focus = review_focus(["api", "mutation", "ai-generated"])
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Missing invariant | Generated code preserves the wrong behavior | `missing_spec_sections` reports absent sections |
| Generation starts too early | Review scope is unclear | `spec_ready_for_generation` requires full spec shape |
| Review misses risk area | Important boundary is not inspected | `review_focus` expands by tags |

## Function

```python
def missing_spec_sections(required_sections: list[str], present_sections: list[str]) -> list[str]:
def spec_ready_for_generation(required_sections: list[str], present_sections: list[str]) -> bool:
def review_focus(change_tags: list[str]) -> list[str]:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/spec-first-ai-coding/python -q
```
