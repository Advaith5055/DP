def palindrome_partition_cost(text, parts):
    size = len(text)
    cost = [[0] * size for _ in range(size)]

    for length in range(2, size + 1):
        for left in range(size - length + 1):
            right = left + length - 1
            cost[left][right] = cost[left + 1][right - 1] if length > 2 else 0
            if text[left] != text[right]:
                cost[left][right] += 1

    dp = [[float("inf")] * (size + 1) for _ in range(parts + 1)]
    dp[0][0] = 0

    for group in range(1, parts + 1):
        for end in range(group, size + 1):
            for start in range(group - 1, end):
                dp[group][end] = min(dp[group][end], dp[group - 1][start] + cost[start][end - 1])

    return dp[parts][size]


assert palindrome_partition_cost("abc", 2) == 1
assert palindrome_partition_cost("aabbc", 3) == 0
