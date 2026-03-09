from problem_206_reverse_linked_list import ListNode, reverse_linked_list


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


def test_reverse_linked_list_example():
    head = build_list([1, 2, 3])
    result = reverse_linked_list(head)
    assert to_list(result) == [3, 2, 1]


def test_reverse_linked_list_edge_empty():
    assert reverse_linked_list(None) is None


def test_reverse_linked_list_tricky_single():
    head = build_list([1])
    result = reverse_linked_list(head)
    assert to_list(result) == [1]
