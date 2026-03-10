from problem_300_longest_increasing_subsequence import Solution


def test_lis_example():
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_lis_edge_empty():
    assert Solution().lengthOfLIS([]) == 0


def test_lis_tricky_duplicates():
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4


def test_lis_tricky_tail_replacement():
    assert Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3
