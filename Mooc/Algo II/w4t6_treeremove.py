class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right
    
    def remove(self, value):
        def remove_element(node, value):
            if not node: return None
            if value < node.value:
                node.left = remove_element(node.left, value)
            elif value > node.value:
                node.right = remove_element(node.right, value)
            else:
                if not node.left and not node.right:
                    return None
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                child = node.right
                while child.left:
                    child = child.left
                node.value = child.value
                node.right = remove_element(node.right, child.value)
            return node
        self.root = remove_element(self.root, value)

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(3)
    numbers.add(2)
    numbers.add(5)
    numbers.add(7)
    print(numbers) # [2, 3, 5, 7]
    
    numbers.remove(3)
    print(numbers) # [2, 5, 7]

    numbers.remove(7)
    print(numbers) # [2, 5]

    numbers.remove(2)
    print(numbers) # [5]

    numbers.remove(5)
    print(numbers) # []