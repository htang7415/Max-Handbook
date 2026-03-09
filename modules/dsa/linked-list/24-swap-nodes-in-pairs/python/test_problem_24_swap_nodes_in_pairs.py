from problem_24_swap_nodes_in_pairs import ListNode, swap_nodes_in_pairs


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_swap_nodes_in_pairs_example():
    head = build_list([1, 2, 3, 4])
    result = swap_nodes_in_pairs(head)
    assert to_list(result) == [2, 1, 4, 3]


def test_swap_nodes_in_pairs_edge_single():
    head = build_list([1])
    result = swap_nodes_in_pairs(head)
    assert to_list(result) == [1]


def test_swap_nodes_in_pairs_tricky_odd():
    head = build_list([1, 2, 3])
    result = swap_nodes_in_pairs(head)
    assert to_list(result) == [2, 1, 3]
