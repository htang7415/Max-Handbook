from problem_77_combinations_optimized import Solution


def test_combinations_optimized_example():
    result = Solution().combine(4, 2)
    assert sorted(result) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


def test_combinations_optimized_edge_k_zero():
    assert Solution().combine(4, 0) == [[]]


def test_combinations_optimized_tricky_k_equals_n():
    assert Solution().combine(4, 4) == [[1, 2, 3, 4]]
