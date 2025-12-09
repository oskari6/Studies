class Download:
    def __init__(self, n):
     self.nodes = list(range(1,n+1))
     self.graph = {}
     for i in self.nodes:
        for j in self.nodes:
           self.graph[(i,j)] = 0

    def add_link(self, a, b, x):
        self.graph[(a,b)] += x

    def dfs(self, u, sink, flow):
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
    
    def max_data(self, a, b):
        self.residual = self.graph.copy()
        total_flow = 0
        while True:
           self.seen = set()
           flow = self.dfs(a, b, float("inf"))
           if flow == 0: break
           total_flow += flow

        return total_flow

if __name__ == "__main__":
    download = Download(4)

    print(download.max_data(1, 4)) # 0

    download.add_link(1, 2, 5)
    download.add_link(2, 4, 6)
    download.add_link(1, 4, 2)
    print(download.max_data(1, 4)) # 7

    download.add_link(1, 3, 4)
    download.add_link(3, 2, 2)
    print(download.max_data(1, 4)) # 8