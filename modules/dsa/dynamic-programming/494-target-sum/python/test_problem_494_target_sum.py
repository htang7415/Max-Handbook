from problem_494_target_sum import Solution


def test_target_sum_example():
    assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5


def test_target_sum_edge_unreachable():
    assert Solution().findTargetSumWays([1], 2) == 0


def test_target_sum_tricky_zero_multipliers():
    assert Solution().findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1) == 256
