from problem_46_permutations import Solution


def test_permutations_example():
    result = Solution().permute([1, 2, 3])
    assert len(result) == 6
    assert [1, 2, 3] in result
    assert [3, 2, 1] in result


def test_permutations_edge_single():
    assert Solution().permute([1]) == [[1]]


def test_permutations_tricky_zero_included():
    result = Solution().permute([0, 1])
    assert sorted(result) == [[0, 1], [1, 0]]
