import pygame
import sys
import time
import random
from network import Network
from food import Food
from game import Game

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

difficulty = 5
score = 0

f = Food()

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
if check_errors[1] > 0:
    print(
        f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)


def redrawWindow(win, player1, player2):
    win.fill(black)
    player1.draw(game_window)
    player2.draw(game_window)

    f.spawnFood(game_window)

    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()

    while run:
        fps_controller.tick(difficulty)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()

        if p.snake_pos[0] == f.food_pos[0] and p.snake_pos[1] == f.food_pos[1]:
            p.eaten_food = True
            print(f.food_spawn)
            f.food_spawn = False

            # Touching the snake body
            for block in p2.snake_body[1:]:
                if p.snake_pos[0] == block[0] and p.snake_pos[1] == block[1]:
                    game_over()

        if p.death():
            game_over()

        redrawWindow(game_window, p, p2)


main()
