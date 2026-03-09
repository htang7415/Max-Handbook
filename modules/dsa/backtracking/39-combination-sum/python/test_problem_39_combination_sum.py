from problem_39_combination_sum import Solution


def test_combination_sum_example():
    result = Solution().combinationSum([2, 3, 6, 7], 7)
    assert sorted(sorted(combo) for combo in result) == [[2, 2, 3], [7]]


def test_combination_sum_edge_no_solution():
    result = Solution().combinationSum([2], 1)
    assert result == []


def test_combination_sum_tricky_reuse_and_pruning():
    result = Solution().combinationSum([2, 3, 5], 8)
    assert sorted(sorted(combo) for combo in result) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
