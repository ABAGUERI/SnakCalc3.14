# debut du projet

import pygame
from pygame.locals import  *
from get_image_operation import Operation_image

operation = '5+6'
def draw_block():
    surface.fill((50, 168, 94))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ =="__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((50, 168, 94))  # see rgb color picker on google
    block = pygame.image.load("resources/block.jpg").convert()
    print(type(block))
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))

    block_operation = Operation_image(40,40,"5+12",12).image
    block_operation.save("resources/operation.jpg")
    block_op = pygame.image.load("resources/operation.jpg").convert()
    # block_operation.show()
    surface.blit(block_op, (block_x+50, block_y+50))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key ==K_ESCAPE:
                    running =False
                if event.key == K_UP:
                    block_y -=10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
            elif event.type == QUIT:
                running = False
