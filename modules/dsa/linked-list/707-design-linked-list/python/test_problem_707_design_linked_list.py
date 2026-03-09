from problem_707_design_linked_list import MyLinkedList


def test_design_linked_list_example():
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)
    assert linked_list.get(1) == 2
    linked_list.deleteAtIndex(1)
    assert linked_list.get(1) == 3


def test_design_linked_list_edge_bounds():
    linked_list = MyLinkedList()
    assert linked_list.get(0) == -1
    linked_list.addAtIndex(1, 10)
    assert linked_list.get(0) == -1
    linked_list.addAtIndex(0, 5)
    assert linked_list.get(0) == 5


def test_design_linked_list_tricky_negative_index_and_delete():
    linked_list = MyLinkedList()
    linked_list.addAtIndex(-1, 7)
    linked_list.addAtTail(9)
    linked_list.deleteAtIndex(0)
    assert linked_list.get(0) == 9
