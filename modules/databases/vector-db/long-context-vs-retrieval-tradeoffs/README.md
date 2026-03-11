# Long-Context Vs Retrieval Tradeoffs

> Track: `databases` | Topic: `vector-db`

## Concept

Long context and retrieval solve the same “get the model the right information” problem with different costs. Long context sends more tokens; retrieval sends fewer tokens but needs ranking to be correct.

## Key Points

- If the whole source fits comfortably and most of it matters, long context can be simpler.
- If the source is much larger than the useful subset, retrieval usually reduces token load.
- Retrieval introduces recall and ranking risks that long context avoids.
- The right choice depends on source size, relevant fraction, and model window.
- If neither approach fits the window, reduce token load first by shrinking chunks, lowering `top_k`, or summarizing.

## Minimal Code Mental Model

```python
summary = strategy_summary(
    source_tokens=200_000,
    relevant_tokens=1_000,
    model_window=128_000,
    top_k=5,
    avg_chunk_tokens=200,
)
```

## Function

```python
def long_context_token_load(source_tokens: int, prompt_overhead: int = 0) -> int:
def retrieval_token_load(
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> int:
def fits_context_window(total_tokens: int, model_window: int) -> bool:
def validate_inputs(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> None:
def choose_strategy(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> str:
def strategy_summary(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> dict[str, int | float | str | bool]:
```

## Run tests

```bash
pytest modules/databases/vector-db/long-context-vs-retrieval-tradeoffs/python -q
```
