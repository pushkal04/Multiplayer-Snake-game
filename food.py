import pygame
import sys
import time
import random

frame_size_x = 720
frame_size_y = 480

white = pygame.Color(255, 255, 255)


class Food:
    def __init__(self):
        self.food_pos = [random.randrange(1, (frame_size_x // 10))
                         * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        self.food_spawn = True

    def spawnFood(self, game_window):
        if not self.food_spawn:
            self.food_pos = [random.randrange(
                1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
            self.food_spawn = True

        pygame.draw.rect(game_window, white, pygame.Rect(
            self.food_pos[0], self.food_pos[1], 10, 10))
