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
        
        self.apple = pygame.image.load(r"C:\Users\ASUS-PC\Desktop\final_project\images\greene appel.jpg").convert()
        self.x = 300
        self.y = 300

    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))  #set the character
        pygame.display.flip()   #update the screen
    
    def move(self):
        self.x = random.randint(1,10) * 20  #move to a random position in X grid
        self.y = random.randint(1,10) * 20  #move to a random position in Y grid

class Cherry:
    def __init__(self, window):
        self.window = window    #common window/pygame screen
        
        self.apple = pygame.image.load(r"C:\Users\ASUS-PC\Desktop\final_project\images\cherry boiii.jpg").convert()
        self.x = 100
        self.y = 200

    def draw(self):
        self.window.blit(self.apple, (self.x, self.y))  #set the character
        pygame.display.flip()   #update the screen
    
    def move(self):
        self.x = random.randint(1,100) * 5  #move to a random position in X grid
        self.y = random.randint(1,100) * 5  #move to a random position in Y grid

class Poison:
    def __init__(self, window):
        self.window = window   
        
        self.poison = pygame.image.load(r"C:\Users\ASUS-PC\Desktop\final_project\images\POISON IMG.jpg").convert()
        self.x = 50
        self.y = 200

    def draw(self):
        self.window.blit(self.poison, (self.x, self.y))  
        pygame.display.flip()   
    
    def move(self):
        self.x = random.randint(1,20) * 8 
        self.y = random.randint(1,20) * 8


class Snake:
    def __init__(self, window, length): #init a speacial function that will automically called when a object created
        self.window = window    #pygame window
        self.snake = pygame.image.load(r"C:\Users\ASUS-PC\Desktop\final_project\images\box.png").convert() #load the image of snake
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

    def increase2(self):
        self.length += 2
        self.x.append(-1)
        self.y.append(-1)



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
        self.poison = Poison(self.window)
        self.poison.draw()



    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False
    
    def is_collision2(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        
        

        return False
    
    def play_background_music(self):
        pygame.mixer.music.load(r'C:\Users\ASUS-PC\Desktop\final_project\sounds\bg_music_1.mp3')
        pygame.mixer.music.play()
    
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (3, 2, 2))
        self.window.blit(score,(500,10))
    
    def show_background(self):
        bg = pygame.image.load(r'C:\Users\ASUS-PC\Desktop\final_project\images\background4.png').convert()
        self.window.blit(bg, (0,0))

    def play(self):
        self.show_background()
        self.snake.walk()
        self.apple.draw()
        self.cherry.draw()
        self.poison.draw()
        
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            print('Collision Detected')

            sound = pygame.mixer.Sound(r'C:\Users\ASUS-PC\Desktop\final_project\sounds\ding.mp3')
            pygame.mixer.Sound.play(sound)
            
            self.apple.move()
            self.cherry.move()
            self.poison.move()
            self.snake.increase()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.cherry.x, self.cherry.y):
            print('Collision Detected')

            sound = pygame.mixer.Sound(r'C:\Users\ASUS-PC\Desktop\final_project\sounds\ding.mp3')
            pygame.mixer.Sound.play(sound)
            
            self.apple.move()
            self.cherry.move()
            self.poison.move()
            self.snake.increase()
        
        for i in range(3, self.snake.length):
            if self.is_collision2(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                print('Game Over')
                pygame.mixer.music.load(r'C:\Users\ASUS-PC\Desktop\final_project\sounds\bg_music_2.ogg')
                pygame.mixer.music.stop()
        
                bg = pygame.image.load(r'C:\Users\ASUS-PC\Desktop\final_project\images\game_over.png').convert()
                self.window.blit(bg, (0,0))
                pygame.display.flip()
                
                font = pygame.font.SysFont('arial', 50)
                score = font.render(f"Score: {self.snake.length}", True, (242, 239, 237))
                self.window.blit(score,(500,10))
                pygame.display.flip()

                sound = pygame.mixer.Sound(r'C:\Users\ASUS-PC\Desktop\final_project\sounds\KL Peach Game Over III.mp3')
                pygame.mixer.Sound.play(sound)
                time.sleep(5)
                exit(0)

        if self.is_collision2(self.snake.x[0], self.snake.y[0], self.poison.x, self.poison.y):
            print('Game Over')
            pygame.mixer.music.load(r'C:\Users\ASUS-PC\Desktop\final_project\sounds\bg_music_2.ogg')
            pygame.mixer.music.stop()
            bg = pygame.image.load(r'C:\Users\ASUS-PC\Desktop\final_project\images\game_over.png').convert()
            self.window.blit(bg, (0,0))
            pygame.display.flip()
                
            font = pygame.font.SysFont('arial', 50)
            score = font.render(f"Score: {self.snake.length}", True, (242, 239, 237))
            self.window.blit(score,(500,10))
            pygame.display.flip()

            sound = pygame.mixer.Sound(r'C:\Users\ASUS-PC\Desktop\final_project\sounds\KL Peach Game Over III.mp3')
            pygame.mixer.Sound.play(sound)
            time.sleep(5)
            exit(0)


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