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

def add_number(sudoku : list, row_no: int, col_no : int, number:int):
    sudoku[row_no][col_no] = number

if __name__ == "__main__":
    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)