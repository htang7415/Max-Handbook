from problem_968_binary_tree_cameras import Solution, TreeNode


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


def test_binary_tree_cameras_example():
    root = build_tree([0, 0, None, 0, 0])
    assert Solution().minCameraCover(root) == 1


def test_binary_tree_cameras_edge_empty():
    assert Solution().minCameraCover(None) == 0


def test_binary_tree_cameras_tricky_chain():
    root = build_tree([0, 0, None, 0, None, 0, None, None, 0])
    assert Solution().minCameraCover(root) == 2
