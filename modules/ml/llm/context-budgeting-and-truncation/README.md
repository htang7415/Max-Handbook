# Context Budgeting and Truncation

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand how to reserve output space, detect truncation,
and keep the most useful parts of a long prompt inside a fixed context window.

## First Principles

- A prompt budget is smaller than the full context window because output tokens need reserved space.
- Truncation is a systems decision, not just a tokenizer detail.
- Head-only or tail-only truncation often loses important structure.
- Simple head-plus-tail retention is a useful baseline when you need both setup and recent context.

## Core Math

Available prompt budget:

$$
B_{\text{prompt}} = W - R
$$

Tokens dropped:

$$
\mathrm{drop} = \max(0, T - B_{\text{prompt}})
$$

- $W$ -- context window
- $R$ -- reserved output tokens
- $T$ -- total prompt tokens before truncation
- $B_{\text{prompt}}$ -- available prompt budget after reserving output space

## From Math To Code

- Reserve output tokens before packing prompt tokens.
- Check whether truncation is needed only after the prompt budget is known.
- Count how many tokens must be dropped before choosing a retention strategy.
- Use head-plus-tail retention when both global instructions and recent evidence matter.

## Minimal Code Mental Model

```python
prompt_budget = available_prompt_budget(context_window=8192, reserved_output_tokens=1024)
needs_truncation = truncation_needed(total_prompt_tokens=9600, prompt_budget=prompt_budget)
drop = tokens_to_drop(total_prompt_tokens=9600, prompt_budget=prompt_budget)
head_keep, tail_keep = head_tail_keep(total_prompt_tokens=9600, prompt_budget=7168, head_tokens=1024)
```

## Functions

```python
def available_prompt_budget(context_window: int, reserved_output_tokens: int) -> int:
def truncation_needed(total_prompt_tokens: int, prompt_budget: int) -> bool:
def tokens_to_drop(total_prompt_tokens: int, prompt_budget: int) -> int:
def head_tail_keep(total_prompt_tokens: int, prompt_budget: int, head_tokens: int) -> tuple[int, int]:
```

## When To Use What

- Use `available_prompt_budget` before any prompt packing decision.
- Use `truncation_needed` and `tokens_to_drop` when you need the simplest overflow check.
- Use `head_tail_keep` when prompt structure matters more than pure recency.

## Run tests

```bash
pytest modules/ml/llm/context-budgeting-and-truncation/python -q
```
