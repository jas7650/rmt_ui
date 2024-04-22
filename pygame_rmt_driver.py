import pygame
import numpy as np
import sys
from objects.ModelTemp import ModelTemp
from objects.RMTButton import RMTButton

BLACK = pygame.Color('black')
WHITE = pygame.Color('grey')
GREEN = pygame.Color('green3')
RED = pygame.Color('red3')
YELLOW = pygame.Color('yellow3')
BROWN = pygame.Color('burlywood4')


def main():
    global SCREEN, CLOCK
    pygame.init()
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h

    BLOCK_WIDTH = screen_width/4
    BLOCK_HEIGHT = screen_height/4

    SCREEN = pygame.display.set_mode((screen_width, screen_height))
    CLOCK = pygame.time.Clock()

    rmt_model = ModelTemp(10, 10)
    tiles = []
    label_tiles = []
    label_tiles.append(RMTButton(0, 0, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    label_tiles.append(RMTButton(0, 1, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    label_tiles.append(RMTButton(0, 2, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    label_tiles.append(RMTButton(0, 3, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    tiles.append(label_tiles)

    label_values = []
    label_values.append(RMTButton(1, 0, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    label_values.append(RMTButton(1, 1, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    label_values.append(RMTButton(1, 2, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    label_values.append(RMTButton(1, 3, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    tiles.append(label_values)

    increase_buttons = []
    increase_buttons.append(RMTButton(2, 0, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    increase_buttons.append(RMTButton(2, 1, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    increase_buttons.append(RMTButton(2, 2, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    increase_buttons.append(RMTButton(2, 3, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    tiles.append(increase_buttons)

    decrease_buttons = []
    decrease_buttons.append(RMTButton(3, 0, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    decrease_buttons.append(RMTButton(3, 1, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    decrease_buttons.append(RMTButton(3, 2, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    decrease_buttons.append(RMTButton(3, 3, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN, rmt_model))
    tiles.append(decrease_buttons)

    tiles = np.asarray(tiles)
    for row_tiles in tiles:
        for tile in row_tiles:
            tile.process()
    while True:
        rects = drawGUI(tiles, BLOCK_WIDTH, BLOCK_HEIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def drawGUI(tiles, BLOCK_WIDTH, BLOCK_HEIGHT):
    rects = []
    for row in range(0, 4):
        row_rects = []
        for col in range(0, 4):
            outline = pygame.Rect(col*BLOCK_WIDTH, row*BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
            button = pygame.Rect(col*BLOCK_WIDTH, row*BLOCK_HEIGHT, BLOCK_WIDTH-2, BLOCK_HEIGHT-2)
            pygame.draw.rect(SCREEN, BLACK, outline, 2)
            pygame.draw.rect(SCREEN, WHITE, button)
            row_rects.append(button)
        rects.append(row_rects)
    return np.asarray(rects)


if __name__ == "__main__":
    main()
