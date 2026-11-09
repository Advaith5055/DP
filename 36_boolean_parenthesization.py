def count_true_parenthesizations(expression):
    values = expression[::2]
    operators = expression[1::2]
    size = len(values)
    true = [[0] * size for _ in range(size)]
    false = [[0] * size for _ in range(size)]

    for index, value in enumerate(values):
        true[index][index] = value == "T"
        false[index][index] = value == "F"

    for length in range(2, size + 1):
        for left in range(size - length + 1):
            right = left + length - 1
            for split in range(left, right):
                left_true = true[left][split]
                left_false = false[left][split]
                right_true = true[split + 1][right]
                right_false = false[split + 1][right]
                total = (left_true + left_false) * (right_true + right_false)
                if operators[split] == "&":
                    true[left][right] += left_true * right_true
                    false[left][right] += total - left_true * right_true
                elif operators[split] == "|":
                    true[left][right] += total - left_false * right_false
                    false[left][right] += left_false * right_false
                else:
                    true[left][right] += left_true * right_false + left_false * right_true
                    false[left][right] += left_true * right_true + left_false * right_false

    return true[0][-1]


assert count_true_parenthesizations("T|F&T") == 2
assert count_true_parenthesizations("T^T^F") == 0
