from problem_51_n_queens import Solution


def test_n_queens_example():
    result = Solution().solveNQueens(4)
    assert len(result) == 2


def test_n_queens_edge_one():
    assert Solution().solveNQueens(1) == [["Q"]]


def test_n_queens_tricky_no_solution():
    assert Solution().solveNQueens(2) == []
