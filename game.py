import random
import pygame

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


class Game:
    def __init__(self, snake_pos):
        # game variables
        frame_size_x = 720
        frame_size_y = 480
        # snake variables
        self.snake_pos = snake_pos

        self.snake_body = [[snake_pos[0], snake_pos[1]], [snake_pos[0] - 10, snake_pos[1]],
                           [snake_pos[0] - (2 * 10), snake_pos[1]]]

        # movement variables
        self.direction = 'RIGHT'
        self.change_to = self.direction

        # food position variables
        self.food_pos = [random.randrange(1, (frame_size_x // 10))
                    * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        self.food_spawn = True

        self.score = 0

    def move(self):
        keys = pygame.key.get_pressed()
        # W -> Up; S -> Down; A -> Left; D -> Right
        if keys[pygame.K_UP]:
            self.change_to = 'UP'
        if keys[pygame.K_DOWN]:
            self.change_to = 'DOWN'
        if keys[pygame.K_LEFT]:
            self.change_to = 'LEFT'
        if keys[pygame.K_RIGHT]:
            self.change_to = 'RIGHT'
        # Esc -> Create event to quit the game
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        self.update()

    def update(self):
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10

        self.snake_body.insert(0, list(self.snake_pos))
        if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
            self.score += 1
            self.food_spawn = False
        else:
            self.snake_body.pop()

    def draw(self, game_window):
        for pos in self.snake_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))
