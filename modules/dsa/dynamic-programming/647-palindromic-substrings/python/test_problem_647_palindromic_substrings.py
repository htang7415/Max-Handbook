from problem_647_palindromic_substrings import Solution


def test_palindromic_substrings_example():
    assert Solution().countSubstrings("abc") == 3


def test_palindromic_substrings_edge_empty():
    assert Solution().countSubstrings("") == 0


def test_palindromic_substrings_tricky_repeated():
    assert Solution().countSubstrings("aaa") == 6
