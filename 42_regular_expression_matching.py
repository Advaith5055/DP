def is_match(text, pattern):
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[0][0] = True

    for j in range(2, len(pattern) + 1):
        if pattern[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] in {text[i - 1], "."}:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]
                if pattern[j - 2] in {text[i - 1], "."}:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[-1][-1]


assert is_match("aab", "c*a*b")
assert not is_match("mississippi", "mis*is*p*.")
