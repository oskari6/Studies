class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_tree(grid):
    positions = {}

    for r,row in enumerate(grid):
        for c,char in enumerate(row):
            if char.isdigit(): positions[(r,c)]=Node(int(char))
    
    for (r, c), node in positions.items():
        if r + 2 < len(grid):
            if c > 1 and grid[r + 1][c - 1] == "/":
                child_node = find_child(grid, r + 2, c - 2, 1, -1, positions)
                if child_node: node.children.append(child_node)
                    
            if grid[r + 1][c] == "|":
                child_node = find_child(grid, r + 1, c, 1, 0, positions) 
                if child_node: node.children.append(child_node)
                    
            if c + 2 < len(grid[0]) and grid[r + 1][c + 1] == "\\":
                child_node = find_child(grid, r + 2, c + 2, 1, 1, positions)
                if child_node: node.children.append(child_node)
                    
    child_nodes = {child for node in positions.values() for child in node.children}
    root = next(node for node in positions.values() if node not in child_nodes)

    return root

def find_child(grid, r, c, dr, dc, positions):
    while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        if (r,c) in positions: return positions[(r,c)]
        if grid[r][c] == "|": r += 1
        else:
            r += dr
            c += dc
    return None

if __name__ == "__main__":
    grid = ["...........",
            "...........",
            "......5....",
            "...../.\...",
            "....3...\..",
            "....|....1.",
            "....2......"]
    tree = find_tree(grid)
    print(tree)
    Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = ["....1.....",
            ".../.\....",
            "..2...\...",
            "..|....3..",
            "..7.../|\.",
            "./.\.4.|.6",
            "8...9..5.."]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])