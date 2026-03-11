from entity_vs_event_tables import (
    append_job_event,
    create_connection,
    create_entity_event_schema,
    current_state_from_entity_table,
    current_state_from_event_table,
    upsert_job_state,
)


def build_connection():
    conn = create_connection()
    create_entity_event_schema(conn)
    upsert_job_state(conn, "run-1", "running")
    upsert_job_state(conn, "run-1", "completed")
    upsert_job_state(conn, "run-2", "failed")
    append_job_event(conn, "run-1", "queued", "2026-03-11T09:55:00Z")
    append_job_event(conn, "run-1", "running", "2026-03-11T10:00:00Z")
    append_job_event(conn, "run-1", "completed", "2026-03-11T10:10:00Z")
    append_job_event(conn, "run-2", "failed", "2026-03-11T10:05:00Z")
    return conn


def test_entity_table_answers_current_state_directly() -> None:
    conn = build_connection()

    assert current_state_from_entity_table(conn) == {
        "run-1": "completed",
        "run-2": "failed",
    }


def test_event_table_can_reconstruct_current_state_from_history() -> None:
    conn = build_connection()

    assert current_state_from_event_table(conn) == {
        "run-1": "completed",
        "run-2": "failed",
    }


def test_entity_and_event_state_can_stay_consistent_when_both_are_maintained() -> None:
    conn = build_connection()

    assert current_state_from_entity_table(conn) == current_state_from_event_table(conn)
