from problem_47_permutations_ii import Solution


def test_permutations_unique_example():
    result = Solution().permuteUnique([1, 1, 2])
    assert sorted(result) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]


def test_permutations_unique_edge_single():
    assert Solution().permuteUnique([1]) == [[1]]


def test_permutations_unique_tricky_all_same():
    assert Solution().permuteUnique([2, 2, 2]) == [[2, 2, 2]]
