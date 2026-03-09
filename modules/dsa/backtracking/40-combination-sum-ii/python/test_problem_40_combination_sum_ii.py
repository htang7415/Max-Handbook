from problem_40_combination_sum_ii import Solution


def test_combination_sum_ii_example():
    result = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    assert sorted(sorted(combo) for combo in result) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]


def test_combination_sum_ii_edge_no_solution():
    result = Solution().combinationSum2([3], 2)
    assert result == []


def test_combination_sum_ii_tricky_duplicates():
    result = Solution().combinationSum2([2, 5, 2, 1, 2], 5)
    assert sorted(sorted(combo) for combo in result) == [[1, 2, 2], [5]]
