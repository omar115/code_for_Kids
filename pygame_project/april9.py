# Convert block into a snake
# Draw apple at random locations

import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, window):
        self.window = window
        self.apple = pygame.image.load("/home/akash/git_workspace/code_for_Kids/pygame_project/images/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


class Snake:
    def __init__(self, window, length):
        self.window = window
        self.snake = pygame.image.load("/home/akash/git_workspace/code_for_Kids/pygame_project/images/block.jpg").convert()
        self.direction = 'down'

        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.window.fill((110, 110, 5))

        for i in range(self.length):
            self.window.blit(self.snake, (self.x[i], self.y[i]))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.window, 3)
        self.snake.draw()
        self.apple = Apple(self.window)
        self.apple.draw()


    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(.2)

game = Game()
game.run()