class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.max_depth = max(self.max_depth, 0)
            return
        node = self.root
        height = 0
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    self.max_depth = max(self.max_depth, height+1)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    self.max_depth = max(self.max_depth, height+1)
                    return
                node = node.right
            height += 1

    def height(self):
        return self.max_depth

if __name__ == "__main__":
    numbers = TreeSet()
    print(numbers.height()) # -1
    numbers.add(2)
    print(numbers.height()) # 0
    numbers.add(1)
    print(numbers.height()) # 1
    numbers.add(3)
    print(numbers.height()) # 1
    numbers.add(4)
    print(numbers.height()) # 2