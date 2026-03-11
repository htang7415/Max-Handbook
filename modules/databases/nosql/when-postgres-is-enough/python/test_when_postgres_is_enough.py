from when_postgres_is_enough import decision_summary, recommend_store


def test_relational_product_requirements_prefer_postgres() -> None:
    assert (
        recommend_store(
            needs_joins=True,
            needs_transactions=True,
            simple_key_access=False,
            extreme_write_scale=False,
            ad_hoc_queries=True,
        )
        == "postgres"
    )


def test_extreme_simple_key_workload_can_tip_toward_nosql() -> None:
    summary = decision_summary(
        needs_joins=False,
        needs_transactions=False,
        simple_key_access=True,
        extreme_write_scale=True,
        ad_hoc_queries=False,
    )

    assert summary["recommendation"] == "nosql"
