# Sample Size and Power

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Sample size and power basics estimate how many paired or per-variant cases an agent evaluation needs before a target effect size is realistically detectable.

## Key Points

- Tiny quality differences need more eval cases than large differences.
- Required sample size depends on the baseline rate and the effect you care about.
- Before running more benchmarks, it helps to know whether the current sample can detect the change at all.

## Minimal Code Mental Model

```python
required = required_sample_size(baseline_success=0.7, effect_size=0.05)
mde = minimum_detectable_effect(baseline_success=0.7, sample_size_per_variant=required)
route = sample_size_route(current_samples_per_variant=900, required_samples_per_variant=required)
```

## Function

```python
def required_sample_size(
    baseline_success: float,
    effect_size: float,
    z_alpha: float = 1.96,
    z_beta: float = 0.84,
) -> int:
def minimum_detectable_effect(
    baseline_success: float,
    sample_size_per_variant: int,
    z_alpha: float = 1.96,
    z_beta: float = 0.84,
) -> float:
def sample_size_route(current_samples_per_variant: int, required_samples_per_variant: int) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/sample-size-and-power/python -q
```
