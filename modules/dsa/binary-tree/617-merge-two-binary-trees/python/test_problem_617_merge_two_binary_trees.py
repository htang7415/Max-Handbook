from problem_617_merge_two_binary_trees import Solution, TreeNode


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


def level_order(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []
    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def test_merge_trees_example():
    t1 = build_tree([1, 3, 2, 5])
    t2 = build_tree([2, 1, 3, None, 4, None, 7])
    merged = Solution().mergeTrees(t1, t2)
    assert level_order(merged) == [3, 4, 5, 5, 4, None, 7]


def test_merge_trees_edge_one_empty():
    t2 = build_tree([2, 1, 3])
    merged = Solution().mergeTrees(None, t2)
    assert level_order(merged) == [2, 1, 3]


def test_merge_trees_tricky_disjoint_shapes():
    t1 = build_tree([1, None, 2])
    t2 = build_tree([3, 4, None])
    merged = Solution().mergeTrees(t1, t2)
    assert level_order(merged) == [4, 4, 2]
