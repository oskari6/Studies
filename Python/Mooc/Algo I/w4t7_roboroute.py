def analyze_route(grid):
    row, col = find_initial(grid)
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
    dir_order = ["up", "right", "down", "left"]
    direction = "up"
    visited = set()
    squares = set()
    while True:
        state = (row, col, direction)
        square = (row, col)
        if state in visited:
            return (len(squares), False)
        
        visited.add(state)
        squares.add(square)

        dir_row, dir_col = directions[direction]
        next_row, next_col = row + dir_row, col + dir_col

        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            return (len(squares), True)
        if grid[next_row][next_col] == "#":
            direction = dir_order[(dir_order.index(direction)+1) % 4] # % 4 wrap around
        else:
            row, col = next_row, next_col
        
        

def find_initial(grid):
    for i, row in enumerate(grid):
        col_index = row.find("R")
        if col_index != -1:
            return (i, col_index)

if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)