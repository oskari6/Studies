def count_pairs(grid):
    n = 8
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1,2), (1,-2),(1,2),(2,-1), (2,1)]

    def convert_position(i,j):
        return i * n + j
    
    graph = {}
    left_nodes = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "*":
                u = convert_position(i,j)
                graph[u] = []
                if (i+j) % 2 == 0:
                    left_nodes.append(u)
                    for dx,dy in moves:
                        new_i,new_j = i + dx, j + dy
                        if  0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == "*":
                            v = convert_position(new_i,new_j)
                            graph[u].append(v)

    match = {}
    def hopcroft_karp(u,visited):
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                if v not in match or hopcroft_karp(match[v], visited):
                    match[v] = u
                    return True
        return False
    
    result = 0
    for u in left_nodes:
        visited = set()
        if hopcroft_karp(u, visited):
            result += 1
    return result

if __name__ == "__main__":
    grid = ["*.......",
            "..*...*.",
            "........",
            ".*......",
            "...*....",
            ".......*",
            "........",
            "......*."]

    print(count_pairs(grid)) # 3

    grid = ["*.***.**",
            "*******.",
            "*.**.**.",
            "***.****",
            "..****.*",
            "********",
            "*.******",
            "***.**.*"]

    print(count_pairs(grid)) # 25