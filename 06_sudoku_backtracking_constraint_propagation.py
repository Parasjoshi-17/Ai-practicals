
"""Sudoku Solver using Backtracking."""

grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Check whether number can be placed
def is_safe(row, col, num):

    # Check row
    for c in range(9):
        if grid[row][c] == num:
            return False

    # Check column
    for r in range(9):
        if grid[r][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True
# Solve Sudoku using backtracking
def solve():

    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                for num in range(1, 10):

                    if is_safe(row, col, num):
                        grid[row][col] = num

                        if solve():
                            return True

                        grid[row][col] = 0

                return False

    return True

# Print solution
if solve():
    for row in grid:
        print(row)
else:
    print("No solution exists.")
