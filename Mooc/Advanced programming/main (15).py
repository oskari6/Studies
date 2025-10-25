import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 100
robot_y = 100
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0]-robot.get_width()/2
            target_y = event.pos[1]-robot.get_height()/2
            if target_x - robot_x <= robot.get_width()/2:
                if target_y - robot_y <= robot.get_height()/2:
                    robot_x = randint(50, 600)
                    robot_y = randint(50, 400)

        if event.type == pygame.QUIT:
            exit(0)
    
    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)