class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_subtrees(node):
    if not node.children: return [1]
    sizes = []
    size = 1
    for child in node.children:
        child_sizes = count_subtrees(child)
        sizes.extend(child_sizes)
        size += len(child_sizes)
    sizes.append(size)
    return sorted(sizes)

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_subtrees(tree1)) # [1, 1, 1, 1, 2, 3, 7]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_subtrees(tree2)) # [1, 2, 3, 4]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_subtrees(tree3)) # [1, 1, 1, 4]