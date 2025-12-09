def block_correct(sudoku, row_no, col_no):
    seen = []
    for row in range(row_no, row_no + 3):
        for col in range(col_no, col_no + 3):
            if sudoku[row][col] == 0:
                continue
            if sudoku[row][col] not in seen:
                seen.append(sudoku[row][col])
            else:
                return False
    return True

def row_correct(sudoku, row_no):
    seen = []
    for col in range(9):
        if sudoku[row_no][col] == 0:
            continue
        if sudoku[row_no][col] not in seen:
            seen.append(sudoku[row_no][col])
        else:
            return False
    return True

def column_correct(sudoku, col_no):
    seen = []
    for row in range(9):
        if sudoku[row][col_no] == 0:
            continue
        if sudoku[row][col_no] not in seen:
            seen.append(sudoku[row][col_no])
        else:
            return False
    return True

def sudoku_grid_correct(sudoku):
    for row in range(9):
        if not row_correct(sudoku, row):
            return False
        
    for col in range(9):
        if not column_correct(sudoku, col):
            return False
        
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_correct(sudoku, row, col):
                return False
    return True
            

if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_grid_correct(sudoku))