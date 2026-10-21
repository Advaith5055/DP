def find_median_sorted_arrays(first, second):
    if len(first) > len(second):
        first, second = second, first

    total = len(first) + len(second)
    half = total // 2
    left = 0
    right = len(first)

    while left <= right:
        cut_first = (left + right) // 2
        cut_second = half - cut_first

        first_left = first[cut_first - 1] if cut_first else float("-inf")
        first_right = first[cut_first] if cut_first < len(first) else float("inf")
        second_left = second[cut_second - 1] if cut_second else float("-inf")
        second_right = second[cut_second] if cut_second < len(second) else float("inf")

        if first_left <= second_right and second_left <= first_right:
            if total % 2:
                return min(first_right, second_right)
            return (max(first_left, second_left) + min(first_right, second_right)) / 2

        if first_left > second_right:
            right = cut_first - 1
        else:
            left = cut_first + 1


assert find_median_sorted_arrays([1, 3], [2]) == 2
assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
assert find_median_sorted_arrays([], [2, 3]) == 2.5
