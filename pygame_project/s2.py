import pygame       #importing pygame library
from pygame.locals import *     #importing some global variables
import time

def draw_frame(character_x, character_y, character_direction):
    # print('T')
    window.fill((237, 161, 213))
    
    window.blit(character, (character_x, character_y))

    pygame.display.flip()

    return character_x, character_y


pygame.init()   #initialize the pygame modules


#create window
window = pygame.display.set_mode((500, 500))

window.fill((237, 161, 213))

#give a name of window
pygame.display.set_caption("My First Game")


#load the character
character = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/pygame_project/images/block.jpg')

global character_x, character_y, character_direction
character_x = 100       #character in X position
character_y = 100       #character in Y Position
character_direction = 'down'        #character direction

window.blit(character, (character_x, character_y))
pygame.display.flip()

def walk(character_x, character_y, character_direction):
    # print('true')
    if character_direction == 'up':
        character_y -= 10
        # draw_frame()
    
    if character_direction == 'down':
        character_y += 10

    if character_direction == 'left':
        character_x -= 10

    if character_direction == 'right':
        character_x += 10
    print(character_y)
    # draw_frame(character_x, character_y, character_direction)
    return character_x, character_y, character_direction
    

'''
event loop:
based on user input, the loop will start/end

'''
run = True

while run == True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            run = False

        elif event.type == KEYDOWN:     #to get the keyboard input
            
            if event.key == K_ESCAPE:
                run = False
            
            elif event.key == K_RIGHT:
                character_direction = 'right'

            elif event.key == K_LEFT:
                character_direction = 'left'
            
            elif event.key == K_UP:
                character_direction = 'up'
            
            elif event.key == K_DOWN:
                character_direction = 'down'
            
    character_x, character_y, character_direction = walk(character_x, character_y, character_direction)
    draw_frame(character_x, character_y, character_direction)
    # print('true')
    time.sleep(0.2)

