# Incidents And Postmortems

> Track: `software-engineering` | Topic: `reliability`

## Concept

Incident response limits user harm in the moment, and the postmortem turns the event into concrete follow-up work that reduces repeat failures.

## Use When

| Situation | Engineer Response |
| --- | --- |
| Users are affected right now | Declare and coordinate an incident |
| Data loss or security risk is possible | Escalate severity immediately |
| The event is over | Write a timeline and assign follow-up work |

## First Principles

- Severity should reflect user harm and data risk, not internal embarrassment.
- A postmortem is incomplete if key timeline or remediation details are missing.
- Follow-up work matters more than blame assignment.

## Workflow

1. State impact, owner, channel, and severity.
2. Stabilize the system before optimizing the fix.
3. Record the timeline while facts are fresh.
4. Convert causes into owned action items.

## Minimal Code Mental Model

```python
severity = incident_severity(user_impacting=True, duration_minutes=45, data_loss=False)
missing = missing_postmortem_sections(postmortem)
complete = postmortem_complete(postmortem, action_items=["add retry budget alert"])
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Severity based on team embarrassment | Response does not match user harm |
| Missing timeline | The team cannot reason about detection and recovery gaps |
| No action items | The same incident can repeat |

## Function

```python
def incident_severity(user_impacting: bool, duration_minutes: int, data_loss: bool) -> str:
def missing_postmortem_sections(
    postmortem: dict[str, str],
    required_sections: list[str] | None = None,
) -> list[str]:
def postmortem_complete(postmortem: dict[str, str], action_items: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/incidents-and-postmortems/python -q
```
