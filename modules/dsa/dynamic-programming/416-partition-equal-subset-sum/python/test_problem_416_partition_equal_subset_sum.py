from problem_416_partition_equal_subset_sum import Solution


def test_partition_example():
    assert Solution().canPartition([1, 5, 11, 5]) is True


def test_partition_edge_single():
    assert Solution().canPartition([1]) is False


def test_partition_tricky_false():
    assert Solution().canPartition([1, 2, 3, 5]) is False
