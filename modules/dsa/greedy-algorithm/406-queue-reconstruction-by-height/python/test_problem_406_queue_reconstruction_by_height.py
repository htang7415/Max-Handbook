from problem_406_queue_reconstruction_by_height import Solution


def test_reconstruct_queue_example():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    assert Solution().reconstructQueue(people) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]


def test_reconstruct_queue_edge_single():
    assert Solution().reconstructQueue([[5, 0]]) == [[5, 0]]


def test_reconstruct_queue_tricky_all_zero_k():
    people = [[6, 0], [5, 0], [4, 0]]
    assert Solution().reconstructQueue(people) == [[4, 0], [5, 0], [6, 0]]
