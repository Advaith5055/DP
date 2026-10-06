def max_subarray_sum(numbers):
    best = current = numbers[0]

    for number in numbers[1:]:
        current = max(number, current + number)
        best = max(best, current)

    return best


assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray_sum([5]) == 5
assert max_subarray_sum([-4, -2, -7]) == -2
