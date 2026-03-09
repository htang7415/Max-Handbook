from problem_738_monotone_increasing_digits import Solution


def test_monotone_digits_example():
    assert Solution().monotoneIncreasingDigits(10) == 9


def test_monotone_digits_edge_already_monotone():
    assert Solution().monotoneIncreasingDigits(1234) == 1234


def test_monotone_digits_tricky_cascade():
    assert Solution().monotoneIncreasingDigits(332) == 299
