# Speculative Decoding Verification

> Track: `ml` | Topic: `llm`

## Concept

Speculative decoding uses a fast draft model to propose tokens, then verifies them with a stronger target model.
Accepted draft tokens are kept until the first mismatch.

## Math

$$k = \max \{ t : d_1 = p_1, \ldots, d_t = p_t \}$$

Returned verified continuation:

$$
[p_1,\dots,p_k,p_{k+1}]
$$

- $d_t$ -- draft token at position $t$
- $p_t$ -- target-model token at position $t$
- $k$ -- accepted prefix length

## Key Points

- Verification accepts a matching prefix and falls back at the first mismatch.
- Speedup comes from accepting several cheap draft tokens at once.
- Quality is preserved because the target model still decides the final output.
- The returned step is the accepted draft prefix plus the next target-decided token, when that token exists.

## Function

```python
def speculative_decode_step(
    draft_tokens: list[int],
    target_tokens: list[int],
) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/llm/speculative-decoding/python -q
```
