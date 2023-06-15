# This code was automatically generated from a text file.

from dataclasses import dataclass
from enum import Enum
import random

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

@dataclass
class Snake:
    body: list
    direction: Direction

@dataclass
class Food:
    x: int
    y: int

class GameOverException(Exception):
    pass

class Model:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.snake = Snake(body=[(self.width//2, self.height//2)], direction=Direction.UP)
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            if (x, y) not in self.snake.body:
                return Food(x, y)

    def update(self):
        head_x, head_y = self.snake.body[0]
        if self.snake.direction == Direction.UP:
            new_head = (head_x, head_y-1)
        elif self.snake.direction == Direction.DOWN:
            new_head = (head_x, head_y+1)
        elif self.snake.direction == Direction.LEFT:
            new_head = (head_x-1, head_y)
        elif self.snake.direction == Direction.RIGHT:
            new_head = (head_x+1, head_y)

        if new_head in self.snake.body or new_head[0] < 0 or new_head[0] >= self.width or new_head[1] < 0 or new_head[1] >= self.height:
            raise GameOverException()

        self.snake.body.insert(0, new_head)
        if new_head == (self.food.x, self.food.y):
            self.food = self.generate_food()
            self.score += 1
        else:
            self.snake.body.pop()
