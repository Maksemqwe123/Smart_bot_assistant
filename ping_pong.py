# -*- coding: utf8 -*-

import pygame
import pygame as pg
import sys
import random
pygame.init()

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
white = (255, 255, 255)
blue = (204, 255, 255)
red = (224, 0, 0)
SNAKE_COLOR = (0, 102, 0)
HEADER_COLOR = (0, 204, 153)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1
size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

screen = pg.display.set_mode(size)
pg.display.set_caption('Змейка')
timer = pg.time.Clock()
courier = pygame.font.SysFont('courier', 36)

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 < self.x < SIZE_BLOCK and 0 < self.y < SIZE_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

def get_random_empty_block():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_block:
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block

def draw_block(color, row, column):
    pg.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                 HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                 SIZE_BLOCK, SIZE_BLOCK])

snake_block = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
apple = get_random_empty_block()
d_row = buf_row = 0
d_col = buf_col = 1
total = 0
speed = 1

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('exit')
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and d_col != 0:
                buf_row = -1
                buf_col = 0
            elif event.key == pg.K_DOWN and d_col != 0:
                buf_row = 1
                buf_col = 0
            elif event.key == pg.K_LEFT and d_row != 0:
                buf_row = 0
                buf_col = -1
            elif event.key == pg.K_RIGHT and d_row != 0:
                buf_row = 0
                buf_col = 1

    screen.fill(FRAME_COLOR)
    pg.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    text_total = courier.render(f'Total: {total}', 0, white)
    text_speed = courier.render(f'Speed: {speed}', 0, white)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = blue
            else:
                color = white

            draw_block(color, row, column)

    head = snake_block[-1]
    if not head.is_inside():
        print('crash')
        pg.quit()
        sys.exit()

    draw_block(red, apple.x, apple.y)
    for block in snake_block:
        draw_block(SNAKE_COLOR, block.x, block.y)

    pygame.display.flip()

    if apple == head:
        total += 1
        speed += total % 5 == 0
        snake_block.append(apple)
        apple = get_random_empty_block()

    d_row = buf_row
    d_col = buf_col
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)

    if new_head in snake_block:
        print('crash yourself')
        pygame.quit()
        sys.exit()

    snake_block.append(new_head)
    snake_block.pop(0)

    pg.display.flip()
    timer.tick(3 + speed)