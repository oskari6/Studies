class GraphGame:
    def __init__(self, n):
        self.n = n
        self.graph = {i: [] for i in range(1, n + 1)}

    def add_link(self, a, b):
        self.graph[a].append(b)

    def winning(self, x):
        statuses = {}

        def dfs(node):
            if node in statuses: return statuses[node]

            if not self.graph[node]:
                statuses[node] = False
                return False

            for neighbor in self.graph[node]:
                if not dfs(neighbor):
                    statuses[node] = True
                    return True

            statuses[node] = False
            return False

        return dfs(x)
    
if __name__ == "__main__":
    game = GraphGame(6)

    game.add_link(3, 4)
    game.add_link(1, 4)
    game.add_link(4, 5)

    print(game.winning(3)) # False
    print(game.winning(1)) # False

    game.add_link(3, 1)
    game.add_link(4, 6)
    game.add_link(6, 5)

    print(game.winning(3)) # True
    print(game.winning(1)) # False
    print(game.winning(2)) # False