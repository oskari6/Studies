class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_path(node, a, b):
    a_path = find_root(node, a)
    b_path = find_root(node, b)

    if a_path is None or b_path is None: return None
    if a_path == b_path: return [a_path[-1]]

    merged = list(reversed(a_path)) + b_path
    
    seen = set()
    result = []
    
    for val in merged:
        if val in seen:
            while result and result[-1] != val: result.pop()
            result.pop()
        result.append(val)
        seen.add(val)

    return result

def find_root(node, target):
    if node is None: return None
    if node.value == target: return [node.value]
    for child in node.children:
        path = find_root(child, target)
        if path: return [node.value] + path
    return None

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2)) # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7)) # [1, 4, 7]
    print(find_path(tree1, 5, 5)) # [5]
    print(find_path(tree1, 7, 3)) # [7, 4, 3]
    print(find_path(tree1, 4, 8)) # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4)) # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1)) # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3)) # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3)) # [2, 1, 3]
    print(find_path(tree3, 1, 2)) # [1, 2]
    print(find_path(tree3, 5, 5)) # None