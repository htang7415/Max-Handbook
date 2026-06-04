# Grounded Support Agent

> Track: `ai-agents` | Topic: `capstones`

## Concept

This capstone combines retrieval grounding, short memory, tool choice, and review or block decisions into one compact support-agent loop.

## Key Points

- Grounded answers should depend on both confidence and evidence coverage.
- Tool use should beat direct answering by explicit expected value, not habit.
- Block and review paths should be as explicit as the happy path.
- Active context should stay small enough to inspect.
- The dedicated tool-selection math lives in `expected-value-tool-selection`; this capstone shows how that choice interacts with grounding and memory.

## Core Math

- Grounding coverage:
  $$
  \frac{\text{supported claims}}{\text{claims made}}
  $$
- Context budget:
  $$
  \text{retrieved blocks} + \text{memory blocks} \le \text{active context cap}
  $$

## Minimal Code Mental Model

```python
context = build_support_context(retrieved_chunks, memories, max_chunks=2, max_memories=1)
tool = select_support_tool(tool_profiles, min_expected_value=2.0, min_margin=0.5)
decision = grounded_support_decision(
    retrieved_chunks,
    memories,
    tool_profiles,
    blocked=False,
    confidence=0.82,
    grounding_coverage=0.9,
)
```

## Function

```python
def build_support_context(
    retrieved_chunks: list[tuple[str, float]],
    memories: list[str],
    max_chunks: int = 2,
    max_memories: int = 1,
) -> dict[str, list[str]]:
def select_support_tool(
    tool_to_profile: dict[str, dict[str, float]],
    min_expected_value: float,
    min_margin: float = 0.0,
) -> str:
def grounded_support_decision(
    retrieved_chunks: list[tuple[str, float]],
    memories: list[str],
    tool_to_profile: dict[str, dict[str, float]],
    blocked: bool,
    confidence: float,
    grounding_coverage: float,
    min_confidence: float = 0.7,
    min_grounding: float = 0.75,
    min_expected_value: float = 0.0,
    min_margin: float = 0.0,
    max_chunks: int = 2,
    max_memories: int = 1,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/capstones/grounded-support-agent/python -q
```
