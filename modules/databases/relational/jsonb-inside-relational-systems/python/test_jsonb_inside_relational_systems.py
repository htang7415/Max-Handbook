from jsonb_inside_relational_systems import (
    create_connection,
    create_ticket_schema,
    filter_ticket_ids,
    insert_ticket,
    ticket_metadata,
    update_ticket_metadata,
)


def test_filters_mix_relational_columns_and_metadata_terms():
    conn = create_connection()
    create_ticket_schema(conn)

    wanted_id = insert_ticket(
        conn,
        workspace_id=7,
        status="open",
        title="Broken retrieval",
        metadata={"priority": "high", "tags": ["rag", "prod"]},
    )
    insert_ticket(
        conn,
        workspace_id=7,
        status="open",
        title="Warm cache",
        metadata={"priority": "low", "tags": ["cache"]},
    )
    insert_ticket(
        conn,
        workspace_id=8,
        status="open",
        title="Other tenant",
        metadata={"priority": "high", "tags": ["rag"]},
    )

    matches = filter_ticket_ids(
        conn,
        workspace_id=7,
        status="open",
        required_terms=["priority=high", "tag=rag"],
    )

    assert matches == [wanted_id]


def test_updating_metadata_refreshes_extracted_terms():
    conn = create_connection()
    create_ticket_schema(conn)
    ticket_id = insert_ticket(
        conn,
        workspace_id=7,
        status="open",
        title="Pipeline issue",
        metadata={"priority": "low", "tags": ["batch"]},
    )

    update_ticket_metadata(
        conn,
        ticket_id,
        metadata={"priority": "high", "tags": ["streaming", "rag"]},
    )

    assert ticket_metadata(conn, ticket_id)["priority"] == "high"
    assert filter_ticket_ids(conn, 7, required_terms=["priority=low"]) == []
    assert filter_ticket_ids(conn, 7, required_terms=["priority=high", "tag=rag"]) == [
        ticket_id
    ]
