# Input Validation And Output Encoding

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Input validation constrains what the system accepts, and output encoding ensures untrusted text is rendered safely in the target context.

## Key Points

- Validation should happen before business logic depends on the input.
- Rendering user input without encoding creates injection risk.
- Validation and encoding solve different problems and both are needed.

## Minimal Code Mental Model

```python
username = validate_username("alice_1")
safe = html_escape('<script>alert(1)</script>')
rendered = render_comment_html("alice_1", "<b>Hello</b>")
```

## Function

```python
def validate_username(username: str) -> str:
def html_escape(text: str) -> str:
def render_comment_html(author: str, comment: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/input-validation-and-output-encoding/python -q
```
