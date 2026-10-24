def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def explore(row, col):
        if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != "1":
            return
        grid[row][col] = "0"
        explore(row + 1, col)
        explore(row - 1, col)
        explore(row, col + 1)
        explore(row, col - 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                islands += 1
                explore(row, col)

    return islands


assert count_islands([
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
]) == 2
assert count_islands([]) == 0
