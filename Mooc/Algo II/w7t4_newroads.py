class UnionFind:
    def __init__(self, nodes):
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]

class NewRoads:
    def __init__(self, n):
        self.roads = list(range(1,n+1))
        self.edges = []

    def add_road(self, a, b, x):
        self.edges.append((a, b, x))

    def min_cost(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.roads)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            a, b, x = edge
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                edges_count += 1
                tree_weight += x

        if edges_count != len(self.roads) -1:
            return -1
        return tree_weight

if __name__ == "__main__":
    new_roads = NewRoads(4)

    new_roads.add_road(1, 2, 2)
    new_roads.add_road(1, 3, 5)
    print(new_roads.min_cost()) # -1

    new_roads.add_road(3, 4, 4)
    print(new_roads.min_cost()) # 11

    new_roads.add_road(2, 3, 1)
    print(new_roads.min_cost()) # 7