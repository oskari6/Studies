import heapq
import random
import time

class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node : []for node in nodes}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        
    def find_distances(self, start_node):
        distances = {node: float("inf") for node in self.nodes}
        distances[start_node] = 0
        heap = [(0,start_node)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances
 
if __name__ == "__main__":
    nodes = list(range(1,5001))
    dj = Dijkstra(nodes)

    for a in nodes:
        for diff in range(1,10):
            b = a +diff
            if b <= 5000:
                weight = random.randint(1, 1000)
                dj.add_edge(a,b,weight)

    start_time = time.perf_counter()
    distances = dj.find_distances(1)
    end_time = time.perf_counter()
    print(f"1. time: {end_time - start_time:.6f} s")
