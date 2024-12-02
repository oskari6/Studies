import pygame
import time
import math

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

hour_hand = 80
minute_hand = 150
second_hand = 170
center = (640 // 2, 480 // 2)

red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

def draw(hours, minutes, seconds):
    display.fill(black)

    pygame.draw.circle(display, red, center, 200)
    pygame.draw.circle(display, black, center, 195)
    pygame.draw.circle(display, red, center, 10)
    
    hour_angle = math.radians((hours % 12) * 30 - 90)
    hour_x = center[0] + hour_hand * math.cos(hour_angle)
    hour_y = center[1] + hour_hand * math.sin(hour_angle)
    pygame.draw.line(display, blue, center, (hour_x, hour_y), 3)

    minute_angle = math.radians((minutes % 60) * 6 - 90)
    minute_x = center[0] + minute_hand * math.cos(minute_angle)
    minute_y = center[1] + minute_hand * math.sin(minute_angle)
    pygame.draw.line(display, blue, center, (minute_x, minute_y), 2)

    second_angle = math.radians((seconds % 60) * 6 - 90)
    second_x = center[0] + second_hand * math.cos(second_angle)
    second_y = center[1] + second_hand * math.sin(second_angle)
    pygame.draw.line(display, blue, center, (second_x, second_y), 1)

    pygame.display.flip()

time_update = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    draw(hours, minutes, seconds)

    pygame.display.set_caption(time.strftime("%H:%M:%S"))
    clock.tick(1)