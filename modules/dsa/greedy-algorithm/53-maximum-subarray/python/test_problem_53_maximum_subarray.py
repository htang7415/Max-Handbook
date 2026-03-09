from problem_53_maximum_subarray import Solution


def test_max_subarray_example():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_edge_all_negative():
    assert Solution().maxSubArray([-2, -1]) == -1


def test_max_subarray_tricky_late_run():
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23
