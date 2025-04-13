# slightly modified version of the class in the course material
class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i,j)] = 0

    def add_edge(self, a, b, capacity):
        self.graph[(a,b)] += capacity
    
    def add_flow(self, node, sink, flow):
        if node in self.seen: return 0

        self.seen.add(node)
        if node == sink: return flow

        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0
    
    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        self.path_count = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
            self.path_count += 1
        return total

def create_edges(x):
    edges = []
    intermediates = list(range(2, 100)) 

    if x <= 98:
        for i in range(x):
            mid = intermediates[i]
            edges.append((1, mid, 1))
            edges.append((mid, 100, 1))
    else:
        # 2 jumps 1-2-100
        for i in range(98):
            mid = intermediates[i]
            edges.append((1, mid, 1))
            edges.append((mid, 100, 1))

        # 3 jumps 1-2-3-100
        if x == 99:
            edges.append((1, 2, 1))
            edges.append((2, 3, 1))
            edges.append((3, 100, 1))
        elif x == 100:
            edges.append((1, 2, 1))
            edges.append((2, 3, 1))
            edges.append((3, 100, 1))

            edges.append((1, 4, 1))
            edges.append((4, 5, 1))
            edges.append((5, 100, 1))

    return edges

if __name__ == "__main__":
    edges = create_edges(42)

    maximum_flow = MaximumFlow(range(1, 100 + 1))

    for edge in edges:
        maximum_flow.add_edge(edge[0], edge[1], edge[2])

    maximum_flow.construct(1, 100)
    print(maximum_flow.path_count) # 42