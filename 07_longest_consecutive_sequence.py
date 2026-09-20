def longest_consecutive_sequence(numbers: list[int]) -> int:
    values = set(numbers)
    longest = 0

    for number in values:
        if number - 1 not in values:
            length = 1
            while number + length in values:
                length += 1
            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive_sequence([]) == 0
