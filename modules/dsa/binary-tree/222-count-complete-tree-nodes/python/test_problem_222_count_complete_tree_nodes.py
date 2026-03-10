from problem_222_count_complete_tree_nodes import Solution, TreeNode


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def test_count_nodes_example():
    root = build_tree([1, 2, 3, 4, 5, 6])
    assert Solution().countNodes(root) == 6


def test_count_nodes_edge_empty():
    assert Solution().countNodes(None) == 0


def test_count_nodes_tricky_last_level_partial():
    root = build_tree([1, 2, 3, 4, 5])
    assert Solution().countNodes(root) == 5


def test_count_nodes_tricky_perfect_tree():
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert Solution().countNodes(root) == 7
