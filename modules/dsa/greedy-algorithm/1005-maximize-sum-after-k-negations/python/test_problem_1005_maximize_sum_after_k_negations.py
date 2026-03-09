from problem_1005_maximize_sum_after_k_negations import Solution


def test_k_negations_example():
    assert Solution().largestSumAfterKNegations([4, 2, 3], 1) == 5


def test_k_negations_edge_zero_absorbs_flip():
    assert Solution().largestSumAfterKNegations([3, -1, 0, 2], 3) == 6


def test_k_negations_tricky_odd_leftover():
    assert Solution().largestSumAfterKNegations([2, -3, -1, 5, -4], 2) == 13
