from problem_150_evaluate_reverse_polish_notation import Solution


def test_eval_rpn_example():
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9


def test_eval_rpn_edge_single_number():
    assert Solution().evalRPN(["7"]) == 7


def test_eval_rpn_tricky_long_expression():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert Solution().evalRPN(tokens) == 22
