from collections import deque


def sliding_window_maximum(numbers, window_size):
    maximums = []
    indices = deque()

    for index, number in enumerate(numbers):
        while indices and indices[0] <= index - window_size:
            indices.popleft()

        while indices and numbers[indices[-1]] <= number:
            indices.pop()

        indices.append(index)

        if index >= window_size - 1:
            maximums.append(numbers[indices[0]])

    return maximums


assert sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert sliding_window_maximum([1], 1) == [1]
assert sliding_window_maximum([9, 8, 7], 2) == [9, 8]
