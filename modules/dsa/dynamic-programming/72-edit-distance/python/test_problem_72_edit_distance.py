from problem_72_edit_distance import Solution


def test_edit_distance_example():
    assert Solution().minDistance("horse", "ros") == 3


def test_edit_distance_edge_empty():
    assert Solution().minDistance("", "abc") == 3


def test_edit_distance_tricky_longer():
    assert Solution().minDistance("intention", "execution") == 5
