import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()
direction = "r"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    

    if direction == "r":
        x += velocity
        if x+robot.get_width() >= 640:
            direction = "d"

    elif direction == "d":
        y += velocity
        if y+robot.get_height() >= 480:
            direction = "l"

    elif direction == "l":
        x -= velocity
        if x <= 0:
            direction = "u"

    elif direction == "u":
        y -= velocity
        if y <= 0:
            direction = "r"

    clock.tick(60)