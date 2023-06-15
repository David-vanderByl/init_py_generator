# This code was automatically generated from a text file.

import pygame

class View:
    def __init__(self):
        pygame.init()
        self.width = 400
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')
        self.font = pygame.font.SysFont('Arial', 20)

    def draw(self, snake, food, score):
        self.screen.fill((0, 0, 0))
        for x, y in snake.body:
            pygame.draw.rect(self.screen, (255, 255, 255), (x*self.width//20, y*self.height//20, self.width//20, self.height//20))
        pygame.draw.rect(self.screen, (255, 0, 0), (food.x*self.width//20, food.y*self.height//20, self.width//20, self.height//20))
        score_text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.update()

    def close(self):
        pygame.quit()
