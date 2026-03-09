from problem_78_subsets import Solution


def test_subsets_example():
    result = Solution().subsets([1, 2])
    assert sorted(result) == [[], [1], [1, 2], [2]]


def test_subsets_edge_empty():
    assert Solution().subsets([]) == [[]]


def test_subsets_tricky_three_elements():
    result = Solution().subsets([1, 2, 3])
    assert len(result) == 8
