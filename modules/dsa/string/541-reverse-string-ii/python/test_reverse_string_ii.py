from reverse_string_ii import Solution


def test_reverse_string_ii_example():
    assert Solution().reverseStr("abcdefg", 2) == "bacdfeg"


def test_reverse_string_ii_edge_shorter_than_k():
    assert Solution().reverseStr("abc", 4) == "cba"


def test_reverse_string_ii_tricky_partial_tail():
    assert Solution().reverseStr("abcdefgh", 3) == "cbadefhg"
