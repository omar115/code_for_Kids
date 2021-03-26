import pygame #importing pygame library
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500,500)) #width=500, height=500

pygame.display.set_caption('First Game')


walkRight = [pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R1.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R2.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R3.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R4.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R5.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R6.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R7.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R8.png'), 
pygame.image.load('/home/akash/git_workspace/code_for_Kids/pygame_first_project/R9.png')]

x = 50
y = 50
width = 40
height = 60
vel = 5
jump = False
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
            
            if event.key == K_SPACE:
                jump = True
            
            