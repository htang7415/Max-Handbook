from self_referential_relationships import (
    create_connection,
    create_employee_table,
    direct_reports,
    insert_employee,
    management_chain,
)


def test_direct_reports_share_same_parent_row() -> None:
    conn = create_connection()
    create_employee_table(conn)
    ceo_id = insert_employee(conn, "ceo")
    insert_employee(conn, "lead-1", ceo_id)
    insert_employee(conn, "lead-2", ceo_id)

    assert direct_reports(conn, ceo_id) == ["lead-1", "lead-2"]


def test_management_chain_walks_up_to_root() -> None:
    conn = create_connection()
    create_employee_table(conn)
    ceo_id = insert_employee(conn, "ceo")
    lead_id = insert_employee(conn, "lead", ceo_id)
    engineer_id = insert_employee(conn, "engineer", lead_id)

    assert management_chain(conn, engineer_id) == ["lead", "ceo"]
