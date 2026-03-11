# Prompt Structuring

> Track: `ai-agents` | Topic: `prompting`

## Concept

Prompt structuring separates behavior instructions, user intent, and explicit constraints into a clearer message layout.

## Key Points

- Separate system behavior from the user request.
- Put constraints in an explicit checklist when they matter.
- Short structured prompts are easier to debug than long blended prompts.

## Core Math

- Active prompt budget:
  $$
  \text{system} + \text{task} + \text{constraints} \le \text{context window}
  $$
- Constraint coverage:
  $$
  \frac{\text{satisfied constraints}}{\text{required constraints}}
  $$

## Minimal Code Mental Model

```python
checklist = format_checklist(["answer in bullets", "cite sources"])
messages = build_messages(
    system_prompt="You are a careful research assistant.",
    user_prompt="Summarize the latest policy changes.",
    checklist=["answer in bullets", "cite sources"],
)
```

## Function

```python
def format_checklist(items: list[str]) -> str:
def build_messages(
    system_prompt: str,
    user_prompt: str,
    checklist: list[str] | None = None,
) -> list[dict[str, str]]:
```

## Run tests

```bash
pytest modules/ai-agents/prompting/prompt-structuring/python -q
```
