# Convert block into a snake
# Draw apple at random locations
#note: convert() function optimize the image and make drawing faster
import pygame
from pygame.locals import *
import time
import random


SIZE = 40

class Apple:
    def __init__(self, window):
        self.window = window    #common window/pygame screen
        
        self.apple = pygame.image.load(r"/home/akash/git_workspace/code_for_Kids/pygame_project/images/r2.png").convert()
        self.x = 300 
        self.y = 300 

    # it will draw the character on window
    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))  #set the character
        pygame.display.flip()   #update the screen
    
    # it will move the character on screen
    def move(self):
        self.x = random.randint(1,10) * 20  #move to a random position in X grid
        self.y = random.randint(1,10) * 20  #move to a random position in Y grid

class Cherry:
    def __init__(self, window):
        self.window = window    #common window/pygame screen
        
        self.cherry = pygame.image.load(r"/home/akash/git_workspace/code_for_Kids/pygame_project/images/cherry2.png").convert()
        self.x = 100
        self.y = 200

    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))  #set the character
        pygame.display.flip()   #update the screen
    
    def move(self):
        self.x = random.randint(1,100) * 5  #move to a random position in X grid
        self.y = random.randint(1,100) * 5  #move to a random position in Y grid


class Snake:
    def __init__(self, window, length): #init a speacial function that will automically called when a object created
        self.window = window    #pygame window
        self.snake = pygame.image.load("/home/akash/git_workspace/code_for_Kids/pygame_project/images/box.png").convert() #load the image of snake
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
        # self.window.fill((60, 58, 66))     #coloring the window

        for i in range(self.length):
            self.window.blit(self.snake, (self.x[i], self.y[i]))
        pygame.display.flip()
    
    def increase(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Diamond:
    def __init__(self, window):
        self.window = window    #common window/pygame screen
        
        self.diamon = pygame.image.load(r"/home/akash/git_workspace/code_for_Kids/pygame_project/images/cherry2.png").convert()
        self.x = 150
        self.y = 250

    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))  #set the character
        pygame.display.flip()   #update the screen
    
    def move(self):
        self.x = random.randint(1,90) * 5  #move to a random position in X grid
        self.y = random.randint(1,90) * 5  #move to a random position in Y grid
    
    def game_over(self):
        exit(0)

class Game:
    def __init__(self):
        pygame.init()   #initialize the modules
        pygame.display.set_caption('Snake game using Python')
        pygame.mixer.init() # initialize the music modules
        self.play_background_music()    #call the music funtion to play music
        
        self.window = pygame.display.set_mode((700, 600))  #display pixel
        
        self.snake = Snake(self.window, 1)
        self.snake.draw()
        
        self.apple = Apple(self.window)
        self.apple.draw()
        
        self.cherry = Cherry(self.window)
        self.cherry.draw()

        self.diamond = Diamond(self.window)
        self.diamond.draw()





    def is_collision(self, x1, y1, x2, y2, x3, y3):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        
        if x1 >= x3 and x1 < x3+SIZE:
            if y1 >= y3 and y1 < y3 + SIZE:
                return True

        return False
    
    def is_collision2(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        
        

        return False
    
    def is_collision3():
        print('Do the task')
    
    def play_background_music(self):
        pygame.mixer.music.load(r'/home/akash/git_workspace/code_for_Kids/pygame_project/sounds/bg_music_2.ogg')
        pygame.mixer.music.play()
    
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (3, 2, 2))
        self.window.blit(score,(500,10))
    
    def show_background(self):
        bg = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/pygame_project/images/grass.jpg').convert()
        self.window.blit(bg, (0,0))

    def play(self):
        self.show_background()
        self.snake.walk()
        self.apple.draw()
        self.cherry.draw()
        self.diamond.draw()
        
        self.display_score()
        pygame.display.flip()
        # if snake touch any of these then the character will move and snake become large
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y, self.cherry.x, self.cherry.y):
            print('Collision Detected')

            sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/pygame_project/sounds/ding.ogg')
            pygame.mixer.Sound.play(sound)
            
            self.apple.move()
            self.cherry.move()
            self.diamond.move()
            self.snake.increase()
        
        
        
        
        
        for i in range(3, self.snake.length):
            if self.is_collision2(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print('Game Over')
                pygame.mixer.music.load(r'/home/akash/git_workspace/code_for_Kids/pygame_project/sounds/bg_music_2.ogg')
                pygame.mixer.music.stop()
        
                bg = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/pygame_project/images/game_over.png').convert()
                self.window.blit(bg, (0,0))
                pygame.display.flip()
                
                font = pygame.font.SysFont('arial', 50)
                score = font.render(f"Score: {self.snake.length}", True, (242, 239, 237))
                self.window.blit(score,(500,10))
                pygame.display.flip()

                sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/pygame_project/sounds/game_over.ogg')
                pygame.mixer.Sound.play(sound)
                time.sleep(5)
                exit(0)     # it will close your window


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