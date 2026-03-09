from problem_376_wiggle_subsequence import Solution


def test_wiggle_example():
    assert Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6


def test_wiggle_edge_single():
    assert Solution().wiggleMaxLength([1]) == 1


def test_wiggle_tricky_flat():
    assert Solution().wiggleMaxLength([1, 1, 1, 1]) == 1
