from normalization_vs_denormalization import (
    create_connection,
    create_normalization_demo_schema,
    denormalized_order_feed,
    insert_customer,
    insert_order_rows,
    normalized_order_feed,
    rename_customer,
)


def build_connection():
    conn = create_connection()
    create_normalization_demo_schema(conn)
    customer_id = insert_customer(conn, "Acme")
    insert_order_rows(conn, customer_id, ["A-1", "A-2"])
    return conn, customer_id


def test_normalized_and_denormalized_feeds_start_with_same_read_output() -> None:
    conn, _ = build_connection()

    assert normalized_order_feed(conn) == denormalized_order_feed(conn) == [
        ("Acme", "A-1"),
        ("Acme", "A-2"),
    ]


def test_customer_rename_touches_one_normalized_row_but_many_denormalized_rows() -> None:
    conn, customer_id = build_connection()

    assert rename_customer(conn, customer_id, "Acme Labs") == (1, 2)


def test_both_models_can_serve_the_same_read_after_syncing_the_duplicate_field() -> None:
    conn, customer_id = build_connection()
    rename_customer(conn, customer_id, "Acme Labs")

    assert normalized_order_feed(conn) == denormalized_order_feed(conn) == [
        ("Acme Labs", "A-1"),
        ("Acme Labs", "A-2"),
    ]
