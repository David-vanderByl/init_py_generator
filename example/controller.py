# This code was automatically generated from a text file.

import pygame
from model import Direction, GameOverException

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.model.snake.direction != Direction.DOWN:
                        self.model.snake.direction = Direction.UP
                    elif event.key == pygame.K_DOWN and self.model.snake.direction != Direction.UP:
                        self.model.snake.direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT and self.model.snake.direction != Direction.RIGHT:
                        self.model.snake.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT and self.model.snake.direction != Direction.LEFT:
                        self.model.snake.direction = Direction.RIGHT

            try:
                self.model.update()
            except GameOverException:
                running = False

            self.view.draw(self.model.snake, self.model.food, self.model.score)

        self.view.close()
