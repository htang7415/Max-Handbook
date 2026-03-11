import sqlite3

import pytest

from one_to_many_and_many_to_many import (
    create_connection,
    create_relationship_schema,
    document_chunk_counts,
    document_tag_names,
    insert_chunk,
    insert_document,
    insert_tag,
    link_document_tag,
)


def build_connection():
    conn = create_connection()
    create_relationship_schema(conn)
    spec_id = insert_document(conn, "spec")
    notes_id = insert_document(conn, "notes")
    insert_chunk(conn, spec_id, 0, "chunk a")
    insert_chunk(conn, spec_id, 1, "chunk b")
    rag_id = insert_tag(conn, "rag")
    eval_id = insert_tag(conn, "eval")
    link_document_tag(conn, spec_id, rag_id)
    link_document_tag(conn, spec_id, eval_id)
    link_document_tag(conn, notes_id, rag_id)
    return conn, spec_id, rag_id


def test_one_to_many_counts_children_per_parent() -> None:
    conn, _, _ = build_connection()

    assert document_chunk_counts(conn) == [
        ("spec", 2),
        ("notes", 0),
    ]


def test_many_to_many_returns_tags_through_the_join_table() -> None:
    conn, _, _ = build_connection()

    assert document_tag_names(conn, "spec") == ["eval", "rag"]
    assert document_tag_names(conn, "notes") == ["rag"]


def test_join_table_blocks_duplicate_relationships() -> None:
    conn, spec_id, rag_id = build_connection()

    with pytest.raises(sqlite3.IntegrityError):
        link_document_tag(conn, spec_id, rag_id)
