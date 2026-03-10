from reverse_words_in_a_string import Solution


def test_reverse_words_example():
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"


def test_reverse_words_edge_only_spaces():
    assert Solution().reverseWords("   ") == ""


def test_reverse_words_tricky_extra_spaces():
    assert Solution().reverseWords("  hello   world  ") == "world hello"


def test_reverse_words_tricky_multiple_words():
    assert Solution().reverseWords("a good   example") == "example good a"
