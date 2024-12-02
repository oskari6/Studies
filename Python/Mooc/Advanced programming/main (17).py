import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot_img = pygame.image.load("robot.png")
rock_img = pygame.image.load("rock.png")

class Rock:
    def __init__(self, image):
        self.image = image
        self.x = randint(0, window.get_width() - image.get_width())
        self.y = 0 - image.get_height()
        self.velocity = randint(1, 3)

    def movement(self):
        self.y += self.velocity
        if self.y >= window.get_height():
            reset_game()
        elif abs(self.x - robot.x) <= self.image.get_width() and abs(self.y - robot.y) <= self.image.get_height():
            robot.points += 1
            rocks.remove(self)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Robot:
    def __init__(self, image):
        self.image = image
        self.x = window.get_width() // 2
        self.y = window.get_height() - image.get_height()
        self.velocity = 5
        self.points = 0

def reset_game():
    global rocks, robot
    rocks = []
    robot = Robot(robot_img)

reset_game()

to_left = False
to_right = False
spawn_delay = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if to_left:
        robot.x -= robot.velocity
    elif to_right:
        robot.x += robot.velocity

    if spawn_delay == 0:
        rocks.append(Rock(rock_img))
        spawn_delay = 60
    else:
        spawn_delay -= 1

    for rock in rocks:
        rock.movement() 

    window.fill((0, 0, 0))
    for rock in rocks:
        rock.draw(window)

    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {robot.points}", True, (255, 0, 0))

    window.blit(robot.image, (robot.x, robot.y))
    window.blit(text, (window.get_width() - 100, 0))
    pygame.display.flip()

    clock.tick(60)