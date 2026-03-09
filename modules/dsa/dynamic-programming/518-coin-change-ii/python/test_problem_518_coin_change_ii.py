from problem_518_coin_change_ii import Solution


def test_coin_change_ii_example():
    assert Solution().change(5, [1, 2, 5]) == 4


def test_coin_change_ii_edge_zero_amount():
    assert Solution().change(0, [1, 2, 5]) == 1


def test_coin_change_ii_tricky_limited_choices():
    assert Solution().change(7, [2, 3, 5]) == 2
