"""when_postgres_is_enough - simple heuristics for staying relational versus moving to NoSQL."""

from __future__ import annotations


def recommend_store(
    needs_joins: bool,
    needs_transactions: bool,
    simple_key_access: bool,
    extreme_write_scale: bool,
    ad_hoc_queries: bool = True,
) -> str:
    relational_score = 0
    nosql_score = 0

    if needs_joins:
        relational_score += 2
    if needs_transactions:
        relational_score += 2
    if ad_hoc_queries:
        relational_score += 1
    if simple_key_access:
        nosql_score += 2
    if extreme_write_scale:
        nosql_score += 2

    return "postgres" if relational_score >= nosql_score else "nosql"


def decision_summary(
    needs_joins: bool,
    needs_transactions: bool,
    simple_key_access: bool,
    extreme_write_scale: bool,
    ad_hoc_queries: bool = True,
) -> dict[str, object]:
    recommendation = recommend_store(
        needs_joins,
        needs_transactions,
        simple_key_access,
        extreme_write_scale,
        ad_hoc_queries,
    )
    return {
        "recommendation": recommendation,
        "needs_joins": needs_joins,
        "needs_transactions": needs_transactions,
        "simple_key_access": simple_key_access,
        "extreme_write_scale": extreme_write_scale,
        "ad_hoc_queries": ad_hoc_queries,
    }
