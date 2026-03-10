# LLM Tokenization

Tokenization decides what the model sees as a unit and what the system pays for in context length.

## Purpose

Use this page to understand:
- what a token is
- why tokenizers differ
- how token counts affect prompting, cost, and truncation

## First Principles

- A tokenizer turns raw text into discrete symbols before the model sees it.
- Better tokenization trades vocabulary size against sequence length.
- Different tokenizers change both quality and systems cost because token counts drive context usage.
- Tokenization is part of the model interface, not just preprocessing.

## Core Math

- Tokenized sequence:
  $$
  x \rightarrow (t_1, t_2, \dots, t_n)
  $$
- In transformer-style models, longer tokenized sequences usually mean more memory and attention cost.

## Minimal Code Mental Model

```python
tokens = tokenizer(text)
count = len(tokens)
fits_budget = count <= max_tokens
```

## Canonical Modules

- Core tokenization: `tokenization`
- Comparison and trade-offs: `tokenizer-comparison`
- Budgeting impact: `token-budgeting`

## When To Use What

- Start with `tokenization` before tokenizer comparisons.
- Use `tokenizer-comparison` when the same text behaves differently across tokenizers.
- Use `token-budgeting` when prompting, truncation, or cost is the actual problem.
