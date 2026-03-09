from problem_377_combination_sum_iv import Solution


def test_combination_sum_iv_example():
    assert Solution().combinationSum4([1, 2, 3], 4) == 7


def test_combination_sum_iv_edge_zero_target():
    assert Solution().combinationSum4([1, 2, 3], 0) == 1


def test_combination_sum_iv_tricky_order_matters():
    assert Solution().combinationSum4([1, 2], 3) == 3
