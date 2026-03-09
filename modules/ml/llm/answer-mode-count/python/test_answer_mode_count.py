from answer_mode_count import answer_mode_count


def test_answer_mode_count_returns_size_of_largest_normalized_vote_block() -> None:
    assert answer_mode_count(["Paris", "the paris", "London", "Rome"]) == 2


def test_answer_mode_count_returns_sample_count_when_all_answers_match() -> None:
    assert answer_mode_count(["Answer", "answer", "the answer"]) == 3


def test_answer_mode_count_returns_zero_for_empty_answers() -> None:
    assert answer_mode_count([]) == 0
