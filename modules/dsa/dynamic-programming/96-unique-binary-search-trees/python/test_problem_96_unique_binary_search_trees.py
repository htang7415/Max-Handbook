from problem_96_unique_binary_search_trees import Solution


def test_unique_bst_example():
    assert Solution().numTrees(3) == 5


def test_unique_bst_edge_single():
    assert Solution().numTrees(1) == 1


def test_unique_bst_tricky_four_nodes():
    assert Solution().numTrees(4) == 14
