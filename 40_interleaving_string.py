def is_interleaving(first, second, target):
    if len(first) + len(second) != len(target):
        return False

    possible = [False] * (len(second) + 1)
    possible[0] = True

    for index in range(1, len(second) + 1):
        possible[index] = possible[index - 1] and second[index - 1] == target[index - 1]

    for first_index in range(1, len(first) + 1):
        possible[0] = possible[0] and first[first_index - 1] == target[first_index - 1]
        for second_index in range(1, len(second) + 1):
            target_index = first_index + second_index - 1
            possible[second_index] = (
                possible[second_index] and first[first_index - 1] == target[target_index]
            ) or (
                possible[second_index - 1] and second[second_index - 1] == target[target_index]
            )

    return possible[-1]


assert is_interleaving("aabcc", "dbbca", "aadbbcbcac") is True
assert is_interleaving("aabcc", "dbbca", "aadbbbaccc") is False
