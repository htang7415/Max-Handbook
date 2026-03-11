from __future__ import annotations

import pytest

from api_contract_basics import (
    extract_path_parameters,
    make_endpoint_summary,
    validate_endpoint_contract,
)


def test_extract_path_parameters_returns_parameters_in_order() -> None:
    assert extract_path_parameters("/v1/workspaces/{workspace_id}/documents/{document_id}") == [
        "workspace_id",
        "document_id",
    ]


def test_validate_endpoint_contract_rejects_invalid_get_body_and_statuses() -> None:
    with pytest.raises(ValueError):
        validate_endpoint_contract("GET", "/v1/documents", ["title"], [200])
    with pytest.raises(ValueError):
        validate_endpoint_contract("POST", "/v1/documents", ["title"], [200, 404])


def test_make_endpoint_summary_normalizes_method_and_fields() -> None:
    summary = make_endpoint_summary(
        " post ",
        "/v1/documents",
        [" title ", "workspace_id"],
        [" id ", "title"],
    )

    assert summary == {
        "method": "POST",
        "path": "/v1/documents",
        "path_params": [],
        "request_body_fields": ["title", "workspace_id"],
        "response_fields": ["id", "title"],
    }
