from problem_151_reverse_words_in_a_string import Solution


def test_reverse_words_example():
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"


def test_reverse_words_edge_extra_spaces():
    assert Solution().reverseWords("  hello   world  ") == "world hello"


def test_reverse_words_tricky_single_word():
    assert Solution().reverseWords("  hello  ") == "hello"
