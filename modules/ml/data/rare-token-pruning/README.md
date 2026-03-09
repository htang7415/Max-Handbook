# Rare Token Pruning

> Track: `ml` | Topic: `data`

## Concept

Rare token pruning replaces infrequent tokens with a shared fallback token before building sparse lexical features.

## Math

$$
\mathrm{prune}(t) =
\begin{cases}
t & \text{if count}(t) \ge m \\
\text{UNK} & \text{otherwise}
\end{cases}
$$

- $t$ -- observed token
- $m$ -- minimum frequency threshold

## Key Points

- Pruning long-tail tokens can stabilize sparse vocabularies.
- This is a preprocessing guardrail before count-vector or TF-IDF features.
- The module returns the pruned token list directly.

## Function

```python
def prune_rare_tokens(tokens: list[str], min_count: int, unk_token: str = "__UNK__") -> list[str]:
```

## Run tests

```bash
pytest modules/ml/data/rare-token-pruning/python -q
```
