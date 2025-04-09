import heapq

def find_route(grid):
    rows = len(grid)
    cols = len(grid[0])
    end = None
    start = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "A":
                start = (r,c)
            elif grid[r][c] == "B":
                end = (r,c)

    heap = [(0,start[0], start[1])]
    visited = [[float("inf")] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while heap:
        walls_broken, r, c = heapq.heappop(heap)
        if (r,c) == end: return walls_broken

        for dr,dc in directions:
            nr,nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = grid[nr][nc]

                if cell == "#": continue

                cost = 1 if cell == "*" else 0
                new_walls_broken = walls_broken + cost

                if new_walls_broken < visited[nr][nc]:
                    visited[nr][nc] = new_walls_broken
                    heapq.heappush(heap, (new_walls_broken, nr, nc))

    return -1

if __name__ == "__main__":
    grid = ["########",
            "#*A*...#",
            "#.*****#",
            "#.**.**#",
            "#.*****#",
            "#..*.B.#",
            "########"]
    print(find_route(grid)) # 2