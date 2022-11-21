# debut du projet

import pygame
from pygame.locals import  *
import time
import random
from get_image_operation import OperationImage
SIZE = 40

class Operation:
    def __init__(self, parent_screen):
        self.imageFil = OperationImage(40, 40, "5+12", 12).image
        self.image_data = self.imageFil.tobytes()
        self.imageSize = self.imageFil.size
        self.imageMode = self.imageFil.mode
        self.image = pygame.image.fromstring(self.image_data, self.imageSize, self.imageMode)
        self.parent_screen = parent_screen
        self.x = random.randint(0,25)*SIZE
        self.y = random.randint(0,20)*SIZE
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Snake:
    def __init__(self,parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'
    def draw(self):
        self.parent_screen.fill((50, 168, 94))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
            if self.x[0] >= self.parent_screen.get_width():
                self.x[0] = 0
            if self.x[0] < 0:
               self.x[0] = self.parent_screen.get_width()-SIZE

            if self.y[0] >= self.parent_screen.get_height():
                self.y[0] = 0
            if self.y[0] < 0:
                self.y[0] = self.parent_screen.get_height()-SIZE

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((50, 168, 94))  # see rgb color picker on google
        self.snake = Snake(self.surface,7)
        self.snake.draw()
        self.operation = Operation(self.surface)
        self.operation.draw()
    def collision (self, x1, x2, y1, y2):
        if x1>x2 and x1 <= x2+ SIZE:
            if y1 >= y2 and y1 <= y2 +SIZE:
                return True
        return False
    def play(self):
        self.snake.walk()
        self.operation.draw()
        if self.collision(self.snake.x[0],self.snake.y[0], self.operation.x, self.operation.y):
            print("Collision")
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            self.play()
            time.sleep(0.2)


operation = '5+6'

if __name__ =="__main__":
    game =Game()
    game.run()

    # block_operation = OperationImage(40, 40, "5+12", 12).image
    # block_operation.save("resources/operation.jpg")
    # block_op = pygame.image.load("resources/operation.jpg").convert()
    # # block_operation.show()
    # surface.blit(block_op, (block_x+50, block_y+50))
    #
    # pygame.display.flip()
