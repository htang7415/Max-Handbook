from __future__ import annotations

import pytest

from schema_evolution_and_compatibility import (
    compatibility_summary,
    make_field,
)


def test_adding_optional_field_is_backward_compatible() -> None:
    old_schema = {
        "id": make_field("string", required=True),
        "title": make_field("string", required=True),
    }
    new_schema = {
        "id": make_field("string", required=True),
        "title": make_field("string", required=True),
        "summary": make_field("string"),
    }

    assert compatibility_summary(old_schema, new_schema) == {
        "backward_compatible": True,
        "breaking_changes": [],
        "additive_fields": ["summary"],
    }


def test_removal_type_change_and_required_upgrade_are_breaking() -> None:
    old_schema = {
        "id": make_field("string", required=True),
        "summary": make_field("string"),
        "status": make_field("string"),
    }
    new_schema = {
        "id": make_field("uuid", required=True),
        "status": make_field("string", required=True),
    }

    assert compatibility_summary(old_schema, new_schema) == {
        "backward_compatible": False,
        "breaking_changes": [
            "type changed for field: id",
            "removed field: summary",
            "field became required: status",
        ],
        "additive_fields": [],
    }


def test_make_field_requires_non_empty_type() -> None:
    with pytest.raises(ValueError):
        make_field(" ")
