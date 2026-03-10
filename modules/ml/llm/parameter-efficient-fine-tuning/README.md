# Parameter-Efficient Fine-Tuning

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to compare the main low-parameter adaptation methods used in modern LLM fine-tuning: LoRA and QLoRA.

## First Principles

- Full fine-tuning updates every weight, which is often too expensive.
- LoRA keeps the base model frozen and learns a low-rank update.
- QLoRA adds that low-rank update on top of quantized base weights to save memory.

## Core Math

LoRA update:

$$
W' = W + \frac{\alpha}{r}AB
$$

QLoRA update:

$$
W_q = \mathrm{Quantize}(W), \quad W' = W_q + \frac{\alpha}{r}AB
$$

## Minimal Code Mental Model

```python
adapted = lora_update(w, a, b, alpha=16.0)
quantized_adapted = qlora_update(w, a, b, alpha=16.0, scale=0.1)
```

## Function

```python
def lora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float) -> list[list[float]]:
def qlora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float, scale: float) -> list[list[float]]:
```

## When To Use What

- Use LoRA when memory is tight but the base weights stay in standard precision.
- Use QLoRA when memory is the main bottleneck and quantized base weights are acceptable.

## Run tests

```bash
pytest modules/ml/llm/parameter-efficient-fine-tuning/python -q
```
