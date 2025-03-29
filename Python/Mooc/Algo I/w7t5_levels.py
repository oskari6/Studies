from collections import deque

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_levels(node):
    #BFS
    if not node: return []
    levels = []
    queue = deque([(node, 0)])
    print(queue)
    while queue:
        current, level = queue.popleft()
        if level == len(levels): levels.append([])
        levels[level].append(current.value)
        levels[level] = sorted(levels[level])
        for child in current.children: queue.append((child, level+1)) 
    return levels

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2)) # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3)) # [[1], [2, 3, 4]]

    tree4 = Node(2, [Node(1)])
    print(find_levels(tree4))  # [[2], [1]]