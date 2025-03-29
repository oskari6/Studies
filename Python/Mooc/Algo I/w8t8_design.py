def create_grid(steps):
    if steps > 41: return None
    labyrinth = [
        list("##########"),
        list("#A-------#"),
        list("#--------#"),
        list("#--------#"),
        list("#--------#"),
        list("#--------#"),
        list("#--------#"),
        list("#--------#"),
        list("#--------#"),
        list("##########")
    ]
    start = (1,2)
    directions = [(0,1), (1,0), (0,-1),(-1,0)]
    direction = 0
    wall_start = (2,1)
    turn = False

    for step in range(steps):
        dx, dy = directions[direction]
        new_x, new_y = start[0] + dx, start[1] + dy
        if turn: turn = False
        else:
            wx, wy = directions[direction]
            wall_x, wall_y = wall_start[0] + wx, wall_start[1] + wy
        print(wall_start)
        if labyrinth[new_x][new_y] != "#":
            if step == steps-1: labyrinth[start[0]][start[1]] = "B"
            else: labyrinth[start[0]][start[1]] = "."
            start = (new_x, new_y)
            if labyrinth[wall_x][wall_y] == "-":
                labyrinth[wall_start[0]][wall_start[1]] = "#"
                wall_start = (wall_x, wall_y)
        else:
            turn = True
            direction = (direction + 1) % 4
            dx, dy = directions[direction]
            new_x, new_y = start[0] + dx, start[1] + dy
            if step == steps-1: labyrinth[start[0]][start[1]] = "B"
            else: labyrinth[start[0]][start[1]] = "."
            start = (new_x, new_y)

    temp = ["".join(row) for row in labyrinth]
    print("\n".join(temp))
    for row in range(len(labyrinth)):
        for col in range(len(labyrinth[0])):
            if labyrinth[row][col] == "-": labyrinth[row][col] = "#"

    return ["".join(row) for row in labyrinth]

if __name__ == "__main__":
    grid = create_grid(38)
    print("\n".join(grid))