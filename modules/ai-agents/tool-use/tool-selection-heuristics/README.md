# Tool Selection Heuristics

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Tool selection heuristics score candidate tools against the request and choose the most relevant one before any call happens.

## Key Points

- Tool choice should be explicit when several tools look plausible.
- A simple score based on keyword overlap is often enough for a first router.
- Ranking is useful even if the final system only calls one tool.

## Minimal Code Mental Model

```python
score = keyword_match_score("check the weather in Madison", ["weather", "temperature"])
ranked = rank_tools("check the weather in Madison", tool_keywords)
tool = pick_tool("check the weather in Madison", tool_keywords)
```

## Function

```python
def keyword_match_score(intent: str, keywords: list[str]) -> int:
def rank_tools(intent: str, tool_keywords: dict[str, list[str]]) -> list[tuple[str, int]]:
def pick_tool(intent: str, tool_keywords: dict[str, list[str]]) -> str | None:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/tool-selection-heuristics/python -q
```
