import pygame
import math
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

vx = randint(5, 10)
vy = randint(5, 10)

x = randint(0, window.get_width() - ball.get_width())
y = randint(0, window.get_height() - ball.get_height())

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x += vx
    y += vy
    
    if x + ball.get_width() > window.get_width() or x < 0:
        vx *= -1
    if y + ball.get_height() > window.get_height() or y < 0:
        vy *= -1

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    clock.tick(60)