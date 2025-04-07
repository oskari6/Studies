class AllPaths:
    def __init__(self, n):
        self.n = n
        self.graph = {i:[] for i in range(1,n+1)}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def topological_sort(self):
        visited = set()
        order = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in self.graph[node]:
                dfs(neighbor)
            order.append(node)

        for node in range(1, self.n+1):
            dfs(node)

        order.reverse()
        return order
    
    def count(self):
        topological_order = self.topological_sort()
        dp = {node: 0 for node in range(1, self.n +1)}
        total_paths = 0

        for node in reversed(topological_order):
            for neighbor in self.graph[node]:
                dp[node] += dp[neighbor]+1
            total_paths += dp[node]
        return total_paths

if __name__ == "__main__":
    counter = AllPaths(4)

    counter.add_edge(1, 2)
    counter.add_edge(1, 3)
    counter.add_edge(2, 4)
    counter.add_edge(3, 4)

    print(counter.count()) # 10

    counter.add_edge(2, 3)

    print(counter.count()) # 14