import sqlite3

import pytest

from entity_resolution_keys import (
    attach_resolution_key,
    create_connection,
    create_entity_resolution_schema,
    insert_entity,
    keys_for_entity,
    resolve_entity_id,
)


def test_multiple_external_keys_can_resolve_to_one_canonical_entity() -> None:
    conn = create_connection()
    create_entity_resolution_schema(conn)

    entity_id = insert_entity(conn, "Acme Labs")
    attach_resolution_key(conn, entity_id, "crm", "acct-42", "account-id")
    attach_resolution_key(conn, entity_id, "billing", "cus_123", "customer-id")

    assert resolve_entity_id(conn, "crm", "acct-42") == entity_id
    assert resolve_entity_id(conn, "billing", "cus_123") == entity_id
    assert keys_for_entity(conn, entity_id) == [
        ("billing", "cus_123", "customer-id"),
        ("crm", "acct-42", "account-id"),
    ]


def test_same_source_key_cannot_point_to_two_entities() -> None:
    conn = create_connection()
    create_entity_resolution_schema(conn)

    first = insert_entity(conn, "Acme Labs")
    second = insert_entity(conn, "Acme Research")
    attach_resolution_key(conn, first, "crm", "acct-42", "account-id")

    with pytest.raises(sqlite3.IntegrityError):
        attach_resolution_key(conn, second, "crm", "acct-42", "account-id")
