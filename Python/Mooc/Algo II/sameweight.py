class SameWeight:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add_edge(self, a, b, x):
        self.edges.append((x, a, b))

    def check(self):
        parent = [i for i in range(self.n + 1)]
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        self.edges.sort()
        i = 0
        while i < len(self.edges):
            same_weight_edges = []
            w = self.edges[i][0]

            while i < len(self.edges) and self.edges[i][0] == w:
                same_weight_edges.append(self.edges[i])
                i += 1

            temp_parent = parent[:]
            def temp_find(x):
                while temp_parent[x] != x:
                    temp_parent[x] = temp_parent[temp_parent[x]]
                    x = temp_parent[x]
                return x
            for _, a, b in same_weight_edges:
                if temp_find(a) == temp_find(b):
                    return False 

            for _, a, b in same_weight_edges:
                if find(a) != find(b):
                    union(a, b)

        root = find(1)
        for i in range(2, self.n + 1):
            if find(i) != root:
                return True
        return True

if __name__ == "__main__":
    same_weight = SameWeight(4)

    same_weight.add_edge(1, 2, 2)
    same_weight.add_edge(1, 3, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(1, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(3, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(2, 4, 1)
    print(same_weight.check()) # False