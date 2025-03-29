def find_components(nodes, edges):
    if not nodes: return []
    graph = {node:set() for node in nodes}
    visited = set()
    components = []
    for a,b in edges:
        graph[a].add(b)
        graph[b].add(a)

    def dfs(node, component):
        if node in visited: return
        visited.add(node)
        component.append(node)
        for neighbour in graph[node]: dfs(neighbour, component)

    for node in nodes:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(sorted(component))
    return sorted(components, key=lambda x:x[0])

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]