class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        node = self.root
        while True:
            if node.value == value:
                node.count += 1
                return
            elif value < node.value:
                if not node.left:
                    node.left =  Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def __contains__(self, value):
        if not self.root:
            return False

        node = self.root
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
                node = node.right

        return False

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def count(self, value):
        node = self.root
        while node:
            if node.value == value:
                return node.count
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return 0

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.extend([node.value] * node.count)
        self.traverse(node.right, items)

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(4)
    numbers.add(1)
    numbers.add(2)
    numbers.add(1)

    print(numbers) # [1, 1, 2, 4]

    print(1 in numbers) # True
    print(2 in numbers) # True
    print(3 in numbers) # False
    print(4 in numbers) # True

    print(numbers.count(1)) # 2
    print(numbers.count(2)) # 1
    print(numbers.count(3)) # 0
    print(numbers.count(4)) # 1