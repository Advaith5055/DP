def minimum_multiplications(dimensions):
    matrix_count = len(dimensions) - 1
    costs = [[0] * matrix_count for _ in range(matrix_count)]

    for length in range(2, matrix_count + 1):
        for start in range(matrix_count - length + 1):
            end = start + length - 1
            costs[start][end] = float("inf")
            for split in range(start, end):
                cost = (
                    costs[start][split]
                    + costs[split + 1][end]
                    + dimensions[start] * dimensions[split + 1] * dimensions[end + 1]
                )
                costs[start][end] = min(costs[start][end], cost)

    return costs[0][matrix_count - 1] if matrix_count else 0


assert minimum_multiplications([10, 30, 5, 60]) == 4500
assert minimum_multiplications([40, 20, 30, 10, 30]) == 26000
assert minimum_multiplications([10, 20]) == 0
