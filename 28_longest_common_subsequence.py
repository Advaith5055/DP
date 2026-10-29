def longest_common_subsequence(first, second):
    previous = [0] * (len(second) + 1)

    for first_char in first:
        current = [0]
        for index, second_char in enumerate(second, start=1):
            if first_char == second_char:
                current.append(previous[index - 1] + 1)
            else:
                current.append(max(previous[index], current[-1]))
        previous = current

    return previous[-1]


assert longest_common_subsequence("abcde", "ace") == 3
assert longest_common_subsequence("abc", "abc") == 3
assert longest_common_subsequence("abc", "def") == 0
