# Examples and Delimiters

> Track: `ai-agents` | Topic: `prompting`

## Concept

Examples and delimiters make the prompt easier for the model to follow by showing a target pattern and clearly separating sections.

## Key Points

- Few-shot examples help when the target format is easier to imitate than describe.
- Delimiters help the model distinguish instructions, input, and expected output shape.
- Examples should stay short and representative.

## Minimal Code Mental Model

```python
example_block = few_shot_block([("Q1", "A1"), ("Q2", "A2")])
section = wrap_section("INPUT", "Summarize this note.")
prompt = compose_prompt_sections([example_block, section])
```

## Function

```python
def few_shot_block(pairs: list[tuple[str, str]]) -> str:
def wrap_section(label: str, content: str) -> str:
def compose_prompt_sections(sections: list[str]) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/prompting/examples-and-delimiters/python -q
```
