import pygame
import math
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_img = pygame.image.load("robot.png")

class Robot:
    def __init__(self, image):
        self.image = image
        self.x = randint(0, window.get_width() - image.get_width())
        self.y = 0 - image.get_height()
        self.velocity = 2
        self.direction = "d"
        self.delay = randint(1, 5) * 60

    def movement(self):
        if self.delay > 0:
            self.delay -= 1
            return
        
        if self.direction == "d":
            self.y += self.velocity
            if self.y + self.image.get_height() >= window.get_height():
                turn = randint(0, 2)
                if turn == 0:
                    self.direction = "l"
                else:
                    self.direction = "r"

        elif self.direction == "l":
            self.x -= self.velocity

        elif self.direction == "r":
            self.x += self.velocity

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

robots = [Robot(robot_img) for _ in range(20)]
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for robot in robots:
        #different spawn times
        robot.movement()        

    window.fill((0, 0, 0))
    for robot in robots:
        robot.draw(window)
    pygame.display.flip()

    clock.tick(60)