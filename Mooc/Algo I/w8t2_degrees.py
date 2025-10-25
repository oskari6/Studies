def find_degrees(nodes, edges):
    counts = {node:0 for node in nodes}
    for a,b in edges:
        counts[a] += 1
        counts[b] += 1
    return sorted([counts[node] for node in nodes])

    print(len(counts))
if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(find_degrees(nodes, edges)) # [2, 2, 3, 3, 4]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_degrees(nodes, edges)) # [0, 0, 0, 0, 0]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_degrees(nodes, edges)) # [1, 1, 1, 1, 4]