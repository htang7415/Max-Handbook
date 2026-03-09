# Combined Sampling Pipeline

> Track: `ml` | Topic: `llm`

## Concept

Modern decoding often applies temperature scaling, then a top-k filter, then a top-p filter before sampling the next token.

## Math

$$p_i = \operatorname{softmax}(z_i / T)$$

$$S_k = \operatorname{TopK}(p, k), \qquad S_p = \operatorname{TopP}(p_{S_k}, p)$$

- $z_i$ -- token logit for token $i$
- $T$ -- temperature
- $S_k$ -- top-k candidate set
- $S_p$ -- nucleus-filtered candidate set after top-k

## Key Points

- Temperature changes the distribution before filtering.
- Top-k sets a hard cap on candidate count.
- Top-p then trims the remaining set by cumulative mass.

## Function

```python
def sampling_pipeline_candidates(
    logits: list[float],
    temperature: float,
    top_k: int,
    top_p: float,
) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/llm/sampling-pipeline/python -q
```
