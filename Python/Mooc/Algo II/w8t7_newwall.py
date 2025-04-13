from collections import deque
from itertools import combinations

def test_reach(grid):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    dq = deque([(0,0)])
    visited[0][0] = True

    while dq:
        x,y = dq.popleft()
        if x == n-1 and y == n-1:
            return True
        for dx,dy in [(0,1),(1,0)]:
            new_x,new_y = x+dx,y+dy
            if (0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == "."
                 and not visited[new_x][new_y]):
                visited[new_x][new_y] = True
                dq.append((new_x, new_y))
    return False

def min_changes(grid):
    n = len(grid)
    if not test_reach(grid):return 0

    floor_positions = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "." and (i,j) != (0,0) and (i,j) != (n-1,n-1):
                floor_positions.append((i,j))

    for k in range(1,len(floor_positions)+1):
        for cells in combinations(floor_positions, k):
            grid_copy = [list(row) for row in grid]
            for x,y in cells:
                grid_copy[x][y] ="#"
            if not test_reach(["".join(row) for row in grid_copy]):
                return k
    return 0

if __name__ == "__main__":
    grid = ["...#.",
            "...#.",
            "####.",
            ".....",
            "....."]

    print(min_changes(grid)) # 0

    grid = [".#...",
            "...#.",
            "...#.",
            ".###.",
            ".###."]

    print(min_changes(grid)) # 0

    grid = [".#...",
            "...#.",
            "...#.",
            ".###.",
            "....."]

    print(min_changes(grid)) # 1

    grid = [".....",
            ".###.",
            "...#.",
            "##.#.",
            "....."]

    print(min_changes(grid)) # 2