from problem_343_integer_break import Solution


def test_integer_break_example():
    assert Solution().integerBreak(2) == 1


def test_integer_break_edge_three():
    assert Solution().integerBreak(3) == 2


def test_integer_break_tricky_larger():
    assert Solution().integerBreak(10) == 36
