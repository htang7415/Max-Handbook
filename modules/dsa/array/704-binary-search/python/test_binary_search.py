from binary_search import Solution


def test_binary_search_example():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_binary_search_edge_empty():
    assert Solution().search([], 7) == -1


def test_binary_search_tricky_left_boundary():
    assert Solution().search([-1, 0, 3, 5, 9, 12], -1) == 0
