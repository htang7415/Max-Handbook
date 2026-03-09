from problem_202_happy_number import is_happy


def test_is_happy_example():
    assert is_happy(19) is True


def test_is_happy_edge_one():
    assert is_happy(1) is True


def test_is_happy_tricky_cycle():
    assert is_happy(2) is False
