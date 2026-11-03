def max_knapsack_value(weights, values, capacity):
    best = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            best[current_capacity] = max(
                best[current_capacity], best[current_capacity - weight] + value
            )
    return best[capacity]


assert max_knapsack_value([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
assert max_knapsack_value([2, 3, 4], [4, 5, 6], 5) == 9
assert max_knapsack_value([1], [10], 0) == 0
