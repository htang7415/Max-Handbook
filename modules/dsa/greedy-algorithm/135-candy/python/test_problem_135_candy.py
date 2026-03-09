from problem_135_candy import Solution


def test_candy_example():
    assert Solution().candy([1, 0, 2]) == 5


def test_candy_edge_single():
    assert Solution().candy([1]) == 1


def test_candy_tricky_equal_tail():
    assert Solution().candy([1, 2, 2]) == 4
