# Write your solution here
def print_sudoku(sudoku : list):
    for row in sudoku:
        rotation = 0
        for cell in row:
            rotation += 1
            if cell == 0:
                print("_", end=" ")
            else:
                print(cell, end=" ")
            if rotation % 3 == 0 and rotation < 9:
                print(" ", end="")
        print()
        if (sudoku.index(row) + 1) % 3 == 0 and (sudoku.index(row) + 1) < 9:
            print()

def copy_and_add(sudoku : list, row_no: int, col_no : int, number:int):
    new = [row[:] for  row in sudoku]
    new[row_no][col_no] = number
    return new

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)