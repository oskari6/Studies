class Planets:
    def __init__(self, n):
        self.n = n
        self.nodes = list(range(1,+n+1))
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_teleport(self, a, b):
        self.graph[(a,b)] += 1

    def dfs(self, u ,sink, flow):
        if u in self.seen: return 0
        self.seen.add(u)
        if u == sink: return flow

        for v in self.nodes:
            if self.residual[(u,v)] > 0:
                bottleneck = self.dfs(v, sink, min(flow, self.residual[(u,v)]))
                if bottleneck > 0:
                    self.residual[(u,v)] -= bottleneck
                    self.residual[(v,u)] += bottleneck
                    return bottleneck
        return 0
    
    def min_removals(self):
        source, sink = 1, self.n
        self.residual = self.graph.copy()
        total_flow = 0
        while True:
            self.seen = set()
            flow = self.dfs(source, sink, float("inf"))
            if flow == 0: break
            total_flow += flow
        return total_flow

if __name__ == "__main__":
    planets = Planets(5)

    print(planets.min_removals()) # 0

    planets.add_teleport(1, 2)
    planets.add_teleport(2, 5)
    print(planets.min_removals()) # 1

    planets.add_teleport(1, 5)
    print(planets.min_removals()) # 2