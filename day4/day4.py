directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]


def get_surrounding_rolls_count(grid, row, col):
    count = 0

    for direction in directions:
        ncol = col + direction[0]
        nrow = row + direction[1]

        if is_within_bounds(grid, nrow, ncol) and grid[nrow][ncol] == "@":
            count += 1

    return count


def is_within_bounds(grid, row, col):
    return col >= 0 and col < len(grid[0]) and row >= 0 and row < len(grid)


grid = [list(line.strip()) for line in open("input.txt", "r").readlines()]

total_rolls = 0

while True:
    rolls = []

    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "@" and get_surrounding_rolls_count(grid, row, col) < 4:
                rolls.append((row, col))

    if len(rolls) == 0:
        break

    total_rolls += len(rolls)

    for row, col in rolls:
        grid[row][col] = "x"


print(f"Forklight accessible rolls: {total_rolls}")
