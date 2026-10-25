def pacific_atlantic(heights):
    if not heights:
        return []

    rows = len(heights)
    cols = len(heights[0])

    def reachable(starts):
        seen = set(starts)
        stack = list(starts)

        while stack:
            row, col = stack.pop()
            for next_row, next_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and (next_row, next_col) not in seen
                    and heights[next_row][next_col] >= heights[row][col]
                ):
                    seen.add((next_row, next_col))
                    stack.append((next_row, next_col))

        return seen

    pacific = [(row, 0) for row in range(rows)] + [(0, col) for col in range(cols)]
    atlantic = [(row, cols - 1) for row in range(rows)] + [(rows - 1, col) for col in range(cols)]
    return sorted(reachable(pacific) & reachable(atlantic))


assert pacific_atlantic([
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]) == [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]
assert pacific_atlantic([[1]]) == [(0, 0)]
