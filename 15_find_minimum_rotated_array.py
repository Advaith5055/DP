def find_minimum(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        middle = (left + right) // 2

        if numbers[middle] > numbers[right]:
            left = middle + 1
        else:
            right = middle

    return numbers[left]


assert find_minimum([3, 4, 5, 1, 2]) == 1
assert find_minimum([4, 5, 6, 7, 0, 1, 2]) == 0
assert find_minimum([1, 2, 3]) == 1
