from problem_383_ransom_note import can_construct


def test_can_construct_example():
    assert can_construct("aab", "baa") is True


def test_can_construct_edge_empty_note():
    assert can_construct("", "abc") is True


def test_can_construct_tricky_insufficient_count():
    assert can_construct("aa", "ab") is False
