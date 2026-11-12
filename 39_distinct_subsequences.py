def count_distinct_subsequences(source, target):
    counts = [0] * (len(target) + 1)
    counts[0] = 1

    for character in source:
        for index in range(len(target) - 1, -1, -1):
            if character == target[index]:
                counts[index + 1] += counts[index]

    return counts[-1]


assert count_distinct_subsequences("rabbbit", "rabbit") == 3
assert count_distinct_subsequences("babgbag", "bag") == 5
