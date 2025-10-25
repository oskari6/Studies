import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = window.get_height()-robot.get_height()

to_right = False
to_left = False
to_top = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_top = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_top = False
            if event.key == pygame.K_DOWN:
                to_down = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        if x + robot.get_width() < window.get_width():
            x += 2
    if to_left:
        if x  > 0:
            x -= 2
    if to_top:
        if y > 0:
            y -= 2
    if to_down:
        if y + robot.get_height() < window.get_height():
            y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)