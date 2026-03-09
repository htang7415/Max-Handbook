from problem_739_daily_temperatures import Solution


def test_daily_temperatures_example():
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    assert Solution().dailyTemperatures(temps) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_daily_temperatures_edge_single():
    assert Solution().dailyTemperatures([30]) == [0]


def test_daily_temperatures_tricky_plateau():
    temps = [70, 70, 71]
    assert Solution().dailyTemperatures(temps) == [2, 1, 0]
