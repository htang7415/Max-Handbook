import sqlite3

import pytest

from embedding_table_design import (
    chunks_missing_model,
    create_connection,
    create_embedding_schema,
    embedding_rows,
    insert_chunk,
    insert_embedding,
)


def build_connection():
    conn = create_connection()
    create_embedding_schema(conn)
    chunk_a = insert_chunk(conn, 7, "spec", "hello")
    chunk_b = insert_chunk(conn, 7, "note", "world")
    return conn, chunk_a, chunk_b


def test_same_chunk_can_have_embeddings_for_different_models() -> None:
    conn, chunk_a, _ = build_connection()
    insert_embedding(conn, chunk_a, "text-embedding-3-small", "job-1", [0.1, 0.2])
    insert_embedding(conn, chunk_a, "text-embedding-3-large", "job-1", [0.3, 0.4])

    assert embedding_rows(conn) == [
        (chunk_a, "text-embedding-3-large", "job-1"),
        (chunk_a, "text-embedding-3-small", "job-1"),
    ]


def test_duplicate_chunk_model_job_combination_is_blocked() -> None:
    conn, chunk_a, _ = build_connection()
    insert_embedding(conn, chunk_a, "text-embedding-3-small", "job-1", [0.1, 0.2])

    with pytest.raises(sqlite3.IntegrityError):
        insert_embedding(conn, chunk_a, "text-embedding-3-small", "job-1", [0.3, 0.4])


def test_missing_chunks_for_a_model_are_easy_to_query() -> None:
    conn, chunk_a, chunk_b = build_connection()
    insert_embedding(conn, chunk_a, "text-embedding-3-small", "job-1", [0.1, 0.2])

    assert chunks_missing_model(conn, "text-embedding-3-small") == [chunk_b]
    assert chunks_missing_model(conn, "text-embedding-3-large") == [chunk_a, chunk_b]
