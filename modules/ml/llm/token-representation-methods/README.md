# Token and Representation Methods

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to learn the front end of an LLM in one place:
tokenization, tokenizer comparison, embedding lookup, and positional encoding.

## First Principles

- Tokenization turns raw text into discrete units.
- Different tokenizers change sequence length, cost, and context usage.
- Embeddings map token ids into dense vectors the model can process.
- Positional encoding injects token order, because token embeddings alone do not tell the model where each token sits.

## Core Math

Tokenization is a mapping:

$$
f: \text{text} \rightarrow (id_1, \dots, id_n)
$$

Embedding lookup uses a table:

$$
E \in \mathbb{R}^{V \times d}, \quad \text{embedding}(i) = E[i]
$$

Sinusoidal position encoding:

$$
\mathrm{PE}[pos,2i] = \sin\left(\frac{pos}{10000^{2i/d}}\right), \quad
\mathrm{PE}[pos,2i+1] = \cos\left(\frac{pos}{10000^{2i/d}}\right)
$$

Combined representation:

$$
x_t = E[\mathrm{token}_t] + \mathrm{PE}_t
$$

## From Math To Code

- Map raw text to token ids.
- Look up token embeddings from the table.
- Build a position encoding vector.
- Add the token embedding and position encoding to get the actual model input vector.

## Minimal Code Mental Model

```python
vocab = build_vocab(["hello world"])
ids = tokenize("hello world", vocab)
vectors = embed(ids, embedding_table)
position = sinusoidal_position(pos=3, d_model=8)
combined = add_position_embedding(vectors[0], position)
```

## Function

```python
def build_vocab(texts: list[str]) -> dict[str, int]:
def tokenize(text: str, vocab: dict[str, int]) -> list[int]:
def compare_token_counts(text: str, subword_vocab: set[str]) -> tuple[int, int]:
def embed(tokens: list[int], embeddings: list[list[float]]) -> list[list[float]]:
def sinusoidal_position(pos: int, d_model: int) -> list[float]:
def add_position_embedding(token_embedding: list[float], position_encoding: list[float]) -> list[float]:
```

## When To Use What

- Use `build_vocab` and `tokenize` to understand the basic text-to-id pipeline.
- Use `compare_token_counts` when token length, budget, or tokenizer choice is the issue.
- Use `embed` when you want the simplest view of token lookup into a learned table.
- Use `sinusoidal_position` when you want an explicit order signal added to token embeddings.

## Run tests

```bash
pytest modules/ml/llm/token-representation-methods/python -q
```
