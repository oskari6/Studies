
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
for i in range(1000):
    rand1 = randint(0, window.get_width()- robot.get_width())
    rand2 = randint(0, window.get_height() - robot.get_height())
    window.blit(robot, (rand1, rand2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()