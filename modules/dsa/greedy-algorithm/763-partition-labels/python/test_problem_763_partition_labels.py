from problem_763_partition_labels import Solution


def test_partition_labels_example():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_partition_labels_edge_single_char():
    assert Solution().partitionLabels("a") == [1]


def test_partition_labels_tricky_one_block():
    assert Solution().partitionLabels("eccbbbbdec") == [10]
