from __future__ import annotations

from collections.abc import Callable


def failing_cases(cases: list[object], predicate: Callable[[object], bool]) -> list[object]:
    return [case for case in cases if not predicate(case)]


def property_holds(cases: list[object], predicate: Callable[[object], bool]) -> bool:
    return not failing_cases(cases, predicate)


def reverse_twice_property(text: str) -> bool:
    return text[::-1][::-1] == text


def sum_commutative_property(pair: tuple[int, int]) -> bool:
    left, right = pair
    return left + right == right + left
