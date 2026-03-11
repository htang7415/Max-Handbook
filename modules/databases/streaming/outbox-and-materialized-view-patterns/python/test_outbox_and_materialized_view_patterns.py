import pytest

from outbox_and_materialized_view_patterns import (
    create_connection,
    create_pipeline_tables,
    next_unprojected_event,
    order_rows,
    outbox_event_rows,
    project_next_event,
    rebuild_workspace_status_view,
    workspace_status_totals,
    write_order_status,
)


def test_outbox_write_rolls_back_if_event_cannot_be_created():
    conn = create_connection()
    create_pipeline_tables(conn)

    with pytest.raises(RuntimeError):
        write_order_status(
            conn,
            order_id="o1",
            workspace_id=7,
            status="placed",
            fail_before_outbox=True,
        )

    assert order_rows(conn) == []
    assert outbox_event_rows(conn) == []


def test_projected_view_matches_full_rebuild():
    conn = create_connection()
    create_pipeline_tables(conn)

    write_order_status(conn, "o1", 7, "placed")
    write_order_status(conn, "o2", 7, "placed")
    write_order_status(conn, "o1", 7, "completed")

    while project_next_event(conn) is not None:
        pass

    assert next_unprojected_event(conn) is None
    assert workspace_status_totals(conn, 7) == {"completed": 1, "placed": 1}

    rebuilt = rebuild_workspace_status_view(
        [(order_id, workspace_id, status) for _, order_id, workspace_id, status, _ in outbox_event_rows(conn)]
    )
    assert rebuilt[7] == {"completed": 1, "placed": 1}
