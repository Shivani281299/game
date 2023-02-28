import pygame
from pygame.locals import *
import time

SIZE =40

class fruits:
    def __init__(self,parent_screen):
        # self.fruits_image = pygame.image.load(f"D:\\test\\assesst\\fruits_images\\1.png").convert()
        self.fruits_image = pygame.transform.scale(pygame.image.load(f'D:\\test\\assesst\\fruits_images\\1.png'), (50, 50))
        self.parent_screen =parent_screen
        self.x =SIZE*3
        self.y= SIZE*3

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.fruits_image, (self.x, self.y))
        pygame.display.update()

class Snake:
    def __init__(self,parent_screen,length):
        self.length = length
        self.parent_screen =parent_screen
        self.block = pygame.image.load(f"D:\\test\\assesst\\block_image\\block.png").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction ='down'

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.update()


    def move_left(self):
        self.direction = 'left'
        # self.x -=10
        # self.draw()

    def move_right(self):
        self.direction='right'
        # self.x += 10
        # self.draw()

    def move_up(self):
        self.direction='up'
        # self.y -= 10
        # self.draw()

    def move_down(self):
        self.direction='down'
        # self.y += 10
        # self.draw()

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= SIZE

        if self.direction == 'down':
            self.y[0] += SIZE

        if self.direction == 'left':
            self.x[0] -= SIZE

        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()






class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((110, 110, 5))
        self.snake =Snake(self.surface,6)
        self.snake.draw()
        self.fruits = fruits(self.surface)
        self.fruits.draw()

    def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1 <=x2+SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True




    def play(self):
        self.snake.walk()
        self.fruits.draw()


    def run(self):

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                        # fruits_y -= 10
                        # draw_block()

                    if event.key == K_DOWN:
                        self.snake.move_down()
                        # fruits_y += 10
                        # draw_block()

                    if event.key == K_LEFT:
                        self.snake.move_left()
                        # fruits_x -= 10
                        # draw_block()

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        # fruits_x += 10
                        # draw_block()


                elif event.type == QUIT:
                    running = False

            # self.snake.walk()
            # self.snake.draw()
            self.play()
            time.sleep(0.3)


if __name__ =='__main__':
    game =Game()
    game.run()






