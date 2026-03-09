from problem_257_binary_tree_paths import Solution, TreeNode


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


def test_binary_tree_paths_example():
    root = build_tree([1, 2, 3, None, 5])
    result = Solution().binaryTreePaths(root)
    assert set(result) == {"1->2->5", "1->3"}


def test_binary_tree_paths_edge_empty():
    assert Solution().binaryTreePaths(None) == []


def test_binary_tree_paths_tricky_single_node():
    root = build_tree([1])
    assert Solution().binaryTreePaths(root) == ["1"]
