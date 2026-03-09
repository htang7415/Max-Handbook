from problem_203_remove_linked_list_elements import ListNode, remove_linked_list_elements


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


def test_remove_linked_list_elements_example():
    head = build_list([1, 2, 6, 3, 4, 5, 6])
    result = remove_linked_list_elements(head, 6)
    assert to_list(result) == [1, 2, 3, 4, 5]


def test_remove_linked_list_elements_edge_all_removed():
    head = build_list([7, 7, 7])
    result = remove_linked_list_elements(head, 7)
    assert to_list(result) == []


def test_remove_linked_list_elements_tricky_head_run():
    head = build_list([6, 6, 1, 2, 6])
    result = remove_linked_list_elements(head, 6)
    assert to_list(result) == [1, 2]
