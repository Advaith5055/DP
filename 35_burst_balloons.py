def max_burst_coins(balloons):
    values = [1] + balloons + [1]
    size = len(balloons)
    best = [[0] * (size + 2) for _ in range(size + 2)]

    for length in range(1, size + 1):
        for left in range(1, size - length + 2):
            right = left + length - 1
            for last in range(left, right + 1):
                coins = values[left - 1] * values[last] * values[right + 1]
                best[left][right] = max(
                    best[left][right],
                    best[left][last - 1] + coins + best[last + 1][right],
                )

    return best[1][size] if size else 0


assert max_burst_coins([3, 1, 5, 8]) == 167
assert max_burst_coins([1, 5]) == 10
assert max_burst_coins([]) == 0
