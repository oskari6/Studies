class Components:
    def __init__(self, n):
        self.link = {node: None for node in range(1,n+1)}
        self.size = {node: 1 for node in range(1,n+1)}

    def add_road(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.size[a] > self.size[b]:
            a,b = b,a
        self.link[a] = b
        self.size[b] += self.size[a]

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x
    
    def count(self):
        roots = set()
        for node in self.link:
            roots.add(self.find(node))
        return len(roots)

if __name__ == "__main__":
    components = Components(5)

    print(components.count()) # 5

    components.add_road(1, 2)
    components.add_road(1, 3)
    print(components.count()) # 3

    components.add_road(2, 3)
    print(components.count()) # 3

    components.add_road(4, 5)
    print(components.count()) # 2