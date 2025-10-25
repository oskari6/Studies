class WallGrid:
    def __init__(self, n):
        self.n = n
        self.grid = [[False] * n for _ in range(n)]
        self.parent = {}
        self.count = 0

    def position_id(self, x , y):
        return x * self.n + y
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        new_a = self.find(a)
        new_b = self.find(b)
        if new_a != new_b:
            self.parent[new_b] = new_a
            self.count -= 1

    def create_floor(self, x, y):
        x -= 1
        y -= 1
        if self.grid[x][y]: return

        self.grid[x][y] = True
        id1 = self.position_id(x,y)
        self.parent[id1] = id1
        self.count += 1

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_x,new_y = x +dx, y+dy
            if 0 <= new_x < self.n and 0 <= new_y < self.n:
                if self.grid[new_x][new_y]:
                    id2 = self.position_id(new_x, new_y)
                    if id2 in self.parent:
                        self.union(id1,id2)

    def count_rooms(self):
        return self.count

if __name__ == "__main__":
    wall_grid = WallGrid(5)

    print(wall_grid.count_rooms()) # 0

    wall_grid.create_floor(2, 2)
    wall_grid.create_floor(4, 2)
    print(wall_grid.count_rooms()) # 2

    wall_grid.create_floor(3, 2)
    print(wall_grid.count_rooms()) # 1

    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(4, 4)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 3)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 4)
    print(wall_grid.count_rooms()) # 1