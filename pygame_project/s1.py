import pygame       #importing pygame library
from pygame.locals import *     #importing some global variables
pygame.init()   #initialize the pygame modules


#create window
window = pygame.display.set_mode((500, 500))

#give a name of window
pygame.display.set_caption("My First Game")

window.fill((237, 161, 213))

character = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/pygame_project/images/block.jpg')
character_x = 100
character_y = 100

window.blit(character, (character_x, character_y))

pygame.display.flip()

'''
event loop:
based on user input, the loop will start/end

'''
run = True

while run == True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            run = False