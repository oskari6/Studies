class MaxSet:
    def __init__(self, n):
        self.link = {node: None for node in range(1,n+1)}
        self.size = {node: 1 for node in range(1,n+1)}
        self.max_size = 1
        
    def find(self,x):
        if self.link[x] is None: return x
        self.link[x] = self.find(self.link[x])
        return self.link[x]
    
    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.size[a] > self.size[b]:
            a,b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]

        if self.size[b] > self.max_size:
            self.max_size = self.size[b]

    def get_max(self):
        return self.max_size

if __name__ == "__main__":
    max_set = MaxSet(5)
    print(max_set.get_max()) # 1

    max_set.merge(1, 2)
    max_set.merge(3, 4)
    max_set.merge(3, 5)
    print(max_set.get_max()) # 3

    max_set.merge(1, 5)
    print(max_set.get_max()) # 5

    max_set.merge(2, 3)
    print(max_set.get_max()) # 5