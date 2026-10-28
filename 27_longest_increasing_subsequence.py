def length_of_lis(numbers):
    if not numbers:
        return 0

    lengths = [1] * len(numbers)

    for current in range(len(numbers)):
        for previous in range(current):
            if numbers[previous] < numbers[current]:
                lengths[current] = max(lengths[current], lengths[previous] + 1)

    return max(lengths)


assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert length_of_lis([7, 7, 7]) == 1
