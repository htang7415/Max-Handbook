from __future__ import annotations

from property_based_testing_basics import (
    failing_cases,
    property_holds,
    reverse_twice_property,
    sum_commutative_property,
)


def test_property_holds_for_reverse_twice_and_commutative_sum() -> None:
    assert property_holds(["abc", "", "racecar"], reverse_twice_property) is True
    assert property_holds([(1, 2), (3, 5), (0, 0)], sum_commutative_property) is True


def test_failing_cases_returns_counterexamples() -> None:
    predicate = lambda n: n % 2 == 0

    assert failing_cases([2, 4, 5, 7], predicate) == [5, 7]


def test_property_helpers_work_with_empty_case_lists() -> None:
    assert failing_cases([], reverse_twice_property) == []
    assert property_holds([], reverse_twice_property) is True
