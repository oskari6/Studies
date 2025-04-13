class Ball:
    def __init__(self, n):
        self.n = n
        self.size = 2 * n + 2
        self.source = 0
        self.sink = 2 * n +1
        self.graph = {}
        for i in range(self.size):
            for j in range(self.size):
                self.graph[(i,j)] = 0

        for i in range(1, n+1):
            self.graph[self.source, i] = 1

        for i in range(n + 1, 2 * n +1):
            self.graph[(i, self.sink)] = 1
            
    def add_pair(self, a, b):
        self.graph[(a,b + self.n)] += 1

    def dfs(self, u, sink, flow):
        if u in self.seen: return 0
        self.seen.add(u)
        if u == sink: return flow

        for v in range(self.size):
            if self.residual.get((u,v), 0) > 0:
                bottleneck = self.dfs(v, sink, min(flow, self.residual[(u,v)]))
                if bottleneck > 0:
                    self.residual[(u,v)] -= bottleneck
                    self.residual[(v,u)] += bottleneck
                    return bottleneck
        return 0
    
    def max_pairs(self):
        self.residual = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            flow = self.dfs(self.source, self.sink, float("inf"))
            if flow == 0: break
            total += flow
        return total
    
if __name__ == "__main__":
    ball = Ball(4)

    print(ball.max_pairs()) # 0

    ball.add_pair(1, 2)
    print(ball.max_pairs()) # 1

    ball.add_pair(1, 3)
    ball.add_pair(3, 2)
    print(ball.max_pairs()) # 2

    ball.add_pair(2, 1)
    print(ball.max_pairs()) # 3