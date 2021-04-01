import pygame
from pygame.locals import *

class Snake:
    def __init__(self, window):
        self.window = window
        self.block = pygame.image.load('images/block.jpg').convert()
        self.x = 100
        self.y = 100
    
    def draw(self):
        self.window.fill((110,100,5))
        self.window.blit(self.block, (self.x, self.y))
        pygame.window.flip()
        

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((500, 500))
        self.window.fill((110,100,5))
        self.snake = Snake(self.window)
        self.snake.draw()
        
    def run(self):
        pass

