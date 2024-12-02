import pygame
from random import randint
import time
import random

class Sokoban:
    def __init__(self):
        self.highscore = 0
        pygame.init()

        self.game_font = pygame.font.SysFont("Arial", 24)

        self.load_images()
        self.new_game()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()

        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))

        pygame.display.set_caption("Ghost game")

        self.enemy_move_time = time.time()#enemy speed
        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["rock", "sand", "coin", "ghost", "robot"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        self.map = [    #1 wall, 0 floor, 2 coin
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 2, 0, 1, 0, 0, 0, 2, 0, 0, 4, 1, 0, 2, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
        self.coins = 0
        self.game_over = False #flag
        self.enemies = [(12, 1, (0, 1)), (10, 8, (1, 0)), (12, 15, (0, -1)), (1, 1, (0, 1)), (1, 15, (0, -1)), (6, 4, (0, 1)), (6, 12, (0, -1))]#enemy spawn points
        self.original_squares = {}#to for enemies going over coins

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

                if self.game_over:
                    if event.key == pygame.K_F2:
                        self.new_game()
                        self.game_over = False
                    continue

                if event.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)
        
        #enemy speed, movement
        current_time = time.time()
        if current_time - self.enemy_move_time >= 0.5:
            self.enemy_move()
            self.enemy_move_time = current_time

    def draw_window(self):#ui
        self.window.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                if square < len(self.images):
                    self.window.blit(self.images[square], (x * self.scale, y * self.scale))
                else:
                    print(f"Incorrect position at position {y}, {x}")

        game_text = self.game_font.render(f"Coins: {self.coins}", True, (255, 0, 0))
        self.window.blit(game_text, (25, self.height * self.scale + 10))

        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, self.height * self.scale + 10))

        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 10))

        game_text = self.game_font.render(f"Highscore {self.highscore}", True, (255, 0, 0))
        self.window.blit(game_text, (600, self.height * self.scale + 10))

        if self.game_over:
            self.game_over_screen()

        pygame.display.flip()

    def game_over_screen(self):
        self.window.fill((0, 0, 0))
        game_text = self.game_font.render(f"Game over! Coins: {self.coins} Press F2 to restart", True, (255, 0, 0))
        game_text_x = self.scale * self.width / 2 - game_text.get_width() / 2
        game_text_y = self.scale * self.height / 2 - game_text.get_height() / 2
        self.window.blit(game_text, (game_text_x, game_text_y))
        pygame.display.flip()
        
    def enemy_move(self):
        new_enemies = []#checking collision
        ghost_positions = set((y, x) for y, x, _ in self.enemies)#checking collision

        for i, (old_y, old_x, direction) in enumerate(self.enemies):#moving direction
            move_y, move_x = direction
            new_y = old_y + move_y
            new_x = old_x + move_x

            # check bounds, a wall, or another ghost
            if not (0 <= new_y < self.height and 0 <= new_x < self.width) or self.map[new_y][new_x] in [1, 3] or (new_y, new_x) in ghost_positions:
                # directions
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                random.shuffle(directions)  #random movement
                found_direction = False
                for new_direction in directions:#get a valid direction
                    if new_direction == (-move_y, -move_x):
                        continue
                    move_y, move_x = new_direction
                    new_y = old_y + move_y
                    new_x = old_x + move_x
                    #found it
                    if 0 <= new_y < self.height and 0 <= new_x < self.width and self.map[new_y][new_x] not in [1, 3] and (new_y, new_x) not in ghost_positions:
                        found_direction = True
                        break
                #didnt find it, make new enemy
                if not found_direction:
                    new_enemies.append((old_y, old_x, direction))
                    continue

            if self.map[new_y][new_x] == 4:#kills robot
                self.game_over = True

            if (old_y, old_x) in self.original_squares:#after exiting coin square
                self.map[old_y][old_x] = self.original_squares.pop((old_y, old_x))
            else:
                self.map[old_y][old_x] = 0 #floor

            if self.map[new_y][new_x] == 2:
                self.original_squares[(new_y, new_x)] = 2 #save coin square image

            #enemy movement
            self.map[new_y][new_x] = 3
            new_enemies.append((new_y, new_x, (move_y, move_x)))
            ghost_positions.add((new_y, new_x))
            ghost_positions.remove((old_y, old_x))

        self.enemies = new_enemies
         
    def move(self, move_y, move_x):
        pos = self.find_robot()
        if pos is None: #for errors
            return
        robot_old_y, robot_old_x = self.find_robot()
        robot_new_y = robot_old_y + move_y
        robot_new_x = robot_old_x + move_x

        if self.map[robot_new_y][robot_new_x] == 1:#wall
            return

        if self.map[robot_new_y][robot_new_x] == 2:#coin
            self.coins += 1
            if self.coins > self.highscore:#highscore
                self.highscore = self.coins
            self.map[robot_new_y][robot_new_x] -= 2 #floor
            while True:
                x, y = randint(0, 14), randint(0, 16)#coin spawn randomly
                if self.map[x][y] == 0:
                    self.map[x][y] += 2
                    break

        if self.map[robot_new_y][robot_new_x] == 3:#ghost
            self.game_over = True

        self.map[robot_old_y][robot_old_x] -= 4 #movement
        self.map[robot_new_y][robot_new_x] += 4

    def find_robot(self): #find on map
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return (y, x)

    def find_enemy(self): #find on map
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [3, 6]:
                    return (y, x)

if __name__ == "__main__":
    Sokoban()