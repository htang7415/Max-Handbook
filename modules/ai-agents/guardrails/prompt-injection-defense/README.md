# Prompt Injection Defense

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Prompt injection defense treats retrieved text, tool output, web pages, and UI content as untrusted data so they cannot silently replace the agent's real instructions.

## Key Points

- External content is data, not policy.
- Injection signals often look like instruction overrides, secret-exfiltration requests, or attempts to change roles.
- A useful first defense is to detect suspicious phrases and fence untrusted content before it enters the main prompt.

## Minimal Code Mental Model

```python
hits = suspicious_instruction_hits(page_text, DEFAULT_SUSPICIOUS_MARKERS)
risk = prompt_injection_risk(page_text)
context = guard_untrusted_content(page_text, source="retrieved page")
```

## Function

```python
DEFAULT_SUSPICIOUS_MARKERS: list[str]
DEFAULT_SENSITIVE_TARGETS: list[str]

def suspicious_instruction_hits(text: str, markers: list[str]) -> list[str]:
def prompt_injection_risk(
    text: str,
    suspicious_markers: list[str] | None = None,
    sensitive_targets: list[str] | None = None,
) -> str:
def guard_untrusted_content(text: str, source: str = "untrusted content") -> str:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/prompt-injection-defense/python -q
```
