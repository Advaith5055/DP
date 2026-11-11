def min_cost_to_cut_stick(length, cuts):
    points = [0] + sorted(cuts) + [length]
    count = len(points)
    dp = [[0] * count for _ in range(count)]

    for gap in range(2, count):
        for left in range(count - gap):
            right = left + gap
            dp[left][right] = min(
                points[right] - points[left] + dp[left][middle] + dp[middle][right]
                for middle in range(left + 1, right)
            )

    return dp[0][-1]


assert min_cost_to_cut_stick(7, [1, 3, 4, 5]) == 16
assert min_cost_to_cut_stick(9, [5, 6, 1, 4, 2]) == 22
