import pygame #importing pygame library
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500,500)) #width=500, height=500

pygame.display.set_caption('First Game')

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == KEYDOWN:     #to get the keyboard input
            
            if event.key == K_ESCAPE:
                run = False
            
            if event.key == K_LEFT:
                x -= 5
                
            
            if event.key == K_RIGHT:
                x += 5
            
            