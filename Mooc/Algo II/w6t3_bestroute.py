import heapq

class BestRoute:
    def __init__(self, n):
        self.n = n
        self.graph = {node: [] for node in range(1,n+1)}

    def add_road(self, a, b, x):
        self.graph[a].append((b,x))
        self.graph[b].append((a,x))

    def find_route(self, a, b):
        distances = {node:float("inf") for node in self.graph}
        distances[a] = 0
        queue = [(0,a)]

        while queue:
            current_dist, node = heapq.heappop(queue)
            if current_dist > distances[node]:
                continue
            for neighbor, weight in self.graph[node]:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))
                    
        return distances[b] if distances[b] != float("inf") else -1

if __name__ == "__main__":
    routes = BestRoute(3)

    routes.add_road(1, 2, 2)
    print(routes.find_route(1, 3)) # -1

    routes.add_road(3, 1, 5)
    print(routes.find_route(1, 3)) # 5

    routes.add_road(2, 3, 1)
    print(routes.find_route(1, 3)) # 3