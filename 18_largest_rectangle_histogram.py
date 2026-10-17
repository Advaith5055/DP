def largest_rectangle_area(heights):
    stack = []
    best = 0

    for index, height in enumerate(heights + [0]):
        start = index
        while stack and stack[-1][1] > height:
            previous_index, previous_height = stack.pop()
            best = max(best, previous_height * (index - previous_index))
            start = previous_index
        stack.append((start, height))

    return best


assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle_area([2, 4]) == 4
