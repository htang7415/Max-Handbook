from problem_509_fibonacci_number import Solution


def test_fibonacci_example():
    assert Solution().fib(2) == 1


def test_fibonacci_edge_zero():
    assert Solution().fib(0) == 0


def test_fibonacci_tricky_ten():
    assert Solution().fib(10) == 55
