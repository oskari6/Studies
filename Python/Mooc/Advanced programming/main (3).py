
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
for i in range(10):
    for j in range(10):
        window.blit(robot, (50+j*robot.get_width()/1.3 + i * 10, 100 + i * robot.get_height() / 5))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()