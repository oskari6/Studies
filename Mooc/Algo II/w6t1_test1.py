import random
import time

class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))
        
    def find_distances(self, start_node):
        distances = {node: float("inf") for node in self.nodes}
        distances[start_node] = 0
        
        for _ in range(len(self.nodes) -1):
            for node_a, node_b, weight in self.edges:
                if distances[node_a] + weight  < distances[node_b]:
                    distances[node_b] = distances[node_a] +weight
                    
        return distances
 
if __name__ == "__main__":
    nodes = list(range(1,5001))
    bf = BellmanFord(nodes)

    for a in nodes:
        for diff in range(1,10):
            b = a +diff
            if b <= 5000:
                weight = random.randint(1, 1000)
                bf.add_edge(a,b,weight)

    random.shuffle(bf.edges)

    start_time = time.perf_counter()
    distances = bf.find_distances(1)
    end_time = time.perf_counter()
    print(f"1. time: {end_time - start_time:.6f} s")
