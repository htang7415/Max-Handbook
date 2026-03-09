from answer_frequency_table import answer_frequency_table


def test_answer_frequency_table_counts_normalized_answers() -> None:
    counts = answer_frequency_table(["Paris", "the paris", "London", "Rome"])

    assert counts == {"paris": 2, "london": 1, "rome": 1}


def test_answer_frequency_table_returns_empty_dict_for_empty_input() -> None:
    assert answer_frequency_table([]) == {}


def test_answer_frequency_table_keeps_distinct_normalized_answers_separate() -> None:
    counts = answer_frequency_table(["A", "B", "B"])

    assert counts == {"": 1, "b": 2}
