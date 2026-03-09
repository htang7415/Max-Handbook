from problem_344_reverse_string import Solution


def test_reverse_string_example():
    chars = ["h", "e", "l", "l", "o"]
    Solution().reverseString(chars)
    assert chars == ["o", "l", "l", "e", "h"]


def test_reverse_string_edge_single():
    chars = ["a"]
    Solution().reverseString(chars)
    assert chars == ["a"]


def test_reverse_string_tricky_even_length():
    chars = ["a", "b", "c", "d"]
    Solution().reverseString(chars)
    assert chars == ["d", "c", "b", "a"]
