from problem_90_subsets_ii import Solution


def test_subsets_with_dup_example():
    result = Solution().subsetsWithDup([1, 2, 2])
    assert sorted(result) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]


def test_subsets_with_dup_edge_empty():
    assert Solution().subsetsWithDup([]) == [[]]


def test_subsets_with_dup_tricky_all_duplicates():
    result = Solution().subsetsWithDup([0, 0])
    assert sorted(result) == [[], [0], [0, 0]]
