from collections import deque

def find_route(grid):
    rows,cols = len(grid),len(grid[0])
    start,end = None, None
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "A": start = row,col
            if grid[row][col] == "B": end = row,col
    
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, distance = queue.popleft()
        if (x, y) == end: return distance

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != "#" and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, distance + 1))

if __name__ == "__main__":
    grid = ["########",
            "#.#.B..#",
            "#A#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 6

    grid = ["########",
            "#B#...A#",
            "#.#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 9

    grid = ["########",
            "####..B#",
            "#.A#.#.#",
            "#..#...#",
            "########"]
    print(find_route(grid)) # None