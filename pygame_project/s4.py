from s3 import draw_frame
import pygame       #importing pygame library
from pygame.locals import *     #importing some global variables
import time

pygame.init()   #initialize the pygame modules


#create window
window = pygame.display.set_mode((500, 480))

#give a name of window
pygame.display.set_caption("Leenat Game")

bg = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/pygame_first_project/images/bg.jpg')
global character, character_x, character_y, character_direction
character = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/pygame_first_project/images/standing.png')
character_x = 50
character_y = 400
character_direction = 'right'
window.blit(bg, (0,0))
window.blit(character, (character_x, character_y))
pygame.display.update()

left = False
right = False


def draw_frame2(character_x, character_y, character_direction):
    if right == True:
        window.blit(character_x, (character_x+5, character_y))
    pygame.display.update()


run = True

while run == True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            run = False

        elif event.type == KEYDOWN:     #to get the keyboard input
            
            if event.key == K_ESCAPE:
                run = False
            
            elif event.key == K_RIGHT:
                character_x += 5
                character_direction = 'right'
                right = True
                left = False
                draw_frame2(character_x, character_y, character_direction)
        
        

