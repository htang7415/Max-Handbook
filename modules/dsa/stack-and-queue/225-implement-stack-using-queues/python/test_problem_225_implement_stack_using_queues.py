from problem_225_implement_stack_using_queues import MyStack


def test_stack_example():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() is False
    assert stack.pop() == 1
    assert stack.empty() is True


def test_stack_edge_single():
    stack = MyStack()
    stack.push(5)
    assert stack.top() == 5
    assert stack.pop() == 5
    assert stack.empty() is True


def test_stack_tricky_interleaved():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    stack.push(3)
    assert stack.top() == 3
    assert stack.pop() == 3
    assert stack.pop() == 1
