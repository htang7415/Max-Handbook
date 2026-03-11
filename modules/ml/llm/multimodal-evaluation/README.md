# Multimodal Evaluation

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to evaluate multimodal systems without collapsing everything
into one opaque benchmark score.

## First Principles

- Multimodal systems can fail because the answer is wrong or because a required modality was missing or ignored.
- VQA-style benchmarks often use reference consensus instead of a single gold answer.
- Modality coverage matters because a text-only answer can look fluent while failing to use the required image, audio, or video input.
- Good multimodal evaluation should separate task correctness from modality availability.

## Core Math

VQA-style consensus accuracy:

$$
\mathrm{VQAAcc} = \min\left(\frac{m}{3}, 1\right)
$$

where `m` is the number of matching references.

Modality coverage:

$$
\mathrm{Coverage} = \frac{|R \cap P|}{|R|}
$$

where `R` is the set of required modalities and `P` is the set of provided modalities.

- $m$ -- number of matching references
- $R$ -- required modalities
- $P$ -- provided modalities

## From Math To Code

- Start with the task score first, such as exact correctness or VQA-style consensus.
- Then check whether the example actually included the modalities the task required.
- Keep answer quality and modality coverage separate before mixing them into dashboards.

## Minimal Code Mental Model

```python
score = vqa_consensus_accuracy(matching_references=2)
coverage = modality_coverage_rate(["text", "image"], ["text", "image"])
overall = average_multimodal_accuracy([1.0, 0.67, 1.0])
```

## Functions

```python
def vqa_consensus_accuracy(matching_references: int) -> float:
def modality_coverage_rate(required_modalities: list[str], provided_modalities: list[str]) -> float:
def average_multimodal_accuracy(scores: list[float]) -> float:
```

## When To Use What

- Use `vqa_consensus_accuracy` when multiple human references are allowed, especially in VQA-style tasks.
- Use `modality_coverage_rate` when you need to verify that the right inputs were actually present.
- Use `average_multimodal_accuracy` only as a final aggregation step after per-example scoring is already clear.

## Run tests

```bash
pytest modules/ml/llm/multimodal-evaluation/python -q
```
