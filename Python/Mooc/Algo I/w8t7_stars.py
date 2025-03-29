def count_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    unique = set()
    patterns = []
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
        ]

    def dfs(r, c, pattern):
        stack = [(r, c)]
        visited.add((r, c))
        while stack:
            x, y = stack.pop()
            pattern.append((x, y))
            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == "*":
                    visited.add((nx, ny))
                    stack.append((nx, ny))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "*" and (row, col) not in visited:
                pattern = []
                dfs(row, col, pattern)
                patterns.append(pattern)

    for pattern in patterns: unique.add(normalize(pattern))
    return len(unique)

def normalize(pattern):
    min_x = min(p[0] for p in pattern)
    min_y = min(p[1] for p in pattern)
    return tuple(sorted((x - min_x, y - min_y) for x, y in pattern))

if __name__ == "__main__":
    grid = ["..*..*..",
            "**.....*",
            ".....**.",
            "...*....",
            ".**....*"]
    print(count_patterns(grid)) # 2

    grid = ["....*..*",
            "*.......",
            "......*.",
            "..*.....",
            "......*."]
    print(count_patterns(grid)) # 1

    grid = ["***.*.**",
            ".*..*..*",
            ".*.***..",
            ".......*",
            "......**"]
    print(count_patterns(grid)) # 4

    grid = ["***.***.",
            "..*...*.",
            "**..**..",
            "..*...*.",
            "**..**.."]
    print(count_patterns(grid)) # 1
