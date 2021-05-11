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
        
        # self.apple = pygame.image.load(r"C:\Users\Mahmud Reza\Documents\Python characters pyagme\apple.jpg").convert()
        self.apple = pygame.image.load(r"/home/akash/git_workspace/code_for_Kids/Pygame files/apple.jpg").convert()
        self.x = 300
        self.y = 300

    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))  #set the character
        pygame.display.flip()   #update the screen
    
    def move(self):
        self.x = random.randint(1,10) * 50
        self.y = random.randint(1,10) * 50 

class Dec:
    def __init__(self, window):
        self.window = window    # common window/pygame screen
        
        # self.dec = pygame.image.load(r"C:\Users\Mahmud Reza\Documents\download.jpg").convert()
        self.dec = pygame.image.load(r"/home/akash/git_workspace/code_for_Kids/Pygame files/download.jpg").convert()
        self.x = 400
        self.y = 450

    def draw(self):
        self.window.blit(self.dec, (self.x, self.y))  # set the character
        pygame.display.flip()   # update the screen
    
    def move(self):
        self.x = random.randint(10,20) * 50
        self.y = random.randint(10,20) * 50


class Cherry:
    def __init__(self, window):
        self.window = window    # common window/pygame screen
        
        # self.apple = pygame.image.load(r"C:\Users\Mahmud Reza\Documents\Python characters pyagme\Bomb.jpg").convert()
        self.apple = pygame.image.load(r"/home/akash/git_workspace/code_for_Kids/Pygame files/Bomb.jpg").convert()
        self.x = 500
        self.y = 600

    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))  # set the character
        pygame.display.flip()   # update the screen
    
    def move(self):
        self.x = random.randint(50,100) * 5
        self.y = random.randint(50,100) * 5



class Snake:
    def __init__(self, window, length): # init a speacial function that will automically called when a object created
        self.window = window    # pygame window
        # self.snake = pygame.image.load(r"C:\Users\Mahmud Reza\Documents\Python characters pyagme\1.png").convert() #load the image of snake
        self.snake = pygame.image.load(r"/home/akash/git_workspace/code_for_Kids/Pygame files/1.png").convert()
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

    def increase(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def decrease(self):
        self.length -= 1
        self.x.append(+1)
        self.y.append(+1)

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
        # self.window.fill((60, 58, 66))     # coloring the window

        for i in range(self.length):
            self.window.blit(self.snake, (self.x[i], self.y[i]))
        pygame.display.flip()
    

class Game:
    def __init__(self):
        pygame.init()   # initialize the modules
        pygame.display.set_caption('Snake!')
        pygame.mixer.init() # initialize the music modules
        self.play_background_music()    # call the music funtion to play music
        
        self.window = pygame.display.set_mode((1000,800))  # display pixel
        self.snake = Snake(self.window, 1)
        self.snake.draw()
        self.apple = Apple(self.window)
        self.apple.draw()
        self.cherry = Cherry(self.window)
        self.cherry.draw()
        self.dec = Dec(self.window)
        self.dec.draw()



    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        
        # if x1 >= x3 and x1 < x3+SIZE:
        #     if y1 >= y3 and y1 < y3 + SIZE:
        #         return True

        return False
    
    def is_collision2(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        
        

        return False
    
    def play_background_music(self):
        # pygame.mixer.music.load(r'C:\Users\Mahmud Reza\Downloads\song.mp3')
        # pygame.mixer.music.load(r'C:\Users\Mahmud Reza\Downloads\song.mp3')
        pygame.mixer.music.load(r'/home/akash/git_workspace/code_for_Kids/Pygame files/song.ogg')
        pygame.mixer.music.play()
    
    def display_score(self):
        font = pygame.font.SysFont('lucida handwriting', 30)
        score = font.render(f"Score: {self.snake.length}", True, (51,4,3))
        self.window.blit(score,(800,70))
    
    def show_background(self):
        # bg = pygame.image.load(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\grass.jpg').convert()
        bg = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/Pygame files/grass.jpg').convert()
        self.window.blit(bg, (0,0))

    def play(self):
        self.show_background()
        self.snake.walk()
        self.apple.draw()
        self.cherry.draw()
        self.dec.draw()
        
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            print('Collision Detected: Apple')

            # sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Downloads\Chewing-popcorn-single-crunch-A-www.fesliyanstudios.com.mp3')
            sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/Pygame files/s1.ogg')
            pygame.mixer.Sound.play(sound)
            
            self.apple.move()
            self.snake.increase()

        # if self.is_collision(self.snake.x[0], self.snake.y[0], self.dec.x, self.dec.y):
        #     print('Collision Detected: Decreaser')

        #     # sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Downloads\lose sound 1_0.wav')
        #     sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/Pygame files/lose sound 1_0.wav')
        #     pygame.mixer.Sound.play(sound)
            
        #     self.dec.move()
        #     # self.snake.decrease()
        #     font = pygame.font.SysFont('lucida handwriting', 30)
        #     score = font.render(f"Score: {self.snake.length}", True, (224,255,255))
        #     self.window.blit(score,(800,70))
        #     pygame.display.flip()
            

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.cherry.x, self.cherry.y):
            print('Collision Detected: Bomb')

            # pygame.mixer.music.load(r'C:\Users\Mahmud Reza\Downloads\song.mp3')
            pygame.mixer.music.load(r'/home/akash/git_workspace/code_for_Kids/Pygame files/song.ogg')
            pygame.mixer.music.stop()
        
            # bg = pygame.image.load(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\Game Over.jpg').convert()
            bg = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/Pygame files/Game Over.jpg').convert()
            self.window.blit(bg, (0,0))
            pygame.display.flip()
                
            font = pygame.font.SysFont('lucida handwriting', 30)
            print(self.snake.length)
            score = font.render(f"Score: {(self.snake.length) - 1}", True, (224,255,255))
            self.window.blit(score,(800,70))
            pygame.display.flip()

            # sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\Game_Over.mp3')
            sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/Pygame files/Game_Over.ogg')
            pygame.mixer.Sound.play(sound)
            time.sleep(5)
            exit(0)

            # sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\exp.mp3')
            # pygame.mixer.Sound.play(sound)
            
            # self.cherry.move()
            # # self.snake.increase()
            # # time.sleep(5)
            # exit(0)

        # for i in range(1, self.snake.length):
        # if self.is_collision(self.snake.x[0], self.snake.y[0], self.dec.x, self.dec.y):
        #     print('Collision Detected: Decreaser')

        #     # sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Downloads\lose sound 1_0.wav')
        #     sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/Pygame files/lose sound 1_0.wav')
        #     pygame.mixer.Sound.play(sound)
            
        #     self.dec.move()
        #     # self.snake.decrease()
        #     font = pygame.font.SysFont('lucida handwriting', 50)
        #     score = font.render(f"Score: {self.snake.length - 1}", True, (225,255,255))
        #     self.window.blit(score,(800,70))
        #     pygame.display.flip()

        for i in range(3, self.snake.length):
            if self.is_collision2(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print('Game Over')
                # pygame.mixer.music.load(r'C:\Users\Mahmud Reza\Downloads\song.mp3')
                pygame.mixer.music.load(r'/home/akash/git_workspace/code_for_Kids/Pygame files/song.ogg')
                pygame.mixer.music.stop()
        
                # bg = pygame.image.load(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\Game Over.jpg').convert()
                bg = pygame.image.load(r'/home/akash/git_workspace/code_for_Kids/Pygame files/Game Over.jpg').convert()
                self.window.blit(bg, (0,0))
                pygame.display.flip()
                
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.dec.x, self.dec.y):
                print('Collision Detected: Decreaser')

                # sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Downloads\lose sound 1_0.wav')
                sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/Pygame files/lose sound 1_0.wav')
                pygame.mixer.Sound.play(sound)
                
                self.dec.move()
                # self.snake.decrease()
                font = pygame.font.SysFont('lucida handwriting', 50)
                score = font.render(f"Score: {self.snake.length - 1}", True, (225,255,255))
                self.window.blit(score,(800,70))
                pygame.display.flip()
            else:
                font = pygame.font.SysFont('lucida handwriting', 30)
                score = font.render(f"Score: {self.snake.length}", True, (224,255,255))
                self.window.blit(score,(800,70))
                pygame.display.flip()

                # sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\Game_Over.mp3')
                sound = pygame.mixer.Sound(r'/home/akash/git_workspace/code_for_Kids/Pygame files/Game_Over.ogg')
                pygame.mixer.Sound.play(sound)
                time.sleep(5)
                exit(0)

            

        # for i in range(3, self.snake.length):
        #     if self.is_collision2(self.snake.x[0], self.snake.y[0], self.cherry.x[i], self.cherry.y[i]):
        #         print('Game Over')
        #         pygame.mixer.music.load(r'C:\Users\Mahmud Reza\Downloads\song.mp3')
        #         pygame.mixer.music.stop()
        
        #         bg = pygame.image.load(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\Game Over.jpg').convert()
        #         self.window.blit(bg, (0,0))
        #         pygame.display.flip()
                
        #         font = pygame.font.SysFont('lucida handwriting', 30)
        #         score = font.render(f"Score: {self.snake.length}", True, (224,255,255))
        #         self.window.blit(score,(800,70))
        #         pygame.display.flip()

        #         sound = pygame.mixer.Sound(r'C:\Users\Mahmud Reza\Documents\Python characters pyagme\Game_Over.mp3')
        #         pygame.mixer.Sound.play(sound)
        #         time.sleep(5)
        #         exit(0)

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