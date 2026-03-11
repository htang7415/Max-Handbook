# API Contract Basics

> Track: `software-engineering` | Topic: `apis`

## Concept

An API contract is the set of method, path, path parameters, success conditions, and payload expectations that clients can depend on.

## Key Points

- Contract design starts with semantics, not with framework routes.
- Path parameters should be explicit and unique.
- Success responses and request body rules should be validated before implementation details grow around them.

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
