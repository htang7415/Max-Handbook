from problem_232_implement_queue_using_stacks import MyQueue


def test_queue_example():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() is False
    assert queue.pop() == 2
    assert queue.empty() is True


def test_queue_edge_single():
    queue = MyQueue()
    queue.push(5)
    assert queue.peek() == 5
    assert queue.pop() == 5
    assert queue.empty() is True


def test_queue_tricky_interleaved_transfers():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    queue.push(3)
    assert queue.peek() == 2
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.empty() is True
