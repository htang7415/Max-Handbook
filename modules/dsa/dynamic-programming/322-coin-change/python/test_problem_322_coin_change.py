from problem_322_coin_change import Solution


def test_coin_change_example():
    assert Solution().coinChange([1, 2, 5], 11) == 3


def test_coin_change_edge_zero_amount():
    assert Solution().coinChange([2], 0) == 0


def test_coin_change_tricky_impossible():
    assert Solution().coinChange([2], 3) == -1
