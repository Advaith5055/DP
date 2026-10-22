def kth_smallest(matrix, k):
    low = matrix[0][0]
    high = matrix[-1][-1]

    while low < high:
        middle = (low + high) // 2
        row = len(matrix) - 1
        column = 0
        count = 0

        while row >= 0 and column < len(matrix[0]):
            if matrix[row][column] <= middle:
                count += row + 1
                column += 1
            else:
                row -= 1

        if count < k:
            low = middle + 1
        else:
            high = middle

    return low


assert kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
assert kth_smallest([[1, 2], [3, 4]], 3) == 3
