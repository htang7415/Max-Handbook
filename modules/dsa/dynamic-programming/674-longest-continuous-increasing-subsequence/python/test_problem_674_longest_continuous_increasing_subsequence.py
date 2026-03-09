from problem_674_longest_continuous_increasing_subsequence import Solution


def test_lcis_example():
    assert Solution().findLengthOfLCIS([1, 3, 5, 4, 7]) == 3


def test_lcis_edge_empty():
    assert Solution().findLengthOfLCIS([]) == 0


def test_lcis_tricky_flat():
    assert Solution().findLengthOfLCIS([2, 2, 2, 2]) == 1
