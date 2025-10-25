class AllPaths:
    def __init__(self, n):
        self.n = n
        self.graph = {i:[] for i in range(1,n+1)}

    def add_edge(self, a,b):
        self.graph[a].append(b)

    def count(self):
        visited = set()
        order = []

        def dfs(node):
            if node in visited: return
            visited.add(node)
            for neighbor in self.graph[node]:
                dfs(neighbor)
            order.append(node)
        
        for node in range(1,self.n+1):
            dfs(node)

        order.reverse()

        dp = [0] * (self.n +1)
        for node in reversed(order):
            if dp[node] == 0:
                dp[node] = 1
            for neighbor in self.graph[node]:
                dp[node] += dp[neighbor]

        return sum(dp[1:])

if __name__ == "__main__":
    counter = AllPaths(4)

    counter.add_edge(1, 2)
    counter.add_edge(1, 3)
    counter.add_edge(2, 4)
    counter.add_edge(3, 4)

    print(counter.count()) # 10

    counter.add_edge(2, 3)

    print(counter.count()) # 14