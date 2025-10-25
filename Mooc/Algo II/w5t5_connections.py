class Connections:
    def __init__(self, n):
        self.node = n
        self.graph = {i:[] for i in range(1, n+1)}

    def add_link(self, a, b):
        self.graph[a].append(b)

    def dfs(self, start, graph):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])
        return visited
    
    def check_network(self):
        visited_from_first = self.dfs(1, self.graph)
        if len(visited_from_first) < self.node:
            return False
        
        reversed_graph = {i: [] for i in range(1, self.node+1)}
        for source in self.graph:
            for destination in self.graph[source]:
                reversed_graph[destination].append(source)

        visited_reversed = self.dfs(1, reversed_graph)
        if len(visited_reversed) < self.node:
            return False
        
        return True

if __name__ == "__main__":
    connections = Connections(5)

    connections.add_link(1, 2)
    connections.add_link(2, 3)
    connections.add_link(1, 3)
    connections.add_link(4, 5)

    print(connections.check_network()) # False

    connections.add_link(3, 5)
    connections.add_link(1, 4)

    print(connections.check_network()) # False

    connections.add_link(5, 1)

    print(connections.check_network()) # True