import pygame

class Player():
    def __init__(self, snake_pos, snake_body, food_pos, snake_color):
        self.snake_pos = snake_pos
        self.snake_body = snake_body
        self.snake_color = snake_color
        self.vel = 100
        self.food_pos = food_pos

    def draw(self, game_window, color, pos):
        pygame.draw.rect(game_window, color, pygame.Rect(pos[0], pos[1], 10, 10))

    def move(self, direction):
        if direction == 'UP':
         self.snake_pos[1] -= self.vel
        if direction == 'DOWN':
         self.snake_pos[1] += self.vel
        if direction == 'LEFT':
         self.snake_pos[0] -= self.vel
        if direction == 'RIGHT':
         self.snake_pos[0] += self.vel
    
        

