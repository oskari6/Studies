def count_rooms(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r,c):
        stack = [(r,c)]
        while stack:
            x,y = stack.pop()
            if (x,y) in visited: continue
            visited.add((x,y))

            for dx,dy in [(-1,0), (0,-1), (0,1),(1,0)]:
                new_x,new_y = x+dx, y+dy
                if (new_x,new_y) not in visited and 0 <= new_x < rows and 0 <= new_y <  cols and grid[new_x][new_y] == ".":
                    stack.append((new_x, new_y))
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "." and (row, col) not in visited:
                dfs(row, col)
                count += 1
    return count

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2