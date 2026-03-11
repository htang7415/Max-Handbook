from __future__ import annotations

import re


def extract_path_parameters(path: str) -> list[str]:
    normalized = path.strip()
    if not normalized.startswith("/"):
        raise ValueError("path must start with '/'")
    params = re.findall(r"{([^{}]+)}", normalized)
    if len(params) != len(set(params)):
        raise ValueError("path parameters must be unique")
    return params


def validate_endpoint_contract(
    method: str,
    path: str,
    request_body_fields: list[str],
    success_statuses: list[int],
) -> None:
    normalized_method = method.strip().upper()
    if normalized_method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
        raise ValueError("unsupported HTTP method")

    extract_path_parameters(path)
    cleaned_body_fields = [field.strip() for field in request_body_fields if field.strip()]
    if normalized_method == "GET" and cleaned_body_fields:
        raise ValueError("GET endpoints should not require request body fields")
    if not success_statuses or not all(200 <= status < 300 for status in success_statuses):
        raise ValueError("success_statuses must contain only 2xx codes")


def make_endpoint_summary(
    method: str,
    path: str,
    request_body_fields: list[str],
    response_fields: list[str],
) -> dict[str, object]:
    validate_endpoint_contract(method, path, request_body_fields, [200])
    return {
        "method": method.strip().upper(),
        "path": path.strip(),
        "path_params": extract_path_parameters(path),
        "request_body_fields": [field.strip() for field in request_body_fields if field.strip()],
        "response_fields": [field.strip() for field in response_fields if field.strip()],
    }
