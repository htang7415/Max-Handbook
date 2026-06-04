# API Contract Basics

> Track: `software-engineering` | Topic: `apis`

## Concept

An API contract is the set of method, path, path parameters, success conditions, and payload expectations that clients can depend on.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| New endpoint | A client will depend on method, path, body, and response fields | The behavior is still private implementation detail |
| Endpoint review | You need to catch route, body, or status-code ambiguity before coding | The only change is internal refactoring |
| API documentation | The contract should be inspectable without reading handler code | The API is not intended for another caller |

## First Principles

- Contract design starts with semantics, not with framework routes.
- Path parameters should be explicit and unique.
- Success responses and request body rules should be validated before implementation details grow around them.

## Workflow

1. Choose the method and path from the resource semantics.
2. Extract path parameters and reject duplicates.
3. Decide whether the method should accept a request body.
4. Define success statuses as 2xx outcomes only.
5. Summarize request and response fields for review.

## Minimal Code Mental Model

```python
params = extract_path_parameters("/v1/workspaces/{workspace_id}/documents/{document_id}")
validate_endpoint_contract("GET", "/v1/documents/{document_id}", [], [200])
summary = make_endpoint_summary(
    "POST",
    "/v1/documents",
    ["title", "workspace_id"],
    ["id", "title"],
)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Duplicate path parameter | Callers cannot tell which value wins | `extract_path_parameters` rejects duplicates |
| GET requires a body | Client and cache behavior becomes ambiguous | `validate_endpoint_contract` rejects GET body fields |
| Non-2xx success status | Error behavior looks like success | `validate_endpoint_contract` enforces 2xx statuses |

## Function

```python
def extract_path_parameters(path: str) -> list[str]:
def validate_endpoint_contract(
    method: str,
    path: str,
    request_body_fields: list[str],
    success_statuses: list[int],
) -> None:
def make_endpoint_summary(
    method: str,
    path: str,
    request_body_fields: list[str],
    response_fields: list[str],
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/software-engineering/apis/api-contract-basics/python -q
```
