# RAG Basics

> Track: `ai-agents` | Topic: `rag`

## Concept

RAG basics cover the smallest useful loop: retrieve candidate chunks, keep the top ones, and pack them into a grounded context block.

## Key Points

- Retrieval should happen before generation, not during hallucinated answering.
- Only the highest-value chunks should be packed into the final context.
- Grounded context should be short enough that the model can still use it.

## Core Math

- Retrieval ranking:
  $$
  \text{top-}k = \operatorname{arg\,sort}_k(\text{chunk score})
  $$
- Packing budget:
  $$
  \sum_i \text{chunk tokens}_i \le \text{context budget}
  $$

## Minimal Code Mental Model

```python
top_chunks = select_top_k([("A", 0.9), ("B", 0.7), ("C", 0.4)], k=2)
context = build_grounded_context(top_chunks, max_chunks=2)
```

## Function

```python
def select_top_k(scored_chunks: list[tuple[str, float]], k: int) -> list[str]:
def build_grounded_context(chunks: list[str], max_chunks: int) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/rag/rag-basics/python -q
```
