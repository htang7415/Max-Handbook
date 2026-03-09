from problem_134_gas_station import Solution


def test_gas_station_example():
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_gas_station_edge_impossible():
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1


def test_gas_station_tricky_single_station():
    assert Solution().canCompleteCircuit([5], [4]) == 0
