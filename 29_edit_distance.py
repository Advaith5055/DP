def edit_distance(first, second):
    previous = list(range(len(second) + 1))

    for first_index, first_char in enumerate(first, start=1):
        current = [first_index]
        for second_index, second_char in enumerate(second, start=1):
            if first_char == second_char:
                current.append(previous[second_index - 1])
            else:
                current.append(
                    1 + min(
                        previous[second_index],
                        current[second_index - 1],
                        previous[second_index - 1],
                    )
                )
        previous = current

    return previous[-1]


assert edit_distance("horse", "ros") == 3
assert edit_distance("intention", "execution") == 5
assert edit_distance("", "abc") == 3
