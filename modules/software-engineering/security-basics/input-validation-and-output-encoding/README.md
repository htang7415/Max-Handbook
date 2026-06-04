# Input Validation And Output Encoding

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Input validation constrains what the system accepts, and output encoding ensures untrusted text is rendered safely in the target context.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| User input | Business logic depends on externally supplied values | The value is internal and already typed |
| HTML rendering | Untrusted text appears in markup | The output target is not HTML |
| Comment or profile UI | User-controlled text and identity appear together | The text is never rendered back to users |

## First Principles

- Validation should happen before business logic depends on the input.
- Rendering user input without encoding creates injection risk.
- Validation and encoding solve different problems and both are needed.

## Workflow

1. Validate identifiers before storing or authorizing them.
2. Reject invalid length or characters.
3. Encode untrusted text for the output context.
4. Render only validated identifiers and encoded content.
5. Keep validation and encoding as separate checks.

## Minimal Code Mental Model

```python
username = validate_username("alice_1")
safe = html_escape('<script>alert(1)</script>')
rendered = render_comment_html("alice_1", "<b>Hello</b>")
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Invalid identifier accepted | Business logic sees malformed names | `validate_username` rejects length and character violations |
| Untrusted HTML rendered raw | Script or markup injection | `html_escape` encodes special characters |
| Validation confused with encoding | Safe username does not make comment safe | `render_comment_html` does both |

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
